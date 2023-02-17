from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_session import Session
from Classes.Classes import Session_OLX, OLX_listing
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
app.config['SECRET_KEY'] = 'your secret key'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "sqlalchemy"

# unknown problem with relative path, will test on linux
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///C:\\Users\\pnowak\\PycharmProjects\\WingScrapper\\search.db'
Session(app)
db = SQLAlchemy(app)




if __name__ == "__main__":
    app.run(debug=True)
    # with app.app_context():
    #     db.create_all()
    #     db.session.commit()
    #     # db.drop_all()
    #     first = Search(name='wing', link='test')
    #     second = Search(name='foil', link='test2')
    #     db.session.add(first)
    #     # db.session.add(second)
    #     # db.session.commit()
    #     query = Search.query.all()
    #     print(query)
    # db.session.add(first)
    # db.session.add(second)
    # db.session.commit()
    # query = Search.query.all()

