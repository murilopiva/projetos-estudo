import os
import pandas as pd 
import numpy as np 
import flask
from joblib import load
from flask import Flask, render_template, request

model = load('udemy.joblib')
app = Flask(__name__)

# como testar com uma amostra nova
def testarAmostra(amostra_nova):
       
    amostra = []
	
    for p in list(vocabulario):
        if p.lower() in amostra_nova.lower().replace('.','').split():
            amostra.append(1)
        else:
            amostra.append(0)
     
    amostra = np.array(amostra)
    amostra = amostra.reshape(1,-1)
    
    return model.predict(amostra)
    
    
#para carregar o vocabulario
vocabulario = []
with open("vocabulario.txt", encoding='utf8') as txt:
    for x in txt:
        li = x.split(',')  
        for h in li:
            if h not in vocabulario and len(h) > 0:
                vocabulario.append(h)


@app.route('/')
def index():
    return flask.render_template('indexUdemyCourses.html')
    
@app.route('/predict', methods = ['POST'])
def result():

    if request.method == 'POST':
        sample = request.form.to_dict()
        sample = list(sample.values())
        sample = list(map(str, sample))
        sample = sample[0] + ' ' + sample[1]
        sample = str(sample)
        
        prediction = testarAmostra(sample)
        
        return render_template("predictUdemyCourses.html", prediction = prediction)

if __name__ == "__main__":
    app.run(debug=True)