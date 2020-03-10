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
## Step-by-step project description
### 1 Airtable
Installation
```
pip install airtable-python-wrapper
```
Airtable Class Instance

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
