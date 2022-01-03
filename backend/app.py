from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from src.Convert import csvToJson
from src.Reportes import *


app = Flask(__name__)
CORS(app)

data = None;
# route = '/api'

@app.route('/')
def index():
    return render_template('index.html')



@app.route(f'/cargar', methods=['POST'])
def prueba():
    try:
        contenido = request.get_json()['content']
        # print(contenido)
        data = csvToJson(contenido)
        content = data[0]
        header = data[1]
        # print(data[0]) #obtiene la data
        # print(data[1]) #obtiene los headers

        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
            "content": content,
            "header": header
        }
    except:
        result = {
            "status":402,
        }
    
    return jsonify(result)

@app.route(f'/reporte1', methods=['POST'])
def reporte1():
    try:
        
        body = request.get_json()
        result = Reporte1(body)

        result = {
            "isError": False,
            "message": "Success",
            "statusCode": 200,
            "poly": result[0],
            "dispers": result[1],
            "rmse": result[2],
            "r2": result[3],
            "label": result[4]
        }
        
    except:
        result = {
            "status": 402
        }


    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5000, debug=True)