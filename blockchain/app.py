from blockchain import Blockchain
from flask import Flask
from waitress import serve

blockchain = Blockchain()
print("Blockchain app is running!")

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Blockchain!"

if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=8080)