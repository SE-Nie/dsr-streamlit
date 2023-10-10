import streamlit as st
import pandas as pd
import numpy as np

st.write('Hello World')
st.write('Hello again')
st.write('Hello again again')
st.video('https://www.youtube.com/watch?v=9Q6sLbz37gk')
st.sidebar.write('Hello from the sidebar')
a = st.sidebar.radio('Select a page', ['Home', 'About', 'Contact'])
if a == "Home":
    st.write('You selected Home')
elif a == "About":
    st.write('You selected About')
else:    
    st.write('You selected Contact')

col1, col2 = st.columns(2)
col1.write('This is column 1')
col2.write('This is column 2')

st.checkbox("I agree")
st.slider('Select a value', 0, 100, 50)
st.multiselect('Select a value', ['A', 'B', 'C', 'D'])
st.time_input('Select a time')

@st.cache_data #only works with functions
def load_data(url, nrows_):
    return pd.read_csv(url, nrows=nrows_)
   

DATA_URL = ('https://s3-us-west-2.amazonaws.com/''streamlit-demo-data/uber-raw-data-sep14.csv.gz')

data = load_data(DATA_URL, 1000)
st.dataframe(data)
data = data.rename(columns={'Lat': 'LAT', 'Lon': 'LON'})
st.dataframe(data)
st.map(data.loc[:, ['LAT', 'LON']])