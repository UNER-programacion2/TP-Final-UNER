# Flask
from flask import Flask, send_from_directory
from flask_restful import Api

from vinoteca import Vinoteca

# API
from recursos import *

if __name__ == "__main__":
    Vinoteca.inicializar()

    app = Flask(__name__)

#redirigir a la página principal index
    @app.route('/')
    def index():
        return send_from_directory('.', 'index.html')

    api = Api(app)
    api.add_resource(RecursoBodega, '/api/bodegas/<id>')
    api.add_resource(RecursoBodegas, '/api/bodegas')
    api.add_resource(RecursoCepa, '/api/cepas/<id>')
    api.add_resource(RecursoCepas, '/api/cepas')
    api.add_resource(RecursoVino, '/api/vinos/<id>')
    api.add_resource(RecursoVinos, '/api/vinos')


    app.run(debug=True)

