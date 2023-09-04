from app import db
from datetime import datetime

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Coulmn(db.String(50))
    email=db.Column(db.String(40),unique=True)
    date_joined= db.Column(db.date,default=datetime.utcnow())