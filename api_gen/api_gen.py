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

# $ wget -mk http://www.developer.zendesk.com/

html_parser = html.parser.HTMLParser()

skip_files=[
    'introduction',
    'changes_roadmap',
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

dev_site = 'http://developer.zendesk.com/rest_api/docs/core'
#os.chdir('old.developer.zendesk.com/documentation/rest_api')
os.chdir('developer.zendesk.com/rest_api/docs/core')

api_items = {}
duplicate_api_items = {}
for doc_file in iglob('*'):
    if '.html' in doc_file or doc_file in skip_files:
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
            api_item['query_params'] = []
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
        len(item['path_params']) == len(
            set(dupe['path_params']) & set(item['path_params']))
       ):
        content += "    # Duplicate API endpoint discarded: {} from {}\n".format(name, dupe['docpage'])
    else:
        should_keep += "    # Duplicate API endpoint that differs: {} from {}\n".format(name, dupe['docpage'])
        should_keep += '    # {}\n'.format(name)
        should_keep += '    #    Path: {}\n'.format(dupe['path'])
        should_keep += '    #    Method: {}\n'.format(dupe['method'])
        should_keep += '    #    Status: {}\n'.format(dupe['status'])
        should_keep += '    #    Parameters:\n'
        for param in dupe['path_params']:
            should_keep += '    #        {}\n'.format(param)
        should_keep += '    #    Query Parameters:'
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

    if item['method'] == 'POST':
        if argspec:
            argspec += ', '
        argspec += 'data'

    if argspec:
        argspec += ', '
    argspec += '**kwargs'

    content += '    def {}(self, {}):\n'.format(name, argspec)
    content += '        "{}/{}"\n'.format(dev_site, item['docpage'])
    content += '        api_path = "{}"\n'.format(item['path'])

    if item['path_params']:
        content += '        api_path = api_path.format({})\n'.format(path_fmt_args)

    if item['query_params']:
        content += '        api_query = {\n'
        for q in item['query_params']:
            content += '            "{}": {},\n'.format(q, sanitize(q))
        content += '        }\n'

    content += '        return self.call(api_path'

    if item['query_params']:
        content += ', api_query'

    if item['method'] != 'GET':
        content += ', "{}"'.format(item['method'])

    if item['status'] != '200':
        content += ', {}'.format(item['status'])

    if item['method'] == 'POST':
        content += ', data'

    content += ', **kwargs)\n\n'

print(template.format(content))

