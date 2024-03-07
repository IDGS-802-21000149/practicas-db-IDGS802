from calendar import monthrange
from datetime import datetime,timedelta
from flask import Flask,request,render_template,Response,redirect,url_for
from flask import flash
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
import forms
from models import Alumnos
from models import Profesores,Pizzas
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



temporal = []
id_pizza = 1

@app.route("/pizza", methods=["GET", "POST"])
def pizzas():
    global temporal, id_pizza, temporalbd
    pizza_form = forms.PizzaForm(request.form)
    
    ventas = None 
    suma_total = None 
    
    if request.method == "POST" and "fecha_consulta" not in request.form:
        ingredientes_seleccionados = []

        if pizza_form.jamon.data:
            ingredientes_seleccionados.append("Jamon")
        if pizza_form.pinia.data:
            ingredientes_seleccionados.append("Pinia")
        if pizza_form.champiniones.data:
            ingredientes_seleccionados.append("Champiniones")

        tamanio_seleccionado = pizza_form.tamanio.data
        if tamanio_seleccionado == 'Chica':
            tamanio_int = 40
        elif tamanio_seleccionado == 'Mediana':
            tamanio_int = 80
        else:
            tamanio_int = 120

        num_ingredientes = len(ingredientes_seleccionados) * 10
        total = int(num_ingredientes) + tamanio_int
        totalP = total * pizza_form.numero.data
        
        temporal.append({ 
            'id': id_pizza,
            'nombre': pizza_form.nombre.data,
            'direccion': pizza_form.direccion.data,
            'telefono': pizza_form.telefono.data,
            'tamanio': tamanio_seleccionado,
            'ingredientes': ingredientes_seleccionados,
            'numero': pizza_form.numero.data,
            'totalP': totalP
        })
        id_pizza += 1
    
    # Consultar ventas solo si se ha enviado el formulario de fecha de consulta
    if request.method == "POST" or request.method == "GET":
        fecha_consulta_str = request.form.get("fecha_consulta")
        if fecha_consulta_str:
            fecha_consulta = datetime.strptime(fecha_consulta_str, "%Y-%m-%d").date()
            
            # Consultar las ventas realizadas en la fecha seleccionada
            ventas = Pizzas.query.filter(Pizzas.create_date >= fecha_consulta).filter(Pizzas.create_date < fecha_consulta + timedelta(days=1)).all()
            suma_total = sum(venta.total for venta in ventas)

    
    return render_template("pizza.html", form=pizza_form, temporal=temporal, ventas=ventas,suma_total=suma_total)



@app.route("/confirmar", methods=["POST"])
def confirmar_registro():
    global temporal

    for registro in temporal:
        pizza = Pizzas(
            nombre=registro['nombre'],
            direccion=registro['direccion'],
            telefono=registro['telefono'],
            tamanio=registro['tamanio'],
            ingredientes=', '.join(registro['ingredientes']),  
            numero=registro['numero'],
            total=registro['totalP']
        )
        db.session.add(pizza)

    db.session.commit()
    temporal = [] 

    return redirect("/pizza")  

 
@app.route("/eliminarPizza", methods=["POST"])
def eliminar_registro():
    global temporal
    id_pizza = int(request.form["id"])
    temporal = [registro for registro in temporal if registro["id"] != id_pizza]
    return redirect("/pizza")

 
@app.route("/ABC_Completo",methods=["GET","POST"])
def ABCompleto():
   alum_form=forms.UserForm2(request.form)
   alumno=Alumnos.query.all()

   return render_template("ABC_Completo.html",alumno=alumno)

@app.route("/ABC_Profesor",methods=["GET","POST"])
def ABCompletoProf():
   profesor_form=forms.Profe(request.form)
   profesor=Profesores.query.all()  
   return render_template("ABC_Profesor.html",profesor=profesor)

@app.route("/eliminar",methods=["GET","POST"])
def eliminar():
   profesor_form=forms.Profe(request.form)
   if request.method == "GET" :
      id=request.args.get('id')
      profe1=db.session.query(Profesores).filter(Profesores.id==id).first()
      profesor_form.id.data=request.args.get('id')
      profesor_form.nombre.data=profe1.nombre
      profesor_form.apaterno.data=profe1.apaterno
      profesor_form.amaterno.data=profe1.amaterno
      profesor_form.grupo.data=profe1.grupo
      profesor_form.email.data=profe1.email
   if request.method=="POST":
      id=profesor_form.id.data
      pro=Profesores.query.get(id)
      db.session.delete(pro)
      db.session.commit()
      return redirect(url_for('ABCompletoProf'))
   return render_template('eliminar.html',form=profesor_form)


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
