from flask import Blueprint, render_template
from datetime import datetime

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("home.html", current_date=datetime.now().date())

@main.route("/crypto")
def crypto_dashboard():
    return render_template("crypto_dashboard.html", current_date=datetime.now().date())

@main.route("/stocks")
def stock_dashboard():
    return render_template("stock_dashboard.html", current_date=datetime.now().date())