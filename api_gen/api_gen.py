#!/usr/bin/env python3

import html.parser
import itertools
import os
import re
import shutil
import subprocess
import urllib.parse

from bs4 import BeautifulSoup
import inflection
import requests


# See README.md for documentation.

html_parser = html.parser.HTMLParser()

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
    'logout',
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
    'update',
    'verify',
    ]

with open('api_template.py', 'r') as template_file:
    template = template_file.read()

# os.chdir('old.developer.zendesk.com/documentation/rest_api')
# os.chdir('developer.zendesk.com/rest_api/docs/core')

zen_url = 'https://developer.zendesk.com'

docpages = {
    'core': '/rest_api/docs/core/introduction',
    'webportal': '/rest_api/docs/web-portal/webportal_introduction',
    'hc': '/rest_api/docs/help_center/introduction',
    'zopim': '/rest_api/docs/zopim/introduction',
    'voice': '/rest_api/docs/voice-api/voice',
    'nps': '/rest_api/docs/nps-api/introduction',
}

skippages = [
    '/rest_api/docs/core/introduction',
    '/rest_api/docs/core/getting_started',
    '/rest_api/docs/core/api_changes',
    '/rest_api/docs/core/restrictions',
    '/rest_api/docs/help_center/introduction',
    '/rest_api/docs/zopim/introduction',
    '/rest_api/docs/zopim/restrictions',
    '/rest_api/docs/zopim/changes_roadmap',
    '/rest_api/docs/web-portal/webportal_introduction',
    '/rest_api/docs/nps-api/introduction',
]

skipfiles = [
    'core_introduction',
    'webportal_webportal_introduction',
    'hc_introduction',
    'zopim_introduction',
    'nps_introduction',
]

apidocs = 'apidocs'

if os.path.isdir(apidocs):
    shutil.rmtree(apidocs)

if not os.path.isdir(apidocs + '_orig'):
    os.makedirs(apidocs + '_orig')

os.chdir(apidocs + '_orig')

for category in docpages:
    filename = category + '_' + os.path.basename(docpages[category])

    if os.path.isfile(filename):
        with open(filename, 'rb') as fin:
            content = fin.read()
    else:
        req = requests.get(zen_url + docpages[category])
        content = req.content

        with open(filename, 'wb') as fout:
            fout.write(content)

    soup = BeautifulSoup(content, "html.parser")
    sidenav = soup(attrs={'class': 'docs-sidenav'})[0]

    for a in sidenav.find_all('a'):
        link = a.attrs['href']
        filename = category + '_' + os.path.basename(link)

        if link[0] == '#':
            continue
        if link in skippages:
            continue
        if os.path.isfile(filename):
            continue

        req = requests.get(zen_url + link)
        text = BeautifulSoup(req.content, "html.parser")

        pretty_text = text.prettify()
        if not pretty_text:
            # In the case of prettify killing the whole page
            pretty_text = text
        pretty = (pretty_text)

        with open(category + '_' + os.path.basename(link), 'w') as fout:
            fout.write(pretty)

doc_files = os.listdir()
os.chdir('..')
patchfiles = os.listdir('patches')
shutil.copytree(apidocs + '_orig', apidocs)
os.chdir(apidocs)

for patchfile in patchfiles:
    try:
        sp = subprocess.check_output([
            'patch', '-p1', patchfile,
            os.path.join('..', 'patches', patchfile)])
    except subprocess.CalledProcessError as e:
        print('Failed to patch {}. Exit {}\n'.format(patchfile, e.returncode))
        print('Output was:\n')
        print(e.output.decode())

def code_pre_docanchor(tag):
    class_ = tag.attrs.get('class', ())
    return (tag.name == 'code' or tag.name == 'pre' or
            (tag.name == 'a' and 'doc-anchor-link' in class_))

