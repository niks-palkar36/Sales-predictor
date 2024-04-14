import streamlit as st
import joblib
import numpy as np

model = joblib.load('mymodel.joblib')
st.title('Sales Predictor app')
tv = st.slider(
    'Tv investment',min_value=0,
    max_value=300,
    value=150)
Newspaper = st.slider(
    'Newspaper investment',min_value=0,
    max_value=300,
    value=150)
Radio = st.slider(
    'Radio investment',min_value=0,
    max_value=300,
    value=150)
input_data = np.array(
    [
        [tv,Radio,Newspaper]
    ]
)
prediction = model.predict(input_data)
st.subheader(
    f"""Predicted sales:
    {prediction[0]:.2f}"""
)