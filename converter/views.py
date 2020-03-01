from airtable import Airtable
from django.shortcuts import render
from converter.config import base_key, api_key


def init(request):
    airtable = Airtable(base_key, 'Table 1', api_key)
    print(airtable.get_all())
    return render(request, 'diploma.html')
