from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from src.Convert import csvToJson


app = Flask(__name__)
CORS(app)

route = '/api'

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
        print(data[0]) #obtiene la data
        print(data[1]) #obtiene los headers
        
    else:
        print("hola")
        # print(request)

    return jsonify(
        isError= False,
        message= "Success",
        statusCode= 200,
        ), 200

if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)