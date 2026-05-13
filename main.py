import streamlit as st
import numpy as np
import pickle

st.title("Iris Flower Classification App")
with open("model.pkl", "rb") as f:
    lr_model = pickle.load(f)
sl = st.slider("Insert a sepal Length", 0, 10, 1)
sw = st.slider("Insert a sepal Width", 0, 10, 1)
pl = st.slider("Insert a petal Length", 0, 10, 1)
pw = st.slider("Insert a petal Width", 0, 10, 1)
# pred = lr_model.predict(np.array([[sl, sw, pl, pw]]))
# st.write("The flower is :", pred[0])

if st.button ("Predict"):
    pred = lr_model.predict (np.array([[sl,sw,pl,pw]]))
    st.write ("The flower is :", pred[0])