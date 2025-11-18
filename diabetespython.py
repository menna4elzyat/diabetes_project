
import pickle
import streamlit as st
import pandas as pd 
# upload data 
data = pickle.load(open('Diabetes_predixtion.sav','rb'))

st.title('Diabetes Prediction web App')
st.info('Easy app for Diabetes prediction deseas')
st.sidebar.header('feature selection')
#Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
#       'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'],
pre=st.text_input('Pregnancies')
glu=st.text_input('Glucose')
blo=st.text_input('BloodPressure')
sk=st.text_input('SkinThickness')
ins=st.text_input('Insulin')
bmi=st.text_input('BMI')
df=st.text_input('DiabetesPedigreeFunction')
age=st.text_input('Age')
dataframe=pd.DataFrame({'Pregnancies':[pre],'Glucose':[glu],'BloodPressure':[blo],'SkinThickness':[sk],'Insulin':[ins],'BMI':[bmi],'DiabetesPedigreeFunction':[df],'Age':[age]},index=[0])
con=st.sidebar.button('confirm')
if con:
    result=data.predict(dataframe)
    if result==0:
        st.sidebar.write('The Patiant is Clear')
        st.sidebar.image('https://www.pngfind.com/pngs/m/85-858511_health-icon-hd-png-download.png',width=250)
    else:
        st.sidebar.write('The Patiant was Daseas')   
        st.sidebar.image('https://images.pexels.com/photos/6823763/pexels-photo-6823763.jpeg',width=250)

