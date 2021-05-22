from flask import Flask, render_template

#Se le pasa ese parámetro para luego saber si se trabajará con un archivo principal
app = Flask(__name__)
#Se accede a la ruta raíz
"""
@app.route('/')
def index():
    return "Hola"
"""
def index():
    #Renderizar plantilla
    #return render_template('index.html', titulo = 'Pagina Principal')
    data = {'titulo': 'Index', 'encabezado': 'Bienvenido'}
    return render_template('index.html', data = data)

@app.route('/contacto')
def contacto():
    data = {'titulo': 'Contacto', 'encabezado': 'Bienvenido'}
    return render_template('contacto.html', data = data)
#Esto se verá al ir a esa ruta, se define el parámetro nombre y deben tener el mismo nombre tanto en app como en la función.
@app.route('/saludo/<nombre>')
def saludo(nombre):
    #return 'Hola, Codi'
    return "Hola, {}".format(nombre)


@app.route('/suma/<int:valor1>/<int:valor2>')
def suma(valor1, valor2):
    return 'La suma es: {}'.format((valor1+valor2))


@app.route('/perfil/<nombre>/<int:edad>')
def perfil(nombre, edad):
    return 'Tu nombre es: {} y tu edad es {}'.format(nombre, edad)

@app.route('/lenguajes')
def lenguajes():
    data={'hay_lenguajes':False, 'lenguajes':['PHP', 'Python', 'Kotlin', 'Java', 'C#', 'Javascript']}
    return render_template('lenguajes.html', data = data)

@app.route('/holaMundo')
def hola_mundo():
    return "Hola mundo"
#Si corremos como el main se inicia el servidor
if __name__ == '__main__':
    app.add_url_rule('/', view_func = index)
    app.run(debug = True, port = 5005)
