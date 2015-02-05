#!/usr/bin/env python3

import re
import os
import sys
from glob import iglob
import urllib.parse
import html.parser
import itertools

import inflection
from bs4 import BeautifulSoup

# Unless you're really going to hack on the API generator, don't hammer
# the developer site needlessly. Currently, mirroring the whole site
# results in about 26MB on disk. I may eventually do some more intelligent
# scraping, downloading, and disk caching to avoid this wget.

# That said, here is my usual process:
# $ wget -mk https://developer.zendesk.com/rest_api/docs/core/introduction
# $ cp -R developer.zendesk.com developer.zendesk.com.orig
# $ ./clean.py
# $ cp -R developer.zendesk.com developer.zendesk.com.cleaned
#
# For each patch.* file
# cd developer.zendesk.com
# $ patch -p1 < ../patch.file
#
# $ cd ..
# $ ./api_gen.py

# If I find that more patching is needed to get what I want, then:
# $ vim edit whatever
# $ diff -r -u developer.zendesk.com developer.zendesk.com.cleaned > api_gen.patch.new
# If that all checks out, then api_gen.patch.new becomes the new api_gen.patch

# Then, once all is well:
# cp zdesk_api.py ../zdesk/

html_parser = html.parser.HTMLParser()

skip_files=[
    'introduction',
    'changes_roadmap',
    'side_loading',
    ]

api_actions = [
    'autocomplete',
    'clone',
    'compact',
    'create',
    'destroy',
    'detect',
    'execute',
    'exports',
    'import',
    'imports',
    'make',
    'mark',
    'me',
    'merge',
    'preview',
    'recover',
    'redact',
    'reorder',
    'search',
    'show',
    'verify',
    ]

default_status = '200'

with open('api_template.py', 'r') as template_file:
    template = template_file.read()

#os.chdir('old.developer.zendesk.com/documentation/rest_api')
#os.chdir('developer.zendesk.com/rest_api/docs/core')

api_items = {}
duplicate_api_items = {}
for doc_file in iglob(os.path.join('developer.zendesk.com', 'rest_api', 'docs', '*', '*')):
    if '.html' in doc_file or '.orig' in doc_file or os.path.split(doc_file)[1] in skip_files:
        continue

    with open(doc_file, 'r') as doc:
        soup = BeautifulSoup(doc)

    status_group = []
    duplicate_status_group = []

    for code in soup.find_all(['code', 'pre']):
        text = code.get_text()
        #if re.search(r'<code>(OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT) .*\.json', line):
        #    line = re.sub(r'(<p>|<code>|</p>|</code>|/api/v2)', '', line)
        #    line = re.sub('&#123;', '{', line)
        #    line = re.sub('&#125;', '}', line)
        #    print(line, end='')
        match = re.match(r'\s*(OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT) (.*)', text)
        if match:
            is_singular = False
            api_item = {}
            api_item['docpage'] = doc_file
            api_item['path_params'] = []
            api_item['opt_path_params'] = []
            api_item['opt_path'] = ''
            api_item['query_params'] = []
            api_item['opt_query_params'] = []
            api_item['status'] = default_status

            api_item['method'] = match.group(1)
            path = match.group(2)

            # parse into a url object for easily accessing the parts of the whole url
            url = urllib.parse.urlsplit(path)

            api_item['path'] = url.path

            # Split the path and remove the first (always empty) item and /api/v2
            param_indexes = []
            path_parts = url.path.split('/')

            if path_parts[-1].startswith('{') or api_item['method'] == 'POST':
                # Getting a single object
                # e.g. GET /api/v2/tickets/{id}.json
                is_singular = True

            del path_parts[0]
            del path_parts[0]
            del path_parts[0]

            make_next_singular = False
            path_parts.reverse()
            for i, path_part in enumerate(path_parts):
                part, ext = os.path.splitext(path_part)
                if ext != '':
                    if ext != '.json':
                        print('Non-JSON endpoint encountered!!')
                    path_parts[i] = part

                if part.startswith('{'):
                    api_item['path_params'].append(part[1:-1])
                    param_indexes.append(i)
                    make_next_singular = True
                    continue

                if make_next_singular:
                    make_next_singular = False
                    path_parts[i] = inflection.singularize(path_parts[i])

            path_len = len(path_parts)

            for i in param_indexes[::-1]:
                del path_parts[i]

            expanded_parts = []
            [expanded_parts.extend(part.split('_')) for part in path_parts]
            has_action = True in [action in expanded_parts
                    for action in api_actions]

            query_params = urllib.parse.parse_qsl(url.query)
            for query_items in query_params:
                api_item['query_params'].append(query_items[0])

            path_parts.reverse()
            name = '_'.join(path_parts)
            if is_singular:
                name = inflection.singularize(name)

            if not has_action:
                if api_item['method'] == 'DELETE':
                    name = name + '_delete'
                elif api_item['method'] == 'PUT':
                    name = name + '_update'
                elif api_item['method'] == 'POST':
                    name = name + '_create'
                elif api_item['method'] == 'GET' and is_singular:
                    name = name + '_show'
                elif (
                    api_item['method'] == 'GET' and
                    len(api_item['path_params']) == 0
                   ):
                    name = name + '_list'
            else:
                # one hard corner case with 'me' and 'sessions delete'
                if 'me' in expanded_parts and api_item['method'] == 'DELETE':
                    name = name + '_delete'

            api_item['path_params'].reverse()
            api_item['query_params'].reverse()

            if name in api_items:
                if name not in duplicate_api_items:
                    duplicate_api_items[name] = []
                duplicate_api_items[name].append(api_item)
                duplicate_status_group.append(name)
                continue

            api_items[name] = api_item
            status_group.append(name)

            continue

        match = re.match(r'\s*Status: ([0-9]{3})', text)
        if match:
           status = match.group(1)
           for name in status_group:
               api_items[name]['status'] = status
           for name in duplicate_status_group:
               for item in duplicate_api_items[name]:
                   item['status'] = status
           del status_group[:]
           del duplicate_status_group[:]

