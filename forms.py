from wtforms import Form
from wtforms import StringField,IntegerField,RadioField
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


class GuardarIdiomaForm(Form):
    espaniol = StringField("Español", validators=[validators.DataRequired(message="El campo es requerido")])
    ingles = StringField("Inglés", validators=[validators.DataRequired(message="El campo es requerido")])

class ConsultarIdiomaForm(Form):
    palabra = StringField("Palabra a buscar", validators=[validators.DataRequired(message="El campo es requerido")])
    idioma = RadioField("Idioma", choices=[("Espanol", "Español"), ("Ingles", "Inglés")])
