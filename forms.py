from wtforms import Form
from wtforms import StringField,IntegerField,RadioField,BooleanField 
from wtforms import EmailField
from wtforms import validators



class UserForm(Form):
    nombre=StringField("nombre",[
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4,max=10,message="ingresa nombre vailido")
    ])
    apaterno=StringField("apaterno")
    amaterno=StringField("amaterno")
    edad=IntegerField("edad",[validators.number_range(min=1,max=20,message="Valor no valido")])
    correo=EmailField("correo",[validators.Email(message="Ingrese un correo valido")])
    
class UserForm2(Form):
    id=IntegerField('id')
    nombre=StringField("nombre",[
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4,max=10,message="ingresa nombre vailido")
    ])
    apaterno=StringField("apaterno")
    email=EmailField("correo",[validators.Email(message="Ingrese un correo valido")])

class Profe(Form):
    id=IntegerField('id')
    nombre=StringField("nombre",[
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4,max=10,message="ingresa nombre vailido")
    ])
    apaterno=StringField("apaterno")
    amaterno=StringField("amaterno")
    grupo=StringField("grupo")
    email=EmailField("email",[validators.Email(message="Ingrese un correo valido")])



class PizzaForm(Form):
    
      id=IntegerField('id')
      nombre=StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4,max=10,message="ingresa nombre vailido")
    ])
      direccion=StringField("Direccion",[
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4,max=10,message="ingresa nombre vailido")
    ])
      telefono=StringField("Telefono",[
        validators.DataRequired(message="El campo es requerido"),
    ])
      tamanio = RadioField("Tamanio", choices=[("Chica", "Chica $40"), 
                                              ("Mediana", "Mediana $80"),
                                              ("Grande","Grande $120")])
      jamon = BooleanField('Jamón $10')
      pinia = BooleanField('Piña $10')
      champiniones = BooleanField('Champiñones $10')
      
      numero=IntegerField("Numero",[
        validators.DataRequired(message="El campo es requerido"),
    ])
      
    
      