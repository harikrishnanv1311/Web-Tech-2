from flask import Flask,render_template,jsonify,request,abort,Response
from flask_cors import CORS
import ast
import json
import pprint
import sqlite3
import subprocess
import requests
import re

app = Flask(__name__)
CORS(app)
cors=CORS(app, resources={
    r"/*":{
        "origins": "*"
    }
})

@app.route("/")
def Hello():
    return "In"

@app.route("/getRecommendation/<topic>", methods=["GET"])
def sendRecommendation(topic):
    out = subprocess.run(['python', 'model.py', topic])
    #print(out.stdout)


    with open('recommendation.json') as json_file:
        data = json.load(json_file)

    #print(data)    
    #result=out.stdout
    # print(result,type(result))
    # inter_result = eval(dumps(str(result.decode("utf-8"))))
    # final=[]
    # my_json = result.decode('utf8')
    # print(my_json,type(my_json))

    # for i in my_json:
    #     print(i,type(i))
        #final.append(loads(i))
    
    #print(final,type(final))
    #print(inter_result, type(inter_result))
    # final = ast.literal_eval(inter_result)
    # print(final, type(final))
    # # for i in stdout:
    # #     title = i[0]
    # #     author
    print(data)
    return Response(json.dumps(data), mimetype='text/json')
    # # output = subprocess.check_output(['model.py',topic])
    # # print(output)
    # # return "lol"


if __name__=="__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)