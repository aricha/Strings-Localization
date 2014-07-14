"""
Copyright (c) 2013 Andrew Richardson
(Adapted from Max Vilimpoc's gettext for Django)

Permission is hereby granted, free of charge, to any person obtaining 
a copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom 
the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR 
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
OR OTHER DEALINGS IN THE SOFTWARE.
"""

"""
Generates Cocoa Localizable.strings files from Localization Spreadsheet 
JSONify output.

Dumps the Localizable.strings files into the <locale>.lproj directory
in the same location as this script. Optionally, you may specify a path
argument to output the files into that directory instead.

So you'll want to put this file in the app directory that
you want to localize.

Then, specify the SHEET_ID and SHEET_NAME variables of your Google spreadsheet
below and call this script to do the generation.
"""

import codecs
import os
import sys
import requests
import textwrap

try:
    import markdown
except ImportError:
    print 'Markdown unavailable.'
    pass

ROOTDIR     = ''
FILEPATH    = '{}.lproj/'
FILENAME    = 'Localizable.strings'

EXEMPT_KEYS = ['language_code', 'language_name', 'text_direction']

SHEET_ID    = ''
SHEET_NAME  = 'Main'
SOURCE_URL  = 'https://script.google.com/macros/s/AKfycbxLnEUyElPtL01qHnL7pD2hmTmaO7Tc1yLhjJzQpitpuBfxxBU/exec?sheet%5fid=' + SHEET_ID + '&sheet%5fname=' + SHEET_NAME

def createPoFromDict(language_code='', string_table={}):
    if not language_code:
        raise ValueError('language_code is a required parameter')
    
    if not string_table:
        raise ValueError('string_table is a required parameter')

    output = []

    for k, v in sorted(string_table.iteritems()):
        # Apply Markdown if it's available.
        try:
            v = markdown.markdown(v)
        except:
            pass
        
        if any(k in s for s in EXEMPT_KEYS):
            continue

        b = textwrap.wrap(v, drop_whitespace=False)
        c = [u'{0}'.format(element) for element in b]
        d = u''.join(c)

        output.append((u'"{0}" = "{1}";\n\n'.format(k, d)))

    # Create locale directories.
    poPath = ROOTDIR + FILEPATH.format(language_code)
    if not os.path.isdir(poPath):
        os.makedirs(poPath)

    # Create Localizable.strings files.
    poName = poPath + FILENAME
    print u'Creating {0}'.format(poName)

    with codecs.open(poName, "wb", encoding='utf-8') as poFile:
        poFile.write(u''.join(output))
        poFile.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        ROOTDIR = sys.argv[1] + '/'

    if not SHEET_ID or not SHEET_NAME:
        sys.exit('Sheet ID or name not provided!')
    
    r = requests.get(SOURCE_URL)
    
    if r.ok:
        data = r.json()
        for k, v in sorted(data.iteritems()):
            createPoFromDict(language_code=k, string_table=v)

