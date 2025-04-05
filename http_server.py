import json
from flasgger import Swagger, swag_from
import sql
from flask import Flask, jsonify, request

from flask_cors import CORS
app = Flask(__name__)
swagger = Swagger(app)
CORS(app, resources=r'/*')

@app.route("/") # 指定用户访问的相对地址
def hello_world():
    return "<p>Hello world!</p>" # 这里就是用户看到的最终页面


@app.route("/api/select_name", methods=['GET']) # 指定服务地址、服务类型
@swag_from('s.yml')
def get():
    name=request.args.get("name")
    ans = sql.sel_name(name)
    send=json.dumps({"data":ans})
    #print(send,ans)
    return jsonify(send) 

@app.route("/api/get1", methods=['GET']) # 指定服务地址、服务类型
@swag_from('s.yml')
def get1():
    name=request.args.get("name")
    ans = sql.sel_name1(name)
    send=json.dumps({"data":ans})
    #print(send)
    return jsonify(send) 

@app.route("/api/get2", methods=['GET']) # 指定服务地址、服务类型
@swag_from('s.yml')
def get2():
    name=request.args.get("pici")
    ans = sql.sel_pc(name)
    send=json.dumps({"data":ans})
    #print(send)
    return jsonify(send) 

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080, debug=True) 

