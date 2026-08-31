import sys
import requests


def main():
    n = get_bitcoins()
    try:
        request = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=00001ff176dfa1db3340d59a8eeb085d57b59d4a1cf82d56bbfa9e65298f2ba0"
        )
        data = request.json()
        price = data["data"]
        float_price = float(price["priceUsd"]) * n
        print(f"${float_price:,.4f}")
    except requests.RequestException:
        sys.exit("Kaboom")


def get_bitcoins():
    if len(sys.argv) != 2:
        sys.exit("Invalid # of command-line arguments")
    try:
        return float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")


main()
