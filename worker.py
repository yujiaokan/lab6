from flask import Flask
from flask import request
import requests
import os
import json
app = Flask(__name__)

def get_api_key() -> str:
    secret = os.environ.get("COMPUTE_API_KEY")
    if secret:
        return secret
    else:
        #local testing
        with open('.key') as f:
            return f.read()
      
@app.route("/")
def hello():
    return "Add workers to the Spark cluster with a POST request to add"

@app.route("/test")
def test():
    #return "Test" # testing 
    return(get_api_key())

@app.route("/add",methods=['GET','POST'])
def add():
  if request.method=='GET':
    return "Use post to add" # replace with form template
  else:
    #token=get_api_key()
    token="ya29.a0AX9GBdUyPBs1YWUKRE3uTueEIk1s6NXpaiXykDWmp9eeGGZl7J9miULGH6n7S4p7CGssuvtRdV75fFHoqhhzHYAVrLHnf95GrtduAYZPfrRh0LTY5DxbE6A702MzxyKA18zbHBV47tySxQPcIRGiT6-vkhnn94waCgYKAU0SAQASFQHUCsbCvp_85AXrHI7V0Kh_vDC79Q0166"
    ret = addWorker(token,request.form['num'])
    return ret


def addWorker(token, num):
    with open('payload.json') as p:
      tdata=json.load(p)
    tdata['name']='slave'+str(num)
    data=json.dumps(tdata)
    url='https://www.googleapis.com/compute/v1/projects/spark-372212/zones/europe-west1-b/instances'
    headers={"Authorization": "Bearer "+token}
    resp=requests.post(url,headers=headers, data=data)
    if resp.status_code==200:     
      return "Done"
    else:
      print(resp.content)
      return "Error\n"+resp.content.decode('utf-8') + '\n\n\n'+data


    

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')




