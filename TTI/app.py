from flask import Flask, render_template, request, url_for  
import requests
import io
from PIL import Image
import base64

app = Flask(__name__)

API_URL = "link to your api"
HEADERS = {"Authorization": "Bearer Yout api key"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text_input = request.form['text_input']
    image_bytes = query({"inputs": text_input})
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    print(f"Generated image base64: {image_base64[:50]}...")
    return render_template('index.html', image_base64=image_base64)

def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.content

if __name__ == '__main__':
    app.run(debug=True)
