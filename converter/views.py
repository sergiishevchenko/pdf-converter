from airtable import Airtable
from django.shortcuts import render
from converter.config import base_key, api_key
import pdfkit
from django.template.loader import get_template
from django.http import HttpResponse


def init(request):
    airtable = Airtable(base_key, 'Table 1', api_key)

    template = get_template('diploma.html')
    for script in airtable.get_all():
        name = script['fields']['Имя']
        surname = script['fields']['Фамилия']
        date = script['fields']['Дата']
        html = render(request, 'diploma.html', {'name': name, 'surname': surname, 'date': date})
        config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
        options = {
            'dpi': 300,
            'page-size': 'A4',
            'orientation': 'landscape',
            'margin-top': '0',
            'margin-right': '0.',
            'margin-bottom': '0.',
            'margin-left': '0',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'no-outline': None
        }
        pdfkit.from_file('converter/templates/diploma.html', 'out.pdf', configuration=config, options=options)
    return render(request, 'diploma.html')
