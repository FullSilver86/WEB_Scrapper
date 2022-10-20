from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_session import Session
from Classes.Classes import Session_OLX, OLX_listing
import os

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
app.config['SECRET_KEY'] = 'your secret key'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/', methods=["GET", "POST"])
def search():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == 'POST':
            product = request.form['product']

            if not product:
                flash('Product is required !')
            else:
                session['current_offer']= Session_OLX(product).listing
                return redirect(url_for('product_list', product=product))


    return render_template("search.html")

@app.route('/product_list/<product>', methods=["GET"])
def product_list(product):
    listing = session['current_offer']
    current_offer = Session_OLX(product).listing
    new_offers = [new_link for new_link in set(current_offer) if new_link not in listing]

    return render_template("product_list.html", product=product, new_offers=new_offers)


@app.route("/login", methods=["POST", "GET"])
def login():
    # if form is submited
    if request.method == "POST":
        # record the user name
        session["name"] = request.form.get("name")
        # redirect to the main page
        return redirect("/")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

