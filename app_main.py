import streamlit as st
import numpy as np
import pickle

try:
    with open("case_study_emp.pkl", "rb") as f:
        clf = pickle.load(f)
except Exception as e:
    st.error(f"Error loading model: {e}")


st.title("Case Study On Employee-Attration-Rate-main ")
st.markdown("Let's Predic the rate")

st.header("")
col1, col2 = st.columns(2)

with col1:
    el=st.slider("Education Level", 1,5,2)
    tos = st.slider("Time of Service", 1.0, 100.0, 0.5)
    top = st.slider("Time of Promotion", 0.0, 50.0, 0.5)
    gr = st.slider("Growth Rate", 1,5,2)
    gr1 = st.slider("Post Level", 1,5,2)

st.text('')
if st.button("Chance To Get Admission"):
    # Create a numpy array for the prediction
    input_data = np.array([[el,tos,top,gr,gr1]])
    # Get prediction
    result = predict(input_data)
    # Display result
    st.text(f"Admission Chance: {result[0]}")







