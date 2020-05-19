# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
 
"""
from flask import Flask,render_template,request


import pickle
import numpy as np

model=pickle.load(open('Energy Output.pkl','rb'))


app=Flask(__name__)
@app.route('/')

def home():
    return render_template("index.html")


@app.route('/login',methods=['POST'])
def login():
    Tp=request.form['Tp']
    Ev=request.form['Ev']
    Ap=request.form['Ap']
    Rh=request.form['Rh']
    
    
    total=[[int(Tp),int(Ev),int(Ap),int(Rh)]]
    y_pred=model.predict(total)
    print(y_pred)
    return render_template("index.html",showcase=y_pred)

if __name__=='__main__':
    app.run(debug=False)
