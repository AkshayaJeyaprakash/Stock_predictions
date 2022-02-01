import os
import warnings
warnings.filterwarnings('ignore')
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
import streamlit as st

def predict_stock(df):
    date = df['date']
    open1 = df['open']
    close1 = df['close']
    X1 = open1.values
    X2 = close1.values
    train1 = X1[0:len(X1)]
    train2 = X2[0:len(X2)]
    history1 = [x for x in train1]
    history2 = [x for x in train2]
    predictions1 = list()
    predictions2 = list()
    for t in range(10):
        model1 = SARIMAX(history1, order=(1, 1, 1), seasonal_order=(0,0,0,0))
        model_fit1 = model1.fit(disp=False)
        output1 = model_fit1.forecast()
        yhat1 = output1[0]
        predictions1.append(yhat1)
        history1.append(yhat1)
        st.write("DAY: ",t+1)
        st.write('predicted opening value = %f' % (yhat1))
        
        model2 = SARIMAX(history2, order=(1, 1, 1), seasonal_order=(0,0,0,0))
        model_fit2 = model2.fit(disp=False)
        output2 = model_fit2.forecast()
        yhat2 = output2[0]
        predictions2.append(yhat2)
        history2.append(yhat2)
        st.write('predicted closing value = %f' % (yhat2),"\n")
    st.write(" ")
    st.write("THE PLOT OF OPENING, CLOSING VALUES")
    f = plt.figure()
    f.set_figwidth(12)
    f.set_figheight(4)
    plt.subplot(1, 2, 1)
    plt.plot(predictions1)
    plt.title("OPENING")
    plt.subplot(1, 2, 2)
    plt.plot(predictions2)
    plt.title("CLOSING")
    plt.show();
    st.pyplot(f)
    


menu = ["ABOUT ME","PREDICT YOUR STOCK"]
choice = st.sidebar.selectbox("Menu",menu)
if choice=="PREDICT YOUR STOCK":
    st.title("PREDICT YOUR STOCK")
    st.subheader("Done by: Akshaya Jeyaprakash")
    f = st.file_uploader("Choose a csv or excel file")
    if f is not None:
        try:
            df = pd.read_excel(f)
        except:
            try:
                df = pd.read_csv(f)
            except: 
                st.warning("you need to upload a csv or excel file.")
        predict_stock(df)

elif choice =="ABOUT ME":
    st.title("PREDICT YOUR STOCK")
    st.subheader("Done by: Akshaya Jeyaprakash")
    st.write(" ")
    st.write("THIS WEB APPLICATION WILL PREDICT THE VALUE OF A PARTICULAR STOCK FOR NEXT 10 DAYS\nFROM THE DATA WHICH IS SUPPLIED AS INPUT TO IT ")
    st.write(" ")
    st.write("MORE THE AMOUNT OF DATA GIVEN AS AN INPUT, MORE ACCURATE THE PREDICTIONS ARE !!! ")
    st.write(" ")
    st.write("THE HISTORY OF STOCK DATA OF A PARTICULAR STOCK MUST BE UPLADED AS .XLS OR .CSV...\nTHE .CSV OR THE .XLS FILE UPLOADED MUST STRICTLY OBEY THE FORMAT GIVEN BELOW")
    st.image("FILE.png")


    

