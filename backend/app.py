from flask import Flask, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

route = '/api'

@app.route('/')
def index():
    return render_template('index.html')


@app.route(f'{route}/p', methods=['GET'])
def home():
    return "UPDATE HOME"

if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)