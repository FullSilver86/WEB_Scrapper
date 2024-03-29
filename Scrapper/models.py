from Scrapper import db, login_manager, bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(), nullable=False)
    search = db.relationship('Search', backref='owned_user', lazy=True)

    def __repr__(self):
        return f'name = {self.username}, search is = {self.search}, password hash is {self.password_hash}'

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=40))
    link = db.Column(db.String(length=512), nullable=False )
    current_offer = db.Column(db.Text())
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    new_offers_list = db.Column(db.Text())

    def __repr__(self):
        return f'name = {self.name}, link is = {self.link} and owner is {self.owner}'