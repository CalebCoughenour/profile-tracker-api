from flask import Blueprint, render_template

stocks = Blueprint("stocks", __name__, url_prefix="/stocks")

@stocks.route("/")
def stocks_home():
    return render_template("stocks/stocks_home.html")

@stocks.route("/stocks-dashboard")
def stocks_dashboard():
    return render_template("stocks/stocks_dashboard.html")