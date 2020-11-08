""" 
Database models are listed here 
"""
from libs.shared import db

class User(db.Model):
    __tablename__ = "users" 
    id = db.Column("Id", db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column("FirstName", db.String(100), nullable=False)
    last_name = db.Column("LastName", db.String(100), nullable=False)
    email = db.Column("Email", db.String(100), nullable=False)