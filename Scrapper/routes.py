from Scrapper import app, db
from flask import render_template, request, url_for, flash, redirect, session
from Scrapper.models import Search, User
from Scrapper.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user
from Classes.Classes import Session_OLX, OLX_listing



# Created for testing purposes, later converted to proper test
@app.route('/create')
def create():
    db.drop_all()
    db.create_all()
    search1 = Search(name='wing', link='test', owner='1')
    search2 = Search(name='foil', link='test2')
    user1 = User(username='Bot', email_address='something@wp.pl', password_hash='AFHFADSJ')
    db.session.add(search1)
    db.session.add(search2)
    db.session.add(user1)
    db.session.commit()
    query = Search.query.all()
    query2 = User.query.all()
    print(query)
    print(query2)
    return redirect("/")

@app.route('/', methods=["GET", "POST"])
@login_required
def search():

    if request.method == 'POST':
        product = request.form['product']

        if not product:
            flash('Product is required !')
        else:
            new_search = Search(name=product,
                                link=url_for('product_list',product=product),
                                current_offer=str(Session_OLX(product).listing),
                                owner=current_user.id)
            db.session.add(new_search)
            db.session.commit()
            ident = new_search.id
            return redirect(url_for('product_list', product=product))


    return render_template("search.html")

@app.route('/product_list/<product>', methods=["GET"])
@login_required
def product_list(product, new_offers_list=[]):
    search = Search.query.filter_by(name=product).first()
    listing = search.current_offer
    new_offer = Session_OLX(product).listing
    for new_link in new_offer:
        if new_link not in listing:
            if new_link not in new_offers_list:
                new_offers_list.append(new_link)
    return render_template("product_list.html", product=product, new_offers_list=new_offers_list)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('search'))
        else:
            flash(f'Username and password are not match! Please try again', category='danger')
    return render_template("login.html", form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("login"))


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('search'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template("register.html", form=form)