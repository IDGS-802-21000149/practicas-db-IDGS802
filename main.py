from flask import Flask,request,render_template,Response
from flask import flash
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
import forms
from models import Alumnos
from models import Profesores
from models import db

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

@app.route("/index",methods=["GET","POST"])
def index():
   alum_form=forms.UserForm2(request.form)
   if request.method == "POST" :
      alum=Alumnos(nombre=alum_form.nombre.data,
                  apaterno=alum_form.apaterno.data,
                  email=alum_form.email.data)
      #INSERT INTO alumnos VALUES()
      db.session.add(alum)
      db.session.commit()
   return render_template("index.html",form=alum_form)

@app.route("/profesores",methods=["GET","POST"])
def profesores():
   profe=forms.Profe(request.form)
   if request.method == "POST" :
      prof=Profesores(nombre=profe.nombre.data,
                  apaterno=profe.apaterno.data,
                  amaterno=profe.amaterno.data,
                  grupo=profe.grupo.data,
                  email=profe.email.data)
      #INSERT INTO alumnos VALUES()
      db.session.add(prof)
      db.session.commit()
   return render_template("profesores.html",form=profe)

@app.route("/ABC_Completo",methods=["GET","POST"])
def ABCompleto():
   alum_form=forms.UserForm2(request.form)
   alumno=Alumnos.query.all()

   return render_template("ABC_Completo.html",alumno=alumno)

@app.route("/ABC_Profesor",methods=["GET","POST"])
def ABCompletoProf():
   profesor=forms.Profe(request.form)
   profesor=Profesores.query.all()  
   return render_template("ABC_Profesor.html",profesor=profesor)

@app.errorhandler(404)
def page_not_found(e):
 return render_template("404.html"),404




@app.route("/alumnos",methods=["GET","POST"])
def alumnos():

   nom=""
   apa =""
   ama=""
   correo=""
   edad=""
   alumnos_form=forms.UserForm(request.form)
   if request.method == "POST" and alumnos_form.validate():
      nom = alumnos_form.nombre.data
      apa = alumnos_form.apaterno.data
      ama = alumnos_form.amaterno.data
      correo = alumnos_form.correo.data
      mensaje="Bienvenido:{}".format(nom)
      flash(mensaje)
      print("nombre: {}".format(nom))
      print("apaterno: {}".format(apa))
      print("amaterno: {}".format(ama))
      print("correo: {}".format(correo))
      print("correo: {}".format(edad))

   return render_template("alumnos.html",form=alumnos_form,nom=nom,ama=ama,apa=apa,correo=correo,edad=edad)

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    app.run()
