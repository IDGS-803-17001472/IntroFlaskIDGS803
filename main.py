from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    escuela = "UTL"
    alumnos = ["Mario", "Pedro", "Luis", "David"]
    return render_template("index.html" , escuela = escuela, alumnos = alumnos)

@app.route("/alumnos")
def alum():
    return render_template("alumnos.html")

@app.route("/maestros")
def maes():
    return render_template("maestros.html")

@app.route("/hola")
def hola():
    return "<p><h1>Hola desde Hola</h1></p>"

@app.route("/user/<string:name>")
def user(name):
    return f"hola {name}"

@app.route("/numero/<int:n>")
def numero(n):
    return f"El numero es {n}"

@app.route("/user/<int:id>/<string:name>")
def numero_string(id, name):
    return f"ID: {id} Nombre: {name}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"la suma de {n1} + {n2} es igual a {n1+n2}"

@app.route("/default")
@app.route("/default/<string:ab>")
def funcion(ab="UTL"):
    return "El valor es " + ab


if __name__ == "__main__":
    app.run(debug=True)