import streamlit as st
import pandas as pd
import numpy as np
import pickle 
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def load_model():
    with open('saved.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data['model']
x = data['x']

def show_page():
    st.write("<h1 style='text-align: center; color: blue;'>مدل پیش بینی قیمت طلا</h1>", unsafe_allow_html=True)
    st.write("<h2 style='text-align: center; color: gray;'>ETF پیش بینی بر اساس شاخص های صندوق</h2>", unsafe_allow_html=True)
    st.write("<h3 style='text-align: center; color: gray;'>شاخص های زیر را وارد کنید</h3>", unsafe_allow_html=True)
    st.write("<h4 style='text-align: center; color: gray;'>Robo-Ai.ir طراحی شده توسط</h4>", unsafe_allow_html=True)
    button2 = st.link_button("Robo-Ai بازگشت به", "https://robo-ai.ir")
    
    SPX = st.slider('شاخص سهام 500 شرکت بزرگ ایالات متحده (S & P 500)', 676.0, 2872.0, 700.0)

    USO = st.slider('شاخص نفت خام ایالات متحده', 7.96, 117.4, 10.0)

    SLV	 = st.slider('شاخص نقره', 8.85, 47.25, 10.0)

    EUR_USD = st.slider('نسبت یورو به دلار', 1.039, 1.59, 1.050)

    button = st.button('محاسبه و پیش بینی')
    if button:
        x = np.array([[SPX, USO, SLV, EUR_USD]])

        prediction = model.predict(x)
        st.write("<h4 style='text-align: center; color: gray;'>:بر اساس داده های وارد شده، قیمت طلا به دلار برابر خواهد بود با</h4>", unsafe_allow_html=True)
        st.subheader(prediction[0])
show_page()
