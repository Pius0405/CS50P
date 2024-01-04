import requests

import sys

if len(sys.argv) == 1:
    sys.exit('Missing command-line argument')
else:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit('Command-line argument is not a number')

try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = response.json()
except requests.RequestException:
    sys.exit()

rate = response['bpi']['USD']['rate_float']
amount = rate*n
print(f'${amount:,.4f}')


