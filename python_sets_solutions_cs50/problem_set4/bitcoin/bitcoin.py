import sys
import requests

if (len(sys.argv)) == 1:
    sys.exit("Missing command-line argument")
else:
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        try:
             response = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=41f30d344b8fbcf5ae344c07d1da5230bffa25c3eefa4fea9ad82bc25efab5b0')
             response.raise_for_status()
        except requests.RequestException:
             sys.exit("An error occurred")
        print(f"${(amount*float(response.json()['data']['priceUsd'])):,.4f}")