content = ''
should_keep = ''
names = list(duplicate_api_items.keys())
names.sort()

for name in names:
    for dupe in duplicate_api_items[name]:
        item = api_items[name]
        if (
            dupe['path'] == item['path'] and
            dupe['method'] == item['method'] and
            dupe['status'] == item['status'] and
            False not in [i == j for i, j in itertools.zip_longest(
                dupe['path_params'], item['path_params'])] and
            False not in [i == j for i, j in itertools.zip_longest(
                sorted(dupe['query_params']), sorted(item['query_params']))]
           ):
            # Everything is the same, so discard this duplicate
            content += "    # Duplicate API endpoint discarded: {} from {}\n".format(name, dupe['docpage'])
        elif (
            dupe['method'] == item['method'] and
            dupe['status'] == item['status'] and
            False not in [i == j for i, j in itertools.zip_longest(
                sorted(dupe['query_params']), sorted(item['query_params']))]
            ):
            # Only the path parameters differ, so we have optional arguments

            # Common parameters are all required
            required = set(dupe['path_params']) & set(item['path_params'])

            # Optional parameters are only in one endpoint
            optional = list((set(dupe['path_params']) | set(item['path_params'])) - required)

            if len(set(item['path_params']) - required) == 0:
                # The item is the base function and the dupe has the optional arguments
                # Just need to add the optional arguments
                item['opt_path_params'] = optional
                item['opt_path'] = dupe['path']
            elif len(set(dupe['path_params']) - required) == 0:
                # The dupe is the base function and the item has the optional arguments
                # Need to swap the dupe with the item and then add the optional arguments
                dupe_path = dupe['path']
                item = dupe
                item['opt_path_params'] = optional
                item['opt_path'] = dupe_path
            else:
                content += "    # Duplicate ambiguous API endpoint: {} from {}\n".format(name, dupe['docpage'])
                continue
        elif (
            dupe['path'] == item['path'] and
            dupe['method'] == item['method'] and
            dupe['status'] == item['status'] and
            False not in [i == j for i, j in itertools.zip_longest(
                dupe['path_params'], item['path_params'])]
            ):
                # Only the query parameters differ, so we have optional named arguments
                item['opt_query_params'] = list(set(item['query_params'].copy() +
                                               item['opt_query_params'] +
                                               dupe['query_params']))
                item['query_params'] = []
        else:
            should_keep += "\n"
            should_keep += "    # Duplicate API endpoint that differs: {} from {}\n".format(name, dupe['docpage'])
            should_keep += "    # Original definition located here:    {} from {}\n".format(name, item['docpage'])
            should_keep += '    # {}\n'.format(name)
            should_keep += '    #    Path: {}\n'.format(dupe['path'])
            should_keep += '    #    Method: {}\n'.format(dupe['method'])
            should_keep += '    #    Status: {}\n'.format(dupe['status'])
            should_keep += '    #    Parameters:\n'
            for param in dupe['path_params']:
                should_keep += '    #        {}\n'.format(param)
            should_keep += '    #    Query Parameters:\n'
            for param in dupe['query_params']:
                should_keep += '    #        {}\n'.format(param)
            should_keep += '    # Original definition:\n'
            should_keep += '    #    Path: {}\n'.format(item['path'])
            should_keep += '    #    Method: {}\n'.format(item['method'])
            should_keep += '    #    Status: {}\n'.format(item['status'])
            should_keep += '    #    Parameters:\n'
            for param in item['path_params']:
                should_keep += '    #        {}\n'.format(param)
            should_keep += '    #    Query Parameters:\n'
            for param in item['query_params']:
                should_keep += '    #        {}\n'.format(param)
            should_keep += "\n"

