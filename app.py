from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.secret_key="Clave super bacan que nadie nunca detectara jajaxdxdxddddd"

class Formulario(FlaskForm):
    nem = IntegerField(label="NEM",validators=[DataRequired("Es necesario ingresar el NEM")])
    ranking = IntegerField(label="Ranking",validators=[DataRequired("Es necesario ingresar el Ranking")])
    lenguaje = IntegerField(label="Puntaje prueba Lenguaje",validators=[DataRequired("Lenguaje y Matemáticas son pruebas obligatorias")])
    matematica = IntegerField(label="Puntaje prueba Matemáticas",validators=[DataRequired("Lenguaje y Matemáticas son pruebas obligatorias")])
    ciencia = IntegerField(label="Ciencas")
    historia = IntegerField(label="Historia")
    submit = SubmitField(label="Enviar")

@app.route("/",methods=["get","post"])
def principal():
    formulario = Formulario()
    render_template("index.html",formulario = formulario)

@app.route("/carreras")
def carreras():
    pass

if __name__=="__main__":
    app.run(debug=True)