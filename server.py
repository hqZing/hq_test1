from flask_cors import CORS
from flask import Flask, request, jsonify
from functools import wraps


app = Flask(__name__)






@app.route("/")
def index():
    
    rtn_dict = {
        "success": True,
        "info": "测试测试测试"
    }
    return jsonify(rtn_dict)





if __name__ == "__main__":
    CORS(app, supports_credentials=True)
    app.run(host='0.0.0.0', port=12333)
