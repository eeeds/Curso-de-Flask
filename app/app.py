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
#Esto se verá al ir a esa ruta
@app.route('/holaMundo')
def hola_mundo():
    return "Hola mundo"
#Si corremos como el main se inicia el servidor
if __name__ == '__main__':
    app.add_url_rule('/', view_func = index)
    app.run(debug = True, port = 5005)
