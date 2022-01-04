from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from src.Convert import csvToJson
from src.Reportes import *
from src.Reporte2 import *
from src.Reporte3 import *
from src.Reporte4 import *
from src.Reporte5 import *
from src.Reporte6 import *
from src.Reporte7 import *
from src.Reporte8 import *
from src.Reporte9 import *
from src.Reporte10 import *
from src.Reporte11 import *
from src.Reporte12 import *
from src.Reporte13 import *
from src.Reporte14 import *
from src.Reporte15 import *
from src.Reporte16 import *
from src.Reporte17 import *


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
            "status": 200,
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

@app.route(f'/reporte2', methods=['POST'])
def reporte2():
    try:
        
        body = request.get_json()
        
        result = Report2(body)
        # print(result)
        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
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

@app.route(f'/reporte3', methods=['POST'])
def reporte3():
    try:
        
        body = request.get_json()
        result = Report3(body)

        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
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

@app.route(f'/reporte4', methods=['POST'])
def reporte4():
    try:
        
        body = request.get_json()
        # print(body)
        result = Report4(body)

        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
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

@app.route(f'/reporte5', methods=['POST'])
def reporte5():
    try:
        
        body = request.get_json()
        
        result = Report5(body)
        # print(result)
        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
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

@app.route(f'/reporte6', methods=['POST'])
def reporte6():
    try:
        
        body = request.get_json()
        result = Report6(body)

        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
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

@app.route(f'/reporte7', methods=['POST'])
def reporte7():
    try:
        
        body = request.get_json()
        
        result = Report7(body)
        # print(result)
        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
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

@app.route(f'/reporte8', methods=['POST'])
def reporte8():
    try:
        
        body = request.get_json()
        
        result = Report8(body)
        # print(result)
        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
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

@app.route(f'/reporte9', methods=['POST'])
def reporte9():
    try:
        
        body = request.get_json()
        
        result = Report9(body)
        # print(result)
        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
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


@app.route(f'/reporte10', methods=['POST'])
def reporte10():
    try:
        
        body = request.get_json()
        
        result = Report10(body)
        # print(result)
        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
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


@app.route(f'/reporte11', methods=['POST'])
def reporte11():
    try:
        
        body = request.get_json()
        
        result = Report11(body)

        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
            "bar": result[0],
            "title": result[1],
            "labels": result[2],
            "descr": result[3],
        }
        
    except:
        result = {
            "status": 402
        }


    return jsonify(result)

@app.route(f'/reporte12', methods=['POST'])
def reporte12():
    try:
        
        body = request.get_json()
        
        result = Report12(body)
        # print(result)
        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
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


@app.route(f'/reporte13', methods=['POST'])
def reporte13():
    try:
        
        body = request.get_json()
        
        result = Report13(body)

        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
            "poly": result[0],
            "title": result[1],
            "labels": result[2],
        }
    except:
        result = {
            "status": 402
        }


    return jsonify(result)


@app.route(f'/reporte14', methods=['POST'])
def reporte14():
    try:
        
        body = request.get_json()
        
        result = Report14(body)
        # print(result)
        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
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

@app.route(f'/reporte15', methods=['POST'])
def reporte15():
    try:
        
        body = request.get_json()
        # print(body)
        result = Report15(body)

        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
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

@app.route(f'/reporte16', methods=['POST'])
def reporte16():
    try:
        
        body = request.get_json()
        
        result = Report16(body)
        # print(result)
        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
            "bar": result[0],
            "title": result[1],
            "labels": result[2],
            "descr": result[3],
        }
        
    except:
        result = {
            "status": 402
        }


    return jsonify(result)


@app.route(f'/reporte17', methods=['POST'])
def reporte17():
    try:
        
        body = request.get_json()
        
        result = Report17(body)
        # print(result)
        result = {
            "isError": False,
            "message": "Success",
            "status": 200,
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