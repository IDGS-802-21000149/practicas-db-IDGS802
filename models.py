from flask_sqlalchemy import SQLAlchemy
import datetime

db=SQLAlchemy()

class Alumnos(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    apaterno=db.Column(db.String(50))
    email =db.Column(db.String(50))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)

class Profesores(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    apaterno=db.Column(db.String(50))
    amaterno=db.Column(db.String(50))
    email =db.Column(db.String(50))
    grupo =db.Column(db.String(50))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)
    
class Pizzas(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    direccion=db.Column(db.String(50))
    telefono=db.Column(db.String(50))
    tamanio=db.Column(db.String(50))
    ingredientes =db.Column(db.String(50))
    numero =db.Column(db.Integer)
    total =db.Column(db.Integer)
    fecha=db.Column(db.DateTime)
    dia=db.Column(db.String(50))

    
