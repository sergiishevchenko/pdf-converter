from airtable import airtable

at = airtable.Airtable('BASE_ID', 'API_KEY')
at.get('TABLE_NAME')