if should_keep:
    content += '\n'
    content += should_keep

if content:
    content += '\n'

names = list(api_items.keys())
names.sort()

def sanitize(q):
    return q.replace('[', '_').replace(']', '')

for name in names:
    item = api_items[name]

    # Sorting the parameters alphabetically should prevent needless differences
    # when small changes are made in different locations, so the order will be
    # the same regardless as to which parameter is found first.
    item['opt_path_params'].sort()
    item['opt_query_params'].sort()

    path_fmt_args = ', '.join([p + '=' + p for p in item['path_params']])

    paramspec = ', '.join(item['path_params'])
    queryspec = ', '.join([sanitize(q) for q in item['query_params']])
    if(paramspec and queryspec):
        paramspec += ', '
    argspec = paramspec + queryspec

    if item['method'] in ['POST', 'PUT']:
        if argspec:
            argspec += ', '
        argspec += 'data'

    if item['opt_path_params']:
        if argspec:
            argspec += ', '
        argspec += '=None, '.join(item['opt_path_params']) + '=None'

    if item['opt_query_params']:
        if argspec:
            argspec += ', '
        argspec += '=None, '.join([sanitize(q) for q in item['opt_query_params']]) + '=None'

    if argspec:
        argspec += ', '
    argspec += '**kwargs'

    content += '    def {}(self, {}):\n'.format(name, argspec)
    content += '        "http://{}"\n'.format( item['docpage'])
    content += '        api_path = "{}"\n'.format(item['path'])

    if item['path_params']:
        content += '        api_path = api_path.format({})\n'.format(path_fmt_args)

    if item['opt_path']:
        opt_test = ' and '.join(item['opt_path_params'])
        if path_fmt_args:
            path_fmt_args += ', '
        path_fmt_args = path_fmt_args + ', '.join([p + '=' + p for p in item['opt_path_params']])
        content += '        if {}:\n'.format(opt_test)
        content += '            api_opt_path = "{}"\n'.format(item['opt_path'])
        content += '            api_path = api_opt_path.format({})\n'.format(path_fmt_args)

    if item['query_params'] or item['opt_query_params']:
        content += '        api_query = {}\n'

    if item['query_params']:
        content += '        api_query.update({\n'
        for q in item['query_params']:
            content += '            "{}": {},\n'.format(q, sanitize(q))
        content += '        })\n'

    for q in item['opt_query_params']:
        content += '        if {}:\n'.format(sanitize(q))
        content += '            api_query.update({\n'
        content += '                "{}": {},\n'.format(q, sanitize(q))
        content += '            })\n'

    # todo: query may be required
    #if item['opt_query_params']:
    #    opt_test = ' or '.join([sanitize(q) for q in item['opt_query_params']])
    #    content += '        if not ({}):\n'.format(opt_test)
    #    content += '            pass\n'

    content += '        return self.call(api_path'

    if item['query_params'] or item['opt_query_params']:
        content += ', query=api_query'

    if item['method'] != 'GET':
        content += ', method="{}"'.format(item['method'])

    if item['status'] != '200':
        content += ', status={}'.format(item['status'])

    if item['method'] in ['POST', 'PUT']:
        content += ', data=data'

    content += ', **kwargs)\n\n'

with open('zdesk_api.py', 'w') as f:
    f.write(template.format(content))

