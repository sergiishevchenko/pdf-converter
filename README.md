[![Build Status](https://travis-ci.org/sergiishevchenko/pdf-converter.svg?branch=master)](https://travis-ci.org/sergiishevchenko/pdf-converter)
[![Requirements Status](https://requires.io/github/sergiishevchenko/pdf-converter/requirements.svg?branch=master)](https://requires.io/github/sergiishevchenko/pdf-converter/requirements/?branch=master)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-374/)
[![Coverage Status](https://coveralls.io/repos/github/sergiishevchenko/pdf-converter/badge.svg)](https://coveralls.io/github/sergiishevchenko/pdf-converter)
# PDF-Converter

## How to start?
Your first commands would be:
```
git clone <SSH address of this repo>
cd pdf-converter/
python3 -m myenv venv
source venv\bin\activate
pip install -r requirements.txt
```
## Project description
### 1. Airtable
#### Installation
```
pip install airtable-python-wrapper
```
#### Airtable Class Instance

Authentication is handled by the Airtable class. 
The class can handle authentication automatically if the environment variable AIRTABLE_API_KEY is set with your api key.
```
>>> airtable = Airtable('base_key', 'table_name')
>>> airtable.get_all()
[{id:'rec123asa23', fields': {'Column': 'Value'}, ...}]
```
Alternatively, you can pass the key explicitly:
```
>>> airtable = Airtable(base_key, table_name, api_key='yourapikey')
```
You can also use this class to handle authentication for you if you are making your own wrapper:
```
>>> auth = AirtableAuth(api_key)
>>> response = requests.get('https://api.airtable.com/v0/{basekey}/{table_name}', auth=auth)
```
### 2. Creation template of diploma by HTML + SASS + CSS.
### 3. PDFKIT
It's wkhtmltopdf python wrapper to convert html to pdf using the webkit rendering engine and qt.
#### Install python-pdfkit
```
$ pip install pdfkit
```
#### Install wkhtmltopdf:
```
pip install wkhtmltopdf
```
#### Usage
For simple tasks:
```
import pdfkit

pdfkit.from_url('http://google.com', 'out.pdf')
pdfkit.from_file('test.html', 'out.pdf')
pdfkit.from_string('Hello!', 'out.pdf')
```
You can pass a list with multiple URLs or files:
```
pdfkit.from_url(['google.com', 'yandex.ru', 'engadget.com'], 'out.pdf')
pdfkit.from_file(['file1.html', 'file2.html'], 'out.pdf')
```
If you wish to further process generated PDF, you can read it to a variable:
```
# Use False instead of output path to save pdf to a variable
pdf = pdfkit.from_url('http://google.com', False)
```
You can specify all wkhtmltopdf options.
```
options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ]
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None
}

pdfkit.from_url('http://google.com', 'out.pdf', options=options)
```
#### Configuration
Each API call takes an optional configuration paramater. This should be an instance of pdfkit.configuration() API call. It takes the configuration options as initial paramaters. The available options are:

wkhtmltopdf - the location of the wkhtmltopdf binary. By default pdfkit will attempt to locate this using which (on UNIX type systems) or where (on Windows).
meta_tag_prefix - the prefix for pdfkit specific meta tags - by default this is pdfkit-
Example - for when wkhtmltopdf is not on $PATH:
```
config = pdfkit.configuration(wkhtmltopdf='/opt/bin/wkhtmltopdf')
pdfkit.from_string(html_string, output_file, configuration=config)
```