api_items = {}
duplicate_api_items = {}
for doc_file in doc_files:
    if '.orig' in doc_file or doc_file in skipfiles:
        continue

    with open(doc_file) as doc:
        soup = BeautifulSoup(doc, "html.parser")

    for tag in soup.find_all(code_pre_docanchor):
        if tag.name == 'a':
            last_doc_anchor = tag['href']
            continue

        text = tag.get_text()
        # if re.search(
        #    r'<code>(OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT) .*\.json'
        # , line):
        #    line = re.sub(r'(<p>|<code>|</p>|</code>|/api/v2)', '', line)
        #    line = re.sub('&#123;', '{', line)
        #    line = re.sub('&#125;', '}', line)
        #    print(line, end='')
        match = re.match(
            r'\s*(OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT) (.*)', text)
        if match:
            cat = os.path.basename(doc_file.split('_')[0])
            page = doc_file.replace(cat + '_', '')
            docpage = zen_url + os.path.dirname(docpages[cat]) + '/' + page

            is_singular = False
            api_item = {}
            api_item['docpage'] = docpage + last_doc_anchor
            api_item['path_params'] = []
            api_item['opt_path_params'] = []
            api_item['opt_path'] = ''
            api_item['query_params'] = []
            api_item['opt_query_params'] = []

            api_item['method'] = match.group(1)
            path = match.group(2)

            # parse into a url object for easily accessing the parts of the url
            url = urllib.parse.urlsplit(path)

            api_item['path'] = url.path

            # Split the path and remove the first (always empty) item and
            # /api/v2
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
            has_action = True in [
                action in expanded_parts for action in api_actions]

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

            api_item['path_params'].reverse()
            api_item['query_params'].reverse()

            if name in api_items:
                if name not in duplicate_api_items:
                    duplicate_api_items[name] = []
                duplicate_api_items[name].append(api_item)
                continue

            api_items[name] = api_item

            continue

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
            False not in [i == j for i, j in itertools.zip_longest(
                dupe['path_params'], item['path_params'])] and
            False not in [i == j for i, j in itertools.zip_longest(
                sorted(dupe['query_params']), sorted(item['query_params']))]
        ):
            # Everything is the same, so discard this duplicate
            content += \
                "    # Duplicate API endpoint discarded:\n"\
                "    # {} from\n"\
                "    # {}\n\n".format(
                    name, dupe['docpage'])
        elif (
            dupe['method'] == item['method'] and
            False not in [i == j for i, j in itertools.zip_longest(
                sorted(dupe['query_params']), sorted(item['query_params']))]):
            # Only the path parameters differ, so we have optional or ambiguous
            # arguments

            # Common parameters are all required
            required = set(dupe['path_params']) & set(item['path_params'])

            # Optional parameters are only in one endpoint
            optional = list((
                set(dupe['path_params']) | set(item['path_params'])) -
                required)

            if (len(set(item['path_params']) - required) == 0 and
                    len(optional) > 0):
                # The item is the base function and the dupe has the optional
                # arguments. Just need to add the optional arguments
                item['opt_path_params'] = optional
                item['opt_path'] = dupe['path']
            elif (len(set(dupe['path_params']) - required) == 0 and
                    len(optional) > 0):
                # The dupe is the base function and the item has the
                # optional arguments
                # Need to swap the dupe with the item and then add the
                # optional arguments
                dupe_path = dupe['path']
                item = dupe
                item['opt_path_params'] = optional
                item['opt_path'] = dupe_path
            else:
                # this is ambiguous. If the parameters are in the same place,
                # then they're actually interchangeable, and we just need a
                # better name for them.
                handled = True
                new_path = ''
                new_path_params = []

                # compare each of the path parts to see specifically what is
                # different.
                for i, j in itertools.zip_longest(
                        item['path'].split('/'), dupe['path'].split('/')):
                    if i == j:
                        # everything is the same up to here. keep building a
                        # new, common path.
                        if i:
                            new_path += '/' + i
                    else:
                        # the paths are different. look at how they are
                        # different.
                        ipart, iext = os.path.splitext(i)
                        jpart, jext = os.path.splitext(j)
                        if ipart == jpart and iext != jext:
                            # These are legit dupes that only differ by
                            # the extension at the end.
                            content += \
                                "    # Duplicate API endpoint differs "\
                                "only by extension:\n"\
                                "    # {} from\n"\
                                "    # {}\n\n".format(
                                    name, dupe['docpage'])
                            handled = True
                            break

                        if (ipart.startswith('{') and jpart.startswith('{') and
                                iext != jext):
                            # The parameters are different, but in the same
                            # place and have a different extension. So this
                            # actually needs a new method.
                            # e.g. /thing/{id} vs /thing/{name}.json
                            new_name = name + '_by_' + jpart.strip('{}')
                            if new_name not in api_items:
                                api_items[new_name] = dupe
                                handled = True
                                break

                        if (ipart.startswith('{') and jpart.startswith('{') and
                                iext == jext):
                            # The parameters are in the same place and have the
                            # same extension. Combine these parameters as they
                            # are basically interchangeable.
                            # e.g. /thing/{id} vs /thing/{name} becomes
                            #      /thing/{id_or_name}
                            new_param = i.strip('{}' + iext) \
                                + '_or_' + j.strip('{}' + jext)
                            new_path_params.append(new_param)
                            new_path += '/{' + new_param + '}' + iext
                            item['path'] = new_path
                            item['path_params'] = new_path_params
                            handled = True
                            break

                if not handled:
                    content += \
                        "    # Duplicate ambiguous API endpoint:\n"\
                        "    # {} from\n"\
                        "    # {}\n\n".format(name, dupe['docpage'])
        elif (
            dupe['path'] == item['path'] and
            dupe['method'] == item['method'] and
            False not in [i == j for i, j in itertools.zip_longest(
                dupe['path_params'], item['path_params'])]):
                # Only the query parameters differ, so we have
                # optional named arguments
                item['opt_query_params'] = list(
                    set(item['query_params'].copy() +
                        item['opt_query_params'] +
                        dupe['query_params']))
                item['query_params'] = []
        elif (
            dupe['path'] == item['path'] and
            False not in [i == j for i, j in itertools.zip_longest(
                dupe['path_params'], item['path_params'])] and
            False not in [i == j for i, j in itertools.zip_longest(
                sorted(dupe['query_params']), sorted(item['query_params']))]):
                # Only the method differs, so indicate that method is ambiguous
                item['method'] = None
        else:
            should_keep += "\n"
            should_keep += \
                "    # Duplicate API endpoint that differs:\n"\
                "    #  {} from\n"\
                "    #  {}\n".format(name, dupe['docpage'])
            should_keep += \
                "    # Original definition located here:\n"\
                "    #  {} from\n"\
                "    #  {}\n".format(name, item['docpage'])
            should_keep += '    # {}\n'.format(name)
            should_keep += '    #    Path: {}\n'.format(dupe['path'])
            should_keep += '    #    Method: {}\n'.format(dupe['method'])
            should_keep += '    #    Parameters:\n'
            for param in dupe['path_params']:
                should_keep += '    #        {}\n'.format(param)
            should_keep += '    #    Query Parameters:\n'
            for param in dupe['query_params']:
                should_keep += '    #        {}\n'.format(param)
            should_keep += '    # Original definition:\n'
            should_keep += '    #    Path: {}\n'.format(item['path'])
            should_keep += '    #    Method: {}\n'.format(item['method'])
            should_keep += '    #    Parameters:\n'
            for param in item['path_params']:
                should_keep += '    #        {}\n'.format(param)
            should_keep += '    #    Query Parameters:\n'
            for param in item['query_params']:
                should_keep += '    #        {}\n'.format(param)
            should_keep += "\n"

