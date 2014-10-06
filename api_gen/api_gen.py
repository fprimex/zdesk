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
# $ wget -mk https://developer.zendesk.com/

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
    if '.html' in doc_file or os.path.split(doc_file)[1] in skip_files:
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
        match = re.match(r'(OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT) (.*)', text)
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

            url = html_parser.unescape(path)
            url = urllib.parse.urlsplit(url)

            # Split the path and remove the first (always empty) item and /api/v2
            param_indexes = []
            path_parts = url.path.split('/')

            if path_parts[-1].startswith('{'):
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

            api_item['path'] = re.sub(r'&#123;.*&#125;', '{}', url.path)

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
                    name = name + '_create'
                elif api_item['method'] == 'POST':
                    name = name + '_update'
                elif api_item['method'] == 'GET' and is_singular:
                    name = name + '_show'
                elif (
                    api_item['method'] == 'GET' and
                    len(api_item['path_params']) == 0 and
                    len(api_item['query_params']) == 0
                   ):
                    name = name + '_list'

            api_item['path_params'].reverse()
            api_item['query_params'].reverse()

            if name in api_items:
                duplicate_api_items[name] = api_item
                duplicate_status_group.append(name)
                continue

            api_items[name] = api_item
            status_group.append(name)

            continue

        match = re.match(r'Status: ([0-9]{3})', text)
        if match:
           status = match.group(1)
           for name in status_group:
               api_items[name]['status'] = status
           for name in duplicate_status_group:
               duplicate_api_items[name]['status'] = status
           del status_group[:]
           del duplicate_status_group[:]

content = ''
should_keep = ''
names = list(duplicate_api_items.keys())
names.sort()

for name in names:
    dupe = duplicate_api_items[name]
    item = api_items[name]
    if (
        dupe['path'] == item['path'] and
        dupe['method'] == item['method'] and
        dupe['status'] == item['status'] and
        False not in [i == j for i, j in itertools.zip_longest(
            dupe['path_params'], item['path_params'])] and
        len(item['query_params']) == len(
            set(dupe['query_params']) & set(item['query_params']))
       ):
        # Everything is the same, so discard this duplicate
        content += "    # Duplicate API endpoint discarded: {} from {}\n".format(name, dupe['docpage'])
    elif (
        dupe['method'] == item['method'] and
        dupe['status'] == item['status'] and
        len(item['query_params']) == len(
            set(dupe['query_params']) & set(item['query_params']))
        ):
        # Only the path parameters differ, so we have optional arguments

        # Common parameters are all required
        required = set(dupe['path_params']) & set(item['path_params'])

        # Optional parameters are only in one endpoint
        optional = (set(dupe['path_params']) | set(item['path_params'])) - required

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
            # Only the query parameters differ, so we have optional, either/or arguments
            item['opt_query_params'] = item['query_params']
            item['opt_query_params'] += dupe['query_params']
            item['query_params'] = []
    else:
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

if should_keep:
    content += '\n'
    content += should_keep

if content:
    content += '\n\n'

names = list(api_items.keys())
names.sort()

def sanitize(q):
    return q.replace('[', '_').replace(']', '')

for name in names:
    item = api_items[name]

    path_fmt_args = ', '.join([p + '=' + p for p in item['path_params']])

    paramspec = ', '.join(item['path_params'])
    queryspec = ', '.join([sanitize(q) for q in item['query_params']])
    if(paramspec and queryspec):
        paramspec += ', '
    argspec = paramspec + queryspec

    if item['opt_path_params']:
        if argspec:
            argspec += ', '
        argspec += '=None, '.join(item['opt_path_params']) + '=None'

    if item['opt_query_params']:
        if argspec:
            argspec += ', '
        argspec += '=None, '.join([sanitize(q) for q in item['opt_query_params']]) + '=None'

    if item['method'] == 'POST':
        if argspec:
            argspec += ', '
        argspec += 'data'

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

    if item['query_params']:
        content += '        api_query = {\n'
        for q in item['query_params']:
            content += '            "{}": {},\n'.format(q, sanitize(q))
        content += '        }\n'

    for q in item['opt_query_params']:
        content += '        if {}:\n'.format(q)
        content += '            api_query = {\n'
        content += '                "{}": {},\n'.format(q, sanitize(q))
        content += '            }\n'
    if item['opt_query_params']:
        opt_test = ' or '.join(item['opt_query_params'])
        content += '        if not ({}):\n'.format(opt_test)
        content += '            pass # todo: raise error here, one query is required\n'

    content += '        return self.call(api_path'

    if item['query_params'] or item['opt_query_params']:
        content += ', api_query'

    if item['method'] != 'GET':
        content += ', "{}"'.format(item['method'])

    if item['status'] != '200':
        content += ', {}'.format(item['status'])

    if item['method'] == 'POST':
        content += ', data'

    content += ', **kwargs)\n\n'

print(template.format(content))

