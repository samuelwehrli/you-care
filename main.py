# streamlit app which loads text data and displays it randomly when the user clicks a button

import streamlit as st
import pandas as pd
from random import choice

# load data
#df = pd.read_csv('data.csv')

# read text file advice.txt and store all data in variable text.
# Use utf-8 encoding to avoid errors.
with open('advice.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# splite text by '-' and remove empty strings and trailing whitespaces
advice_list = [x.strip() for x in text.split('-') if x.strip()]

# button
if st.button('Gib mir einen Ratschlag!'):
    # display random row from data
    st.write(choice(advice_list))

