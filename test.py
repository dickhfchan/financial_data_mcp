import requests

# add your API key to the headers
headers = {
    "X-API-KEY": "dcd5c2dd-a15b-4d29-bc19-6f1bbc9ccc1c"
}

# set your query params
ticker = 'INTC'     # stock ticker
period = 'annual'      # possible values are 'annual', 'quarterly', or 'ttm'
limit = 4         # number of statements to return

# create the URL
url = (
    f'https://api.financialdatasets.ai/financials/income-statements/'
    f'?ticker={ticker}'
    f'&period={period}'
    f'&limit={limit}'
)

print(url)

# https://api.financialdatasets.ai/financials/income-statements/?ticker=INTC&period=annual&limit=4
# https://api.financialdatasets.ai/financials/income-statements?ticker=INTC&period=annual&limit=4

# make API request
response = requests.get(url, headers=headers)

# parse income_statements from the response
income_statements = response.json().get('income_statements')

print(income_statements)