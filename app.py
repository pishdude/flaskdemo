from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/getcall/', methods=['GET'])
def respond():
 
    response = "Hello there! This is a JSON response"

    return jsonify(response)
    
    
@app.route('/')
def index():
    return "<h1 style = 'color:Blue'>This is HTML content !!</h1>"

if __name__ == '__main__':
   app.run(port=5000)