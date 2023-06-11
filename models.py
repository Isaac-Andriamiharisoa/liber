from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://isaac:BELOHA03@localhost:5432/liber'

class Ame(db.Model):
    __tablename__ = 'ames'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String)
    prenom = db.Column(db.String)
    bapteme = db.Column(db.Boolean)
    motdepasse = db.Column(db.String)
    communion = db.Column(db.Boolean)
    fanavaozana = db.Column(db.Boolean)
    confirmation = db.Column(db.Boolean)
    mariage = db.Column(db.Boolean)
    mort = db.Column(db.Boolean)
    contribution = db.Column(db.Integer, default=0)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()