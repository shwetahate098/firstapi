from flask import Flask, jsonify,request
import json
import requests

app = Flask(__name__)




@app.post("/bbc")
def post():
        request_data = request.get_json()
        print(request_data)
        return jsonify("success message")
   

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    