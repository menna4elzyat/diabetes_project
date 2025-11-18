import pickle
import streamlit as st
import pandas as pd 
# upload data 
pickle.load(open(r':\Users\menna\Downloads\archive (3)\Diabetes_predixtion.sav','rb'))
st.title('Diabetes Prediction web App')