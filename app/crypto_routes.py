from flask import Blueprint, render_template

crypto = Blueprint("crypto", __name__, url_prefix="/crypto")

@crypto.route("/")
def crypto_home():
    return render_template("crypto/crypto_home.html")

@crypto.route("/portfolio-dashboard")
def crypto_dashboard():
    return render_template("crypto/crypto_dashboard.html")