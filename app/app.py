from flask import Flask

#Se le pasa ese parámetro para luego saber si se trabajará con un archivo principal
app = Flask(__name__)

#Si corremos como el main se inicia el servidor
if __name__ == '__main__':
    app.run()
