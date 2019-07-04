# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 19:13:44 2019

@author: ASPDISCOVERY
"""

import numpy as np
import pandas as pd
import pickle

model=pickle.load(open(r"F:\mlp.pkl","rb"))
from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def predict():
    data=request.get_json(force=True)
    print(data)
    predi=model.predict(np.array([[data["ex']]))
    output=predi[0]
    print(output)
    
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=8000,debug=True)