if should_keep:
    content += should_keep

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

    if item['method']:
        if item['method'] in ['POST', 'PUT']:
            if argspec:
                argspec += ', '
            argspec += 'data'
    else:
        if argspec:
            argspec = 'method, ' + argspec + ', data=None'
        else:
            argspec = 'method, data=None'

    if item['opt_path_params']:
        if argspec:
            argspec += ', '
        argspec += '=None, '.join(item['opt_path_params']) + '=None'

    if item['opt_query_params']:
        if argspec:
            argspec += ', '
        argspec += '=None, '.join(
            [sanitize(q) for q in item['opt_query_params']]) + '=None'

    if argspec:
        argspec += ', '
    argspec += '**kwargs'

    content += '    def {}(self, {}):\n'.format(name, argspec)
    content += '        "{}"\n'.format(item['docpage'])
    content += '        api_path = "{}"\n'.format(item['path'])

    if item['path_params']:
        content += '        api_path = api_path.format({})\n'.format(
            path_fmt_args)

    if item['opt_path']:
        opt_test = ' and '.join(item['opt_path_params'])
        if path_fmt_args:
            path_fmt_args += ', '
        path_fmt_args = path_fmt_args + \
            ', '.join([p + '=' + p for p in item['opt_path_params']])
        content += '        if {}:\n'.format(opt_test)
        content += '            api_opt_path = "{}"\n'.format(item['opt_path'])
        content += '            api_path = api_opt_path.format({})\n'.format(
            path_fmt_args)

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
    # if item['opt_query_params']:
    #    opt_test = ' or '.join(
    #       [sanitize(q) for q in item['opt_query_params']])
    #    content += '        if not ({}):\n'.format(opt_test)
    #    content += '            pass\n'

    content += '        return self.call(api_path'

    if item['query_params'] or item['opt_query_params']:
        content += ', query=api_query'

    if item['method']:
        if item['method'] != 'GET':
            content += ', method="{}"'.format(item['method'])

        if item['method'] in ['POST', 'PUT']:
            content += ', data=data'
    else:
        content += ', method=method, data=data'

    content += ', **kwargs)\n\n'

os.chdir('..')

with open('zdesk_api.py', 'w') as f:
    f.write(template.format(content))
