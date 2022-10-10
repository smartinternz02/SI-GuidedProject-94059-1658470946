from flask import Flask, render_template, request
import requests

import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "7Y0HoWPElQ9JLR-rhBQgwr6Mo7DPMweNGT5xZJFroOtb"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__)
import pickle
model = pickle.load(open('cereal analysis.pkl', 'rb'))

@app.route('/')
def helloworld():
    return render_template("base.html")

@app.route('/assesment',methods=["POST"])
def prediction():
    return render_template("index.html")

@app.route('/predict', methods = ['POST','GET'])
def admin():
    a= request.form["mfr"]
    if (a == 'a'):
        a1,a2,a3,a4,a5,a6,a7=1,0,0,0,0,0,0
    if (a == 'g'):
        a1,a2,a3,a4,a5,a6,a7=0,1,0,0,0,0,0
    if (a == 'k'):
        a1,a2,a3,a4,a5,a6,a7=0,0,1,0,0,0,0
    if (a == 'n'):
        a1,a2,a3,a4,a5,a6,a7=0,0,0,1,0,0,0
    if (a == 'p'):
        a1,a2,a3,a4,a5,a6,a7=0,0,0,0,1,0,0
    if (a == 'q'):
        a1,a2,a3,a4,a5,a6,a7=0,0,0,0,0,1,0
    if (a == 'r'):
        a1,a2,a3,a4,a5,a6,a7=0,0,0,0,0,0,1

    b =request.form["type"]
    if (b == 'c'):
        b=0
    if (b == 'h'):
        b=1
    c = request.form["Calories"]
    d = request.form["Protien"]
    e = request.form["Fat"]
    f = request.form["Sodium"]
    g = request.form["Fiber"]
    h = request.form["Carbo"]
    i = request.form["Sugars"]
    j = request.form["Potass"]
    k = request.form["Vitamins"]
    l = request.form["Shelf"]
    m = request.form["Weight"]
    n = request.form["Cups"]

    t = [[int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7),int(b),int(c),int(d),int(e),int(f),int(g),int(h),int(i),int(j),int(k),int(l),int(m),int(n)]]
    y = model.predict(t)
    print(y)
    payload_scoring = {"input_data": [{"field": ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'Type', 'Calories',
                                                 'Protien', 'Fat', 'Sodium', 'Fiber', 'Carbo', 'Sugars', 'Potass',
                                                 'Vitamins', 'Shelf', 'Weight', 'Cups'],
                                       "values": [[0, 1, 0, 0, 0, 0, 0, 0,
                                                   100, 2, 1, 140, 2, 11, 10, 120,
                                                   25, 3, 1, 0.75]]}]}

    response_scoring = requests.post(
        'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/a8fecb2a-e01c-4d94-8ccd-b9f33da4b6bc/predictions?version=2022-07-28',
        json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    return render_template("prediction.html", z = y[0][0])

if __name__ == '__main__':
    app.run(debug = True)