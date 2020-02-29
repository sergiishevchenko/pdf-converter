# from airtable import airtable
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

# at = airtable.Airtable('BASE_ID', 'API_KEY')
# at.get('TABLE_NAME')


def init(request):
    return render(request, 'diploma.html')
