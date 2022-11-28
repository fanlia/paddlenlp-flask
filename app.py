# paddlenlp loaded from local directory
import sys
sys.path.append('/home/PaddleNLP')

import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from paddlenlp import Taskflow

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

@app.route("/uie", methods=['POST'])
def uie_route():
    schema = request.json.get('schema')
    ie = Taskflow('information_extraction', schema=schema)

    text = request.json.get('text')
    result = ie(text)
    return jsonify({'result': result})

if __name__ == "__main__":
    if os.getenv('FLASK_ENV') == 'development':
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run(host='0.0.0.0', port=5000)
