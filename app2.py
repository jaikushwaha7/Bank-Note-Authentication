# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""


@author: Jai.Kushwaha
"""

#from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
#import flasgger
#from flasgger import Swagger
import streamlit as st

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


    
#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(variance,skewness,curtosis,entropy):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

#@app.route('/predict_file',methods=["POST"])

def main():
    st.title("Bank Note Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style = "color:white;text-align:center;">Streamlit Bank Note Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance= st.text_input("Variance","Type Here")
    skewness = st.text_input("Skewness","Type Here")
    curtosis = st.text_input("Curtosis","Type Here")
    entropy = st.text_input("Entropy","Type Here")
    result=""
    if st.button("Predict"):
        result = predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success("The Output is {}".format(result))
    if st.button("About"):
        st.text("Lets learn")
        st.text('Built with Streamlit')

if __name__=='__main__':
   main()
    
    