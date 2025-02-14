from flask import Flask, render_template, request

app = Flask(__name__)  # Aquí cambia _name_ por __name__

@app.route('/')
def index():
    grupo="IDGS803"
    lista=["Juan","Pedro"]
    return render_template("index.html",grupo=grupo,lista=lista)

@app.route('/ejemplo1')
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route('/ejemplo2')
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route('/cinepolis', methods=['GET', 'POST'])
def cinepolis():
    total_pagar = ""
    mensaje = ""

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        cantidad_compradores = int(request.form.get('cantidad_compradores'))
        tarjeta_cineco = request.form.get('tarjeta_cineco')
        cantidad_boletos = int(request.form.get('cantidad_boletos'))
       
        if cantidad_boletos > 7:
            mensaje = "No se pueden comprar más de 7 boletos"
            return render_template("cinepolis.html", total_pagar=mensaje)
        
        precio_boleto = 12
        total = cantidad_boletos * precio_boleto
        
        
        if cantidad_boletos > 5:
            total *= 0.85
        elif 3 <= cantidad_boletos <= 5:
            total *= 0.90 
        if tarjeta_cineco == 'Si':
            total *= 0.90
        
        total_pagar = "${}".format(round(total, 2))

    
    return render_template("cinepolis.html", total_pagar=total_pagar)

@app.route('/')
def operaBas():
    return render_template("OperasBas.html")

@app.route('/resultado',methods=["GET","POST"])
def resultado():
    
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        resultado=num1+num2
    return "La suma de {} y {} es {}".format(num1,num2,int(num1)+int(num2))

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


@app.route("/form1")
def form1():
    return '''
            <form>
            <label>Nombre:</label>
            <input type="text" name="nombre" placeholder="Nombre">
            <br>
            <label>Nombre:</label>
            <input type="text" name="nombre" placeholder="Nombre">
            <br>
        </form>

        '''

# Cambia _name_ por __name__
if __name__ == '__main__':
    app.run(debug=True, port=300)



