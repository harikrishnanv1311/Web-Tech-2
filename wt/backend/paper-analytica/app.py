from flask import Flask,render_template,jsonify,request,abort,Response
from flask_cors import CORS
from PIL import Image
from flask import send_file
from flask import make_response
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
    #print(data)
    return Response(json.dumps(data), mimetype='text/json',headers={'Cache-Control':'no-cache'})
    # # output = subprocess.check_output(['model.py',topic])
    # # print(output)
    # # return "lol"

@app.route("/getHistogram/year", methods=["GET"])
def sendYearHistogram():
    #img = Image.open("year.png")
    # print(img)
    # url = "C:/Users/harik/OneDrive/Desktop/Vue2/wt/backend/paper-analytica"
    
    # return Response(url, mimetype='text/html')
    # return Response(img, mimetype='image/png')
    response= make_response(send_file("year.png", mimetype='image/png'))
    response.headers['Cache-Control'] = 'no-cache'
    print(type(response))
    return response

@app.route("/getHistogram/author", methods=["GET"])
def sendAuthorHistogram():
    #img = Image.open("year.png")
    # print(img)
    # url = "C:/Users/harik/OneDrive/Desktop/Vue2/wt/backend/paper-analytica"
    
    # return Response(url, mimetype='text/html')
    # return Response(img, mimetype='image/png')
    response= make_response(send_file("author.png", mimetype='image/png'))
    response.headers['Cache-Control'] = 'no-cache'
    print(type(response))
    return response



if __name__=="__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)