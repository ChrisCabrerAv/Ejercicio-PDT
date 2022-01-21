from logica import Carrera,Postulante
from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import IntegerField,SubmitField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)

app.config["SECRET_KEY"] ="Clave super bacan que nadie nunca detectara jajaxdxdxddddd"

class Formulario(FlaskForm):
    nem = IntegerField(label="NEM",validators=[DataRequired("Es necesario ingresar el NEM"),NumberRange(120,850,"El puntaje debe ser un número entre 120 y 850")])
    ranking = IntegerField(label="Ranking",validators=[DataRequired("Es necesario ingresar el Ranking"),NumberRange(120,850,"El puntaje debe ser un número entre 120 y 850")])
    lenguaje = IntegerField(label="Puntaje prueba Lenguaje",validators=[DataRequired("Lenguaje y Matemáticas son pruebas obligatorias"),NumberRange(120,850,"El puntaje debe ser un número entre 120 y 850")])
    matematica = IntegerField(label="Puntaje prueba Matemáticas",validators=[DataRequired("Lenguaje y Matemáticas son pruebas obligatorias"),NumberRange(120,850,"El puntaje debe ser un número entre 120 y 850")])
    ciencia = IntegerField(label="Ciencas",validators=[NumberRange(0,850,"El puntaje debe ser un número entre 120 y 850")])
    historia = IntegerField(label="Historia",validators=[NumberRange(0,850,"El puntaje debe ser un número entre 120 y 850")])
    submit = SubmitField(label="Enviar")

datos = [
    Carrera('Medicina',10,25,15,0,755.15,25,25),
    Carrera('Ingeniería Civil Informática',10,20,20,0,580,25,25),
    Carrera('Derecho',25,10,0,15,600,25,25),
    Carrera('Odontología',10,25,15,0,700.7,25,25),
    Carrera('Kinesiología',10,25,15,0,590.85,25,25)
]

@app.route("/",methods=['get','post'])
def principal():
    formulario = Formulario()
    if formulario.validate_on_submit():
        session['nem'] = formulario.nem.data
        session['ranking'] = formulario.ranking.data
        session['lenguaje'] = formulario.lenguaje.data
        session['matematica'] = formulario.matematica.data
        session['ciencia'] = formulario.ciencia.data
        session['historia'] = formulario.historia.data
        return redirect(url_for("carreras"))
    return render_template("index.html", formulario=formulario)

@app.route("/carreras")
def carreras():
    resultados = []
    for i in datos:
        resultados.append(i.calcular(Postulante(int(session['lenguaje']),int(session['matematica']),int(session['ciencia']),int(session['historia']),int(session['nem']),int(session['ranking']))))
    return render_template("carreras.html", datos = datos, resultados = resultados, range=range(0,len(datos)))

if __name__=="__main__":
    app.run(debug=True)