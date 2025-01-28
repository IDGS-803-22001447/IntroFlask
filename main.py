from flask import Flask

app = Flask(__name__)  # Aquí cambia _name_ por __name__

@app.route('/')
def index():
    return "Hola mundo!!"

@app.route("/hola")
def hola():
    return "Hola!!!"

# va a recibir un parámetro de tipo String
@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}!!!"

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero {}".format(n)

# Los métodos tienen que cambiar si una ruta es igual para dos métodos
@app.route("/user/<string:user>/<int:id>")
def username(user, id):
    return f"Nombre: {user} ID: {id}!!!"

# Pasando dos números flotantes para regresar la suma
@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es: {}!!!".format(n1 + n2)

# Cambia _name_ por __name__
if __name__ == '__main__':
    app.run(debug=True, port=300)
