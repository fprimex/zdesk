#!/usr/bin/env python3

import os

from bs4 import BeautifulSoup

# mostly lifted from
# http://stackoverflow.com/questions/13014862/parse-each-file-in-a-directory-with-beautifulsoup-python-save-out-as-new-file

def clean_dir(directory):

    for filename in os.listdir(directory):
        clean_file(os.path.join(directory, filename))

def clean_file(filename):

    #tag_black_list = ['iframe', 'script']
    #tag_white_list = ['p','div']
    #attr_white_list = {'*': ['title']}

    with open(filename, 'r') as fhandle:
        text = BeautifulSoup(fhandle)

        # Step one, with BeautifulSoup: Remove tags in tag_black_list, destroy contents.
        #[s.decompose() for s in text(tag_black_list)]
        pretty_text = text.prettify()
        if not pretty_text:
            # In the case of prettify killing the whole page
            pretty_text = text
        pretty = (pretty_text)

        # Step two, with Bleach: Remove tags and attributes not in whitelists, leave tag contents.
        #cleaned = bleach.clean(pretty, strip="TRUE", attributes=attr_white_list, tags=tag_white_list)

        # this appends -cleaned to the file; 
        # relies on the file having a '.'
        #dot_pos = filename.rfind('.')
        #cleaned_filename = '{0}-cleaned{1}'.format(filename[:dot_pos], filename[dot_pos:])

    with open(filename, 'w') as fout:
        #fout.write(cleaned.encode("utf-8"))
        fout.write(pretty)

if __name__ == '__main__':
    clean_dir(os.path.join('developer.zendesk.com', 'rest_api',
                           'docs', 'core'))
    clean_dir(os.path.join('developer.zendesk.com', 'rest_api',
                           'docs', 'help_center'))

