# -*- coding: utf-8 -*-
"""
Created on Mon May 17 19:17:42 2021

@author: Ashwin Anil
"""

import pandas as pd
#import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
#from scipy.stats import norm
import streamlit as st

# Read the Files
heartdf1 = pd.read_csv("heart.csv")
#heartdf2 = pd.read_csv("C:/Users/Ashwin Anil/Downloads/Heart Attack Datasets/o2Saturation.csv")

# Specifying the Categorical columns
categorical_cols = ['sex', 'cp', 'fbs', 'restecg', 'exng','slp', 'caa','thall'] 
continuous_cols = ['age', 'trtbps', 'chol','thalachh', 'oldpeak'] 

st.balloons()

st.title("Heart and Head")

st.write("You have the option of viewing three graphs of three variables in this application")
st.write("In the meanwhile  check out the first few rows of the dataset.")

st.sidebar.header("Heart Attack Data Graphs")
st.sidebar.subheader("Select the graph variable")
option = st.sidebar.selectbox("",('intro','age', 'trtbps', 'chol'))
if(option=='intro'):
    st.table(data = heartdf1.head())
else:
    placeholder = st.empty()
    data = heartdf1[option]
    plt.figure(1, figsize = (30,30))
    plt.title(f'Distribution of {option} variable', fontsize = 30)
    # plt.rcParams["figure.figsize"] = (15,10)
    sns.distplot(data,bins = 50, kde = 50, kde_kws={"color": "k", "lw": 5, "label": "KDE"}, hist_kws={"linewidth": 2,"alpha": 1, "color": "orange"})
    plt.rcParams['font.size'] = 30
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
        



