from flask import Blueprint, render_template, jsonify
import requests

crypto = Blueprint("crypto", __name__, url_prefix="/crypto")

@crypto.route("/")
def crypto_home():
    return render_template("crypto/crypto_home.html")

@crypto.route("/portfolio-dashboard")
def crypto_dashboard():
    return render_template("crypto/crypto_dashboard.html")

@crypto.route("/ticker-prices")
def ticker_prices():
    coin_ids = "bitcoin,ethereum,avalanche-2"
    vs_currency = "usd"
    api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_ids}&vs_currencies={vs_currency}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        prices = response.json()
    except Exception as e:
        print(f"Error {e}")
        prices = {}

    return jsonify(prices)