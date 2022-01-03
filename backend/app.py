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
    print("----------")
    if request.method == 'POST':
        contenido = request.get_json()['content']
        # print(contenido)
        data = csvToJson(contenido)
        content = data[0]
        header = data[1]
        # print(data[0]) #obtiene la data
        # print(data[1]) #obtiene los headers

        return jsonify(
            isError= False,
            message= "Success",
            statusCode= 200,
            content = content,
            header = header
            ), 200
        

    return jsonify(
        isError= False,
        message= "Success",
        statusCode= 402,
        ), 402

@app.route(f'/reporte1', methods=['POST'])
def reporte1():

    if(request.method == 'POST'):

        body = request.get_json()
        result = Reporte1(body)

        return jsonify(
            isError = False,
            message = "Success",
            statusCode = 200,
            poly = result[0],
            dispers = result[1],
            rmse = result[2],
            r2 = result[3],
            label = result[4]
        ), 200

    return jsonify(
        isError= False,
        message= "Success",
        statusCode = 402,
        ), 402

if __name__ == "__main__":
    app.run(debug=True)