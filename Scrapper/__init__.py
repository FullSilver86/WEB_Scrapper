from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_session import Session
from Classes.Classes import Session_OLX, OLX_listing
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'

# unknown problem with relative path, will test on linux
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///C:\\Users\\pnowak\\PycharmProjects\\WingScrapper\\Scrapper\\search.db'
# Session(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from Scrapper import models, routes