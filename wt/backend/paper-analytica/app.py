from flask import Flask,render_template,jsonify,request,abort,Response
from flask_cors import CORS
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
    with open('default.json','r') as file:    
        default_data = json.load(file)
    
    x = re.search("\s+", topic)
    if(x!=None):
        
        print()
        print("You entered the following: ","'",topic,"'")
        print("Please don't enter whitespaces, tabs etc.")
        print("Returning Default Data!")
        
    
        default_data.insert(0,{"name": "default","author": "","link_html": "","link_pdf": "","render_def_statement":"whitespace","card_render":"false"})
        for i in default_data:
            if(i["name"]!="default"):
                i["render_def_statement"]="not_default"
                i["card_render"]="true"
        print()
        print("The Data in JSON File is:",default_data)
        print()
        print("The type of the data is:",type(default_data))  
        print()
        

        return Response(json.dumps(default_data), mimetype='text/json',headers={'Cache-Control':'no-cache'})
    
    y = re.search("\-+", topic)
    if(y!=None):
        
        print()
        print("You entered the following: ","'",topic,"'")
        print("Please don't enter whitespaces, tabs etc.")
        print("Returning Default Data!")
        
        default_data.insert(0,{"name": "default","author": "","link_html": "","link_pdf": "","render_def_statement":"whitespace","card_render":"false"})
        for i in default_data:
            if(i["name"]!="default"):
                i["render_def_statement"]="not_default"
                i["card_render"]="true"
        print()
        print("The Data in JSON File is:",default_data)
        print()
        print("The type of the data is:",type(default_data))  
        print()
        

        return Response(json.dumps(default_data), mimetype='text/json',headers={'Cache-Control':'no-cache'})
    
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:0-9]')
    if(regex.search(topic) != None):
        
        print()
        print("You entered the following: ","'",topic,"'")
        print("Please don't enter any special characters or numbers.")
        print("Returning Default Data!")
        
        default_data.insert(0,{"name": "default","author": "","link_html": "","link_pdf": "","render_def_statement":"special","card_render":"false"})
        for i in default_data:
            if(i["name"]!="default"):
                i["render_def_statement"]="not_default"
                i["card_render"]="true"
        print()
        print("The Data in JSON File is:",default_data)
        print()
        print("The type of the data is:",type(default_data))  
        print()
        

        return Response(json.dumps(default_data), mimetype='text/json',headers={'Cache-Control':'no-cache'})
    
    out = subprocess.run(['python', 'model.py', topic])
    #print(out.stdout)
    with open('recommendation.json') as json_file:
        data = json.load(json_file)

    #data = json.dumps(data)

   
    print()
    if(data == default_data):
        print("DEFAULT DATA, AS RECOMMENDATION FOR ","'",topic,"'"," COULDN'T BE FOUND!")  
        print()
        data.insert(0,{"name": "default","author": "","link_html": "","link_pdf": "","render_def_statement":"default","card_render":"false"})
    else:
        data.insert(0,{"name": "default","author": "","link_html": "","link_pdf": "","render_def_statement":"not_default","card_render":"false"})
        print("RECOMMENDATION FOR ","'",topic,"'"," FOUND!")
        print()
    for i in data:
        if(i["name"]!="default"):
            i["render_def_statement"]="false"
            i["card_render"]="true"

    print("The Data in JSON File is:",data)
    print()
    print("The type of the data is:",type(data))  
    print()

    

    #result=out.stdout
    # print(result,type(result))
    # inter_result = eval(dumps(str(result.decode("utf-8"))))
    # final=[]
    # my_json = result.decode('utf8')
    # print(my_json,type(my_json))

    # for i in my_json:
    #     print(i,type(i))
        #final.append(loads(i))
    
    
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
    print()
    print("Returning Year Histogram Image Blob!")
    print()

    response= make_response(send_file("year.png", mimetype='image/png'))
    response.headers['Cache-Control'] = 'no-cache'
    print("The Image Blob Object is:",response)
    print()
    print("The type of the blob is:",type(response))
    print()
    return response

@app.route("/getHistogram/author", methods=["GET"])
def sendAuthorHistogram():
    #img = Image.open("year.png")
    # print(img)
    # url = "C:/Users/harik/OneDrive/Desktop/Vue2/wt/backend/paper-analytica"
    
    # return Response(url, mimetype='text/html')
    # return Response(img, mimetype='image/png')
    print()
    print("Returning Author Histogram Image Blob!")
    print()

    response= make_response(send_file("author.png", mimetype='image/png'))
    response.headers['Cache-Control'] = 'no-cache'
    print("The Image Blob Object is:",response)
    print()
    print("The type of the blob is:",type(response))
    print()
    return response



if __name__=="__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)