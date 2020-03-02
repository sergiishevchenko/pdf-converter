from airtable import Airtable
from django.shortcuts import render
from converter.config import base_key, api_key
import pdfkit


def init(request):
    airtable = Airtable(base_key, 'Table 1', api_key)
    for script in airtable.get_all():
        name = script['fields']['Имя']
        surname = script['fields']['Фамилия']
        date = script['fields']['Дата']
        # config = pdfkit.configuration(wkhtmltopdf="/Users/serg/Desktop/projects/pdf-converter/myenv/lib/python3.7/site-packages/pdfkit/configuration.py")
        pdfkit.from_file('converter/templates/diploma.html', 'out.pdf')
        params = {
            'name': name,
            'surname': surname,
            'date': date}
        return render(request, 'diploma.html', params)
