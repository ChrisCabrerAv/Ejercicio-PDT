from logica import Carrera,Postulante
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] ="Clave super bacan que nadie nunca detectara jajaxdxdxddddd"

class Formulario(FlaskForm):
    nem = IntegerField(label="NEM",validators=[DataRequired("Es necesario ingresar el NEM")])
    ranking = IntegerField(label="Ranking",validators=[DataRequired("Es necesario ingresar el Ranking")])
    lenguaje = IntegerField(label="Puntaje prueba Lenguaje",validators=[DataRequired("Lenguaje y Matemáticas son pruebas obligatorias")])
    matematica = IntegerField(label="Puntaje prueba Matemáticas",validators=[DataRequired("Lenguaje y Matemáticas son pruebas obligatorias")])
    ciencia = IntegerField(label="Ciencas")
    historia = IntegerField(label="Historia")
    submit = SubmitField(label="Enviar")

@app.route("/",methods=['post'])
def principal():
    formulario = Formulario()
    if formulario.validate_on_submit():
        nem = int(formulario.nem)
        ranking = int(formulario.ranking)
        lenguaje = int(formulario.lenguaje)
        matematica = int(formulario.matematica)
        ciencia = int(formulario.ciencia)
        historia = int(formulario.historia)
        p1 = Postulante(lenguaje,matematica,ciencia,historia,nem,ranking)
        return redirect(url_for("carreras",postulante = p1))
    return render_template("index.html",formulario = formulario)

@app.route("/carreras")
def carreras(postulante:Postulante):
    return render_template("carreras.html")

if __name__=="__main__":
    app.run(debug=True)