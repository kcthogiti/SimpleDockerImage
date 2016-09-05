from flask import Flask
from flask import request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

#load the Logistic Regression Models
fl = open("uniquetargets.obj",'r')
unique_targets = pickle.load(fl)

#Load the Classes
fl = open("models.obj",'r')
models = pickle.load(fl)

#create an empty data frame with column names as classes
testing_probs = pd.DataFrame(columns=unique_targets)

@app.route("/", methods = ["GET"])
def index():
	return "Hello World!"

@app.route("/predict", methods = ["POST"])
def predict():
    dt = request.json
    values = dt.values()
    arr = np.array([values])
    for elem in unique_targets:
        lr = models[elem]
        ls = lr.predict_proba(arr)
        testing_probs[elem] = ls[:,1]
    return testing_probs.idxmax(axis = 1)[0]

if __name__ == "__main__":
	app.run(debug = True)