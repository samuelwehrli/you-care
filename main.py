# streamlit app which loads text data and displays it randomly when the user clicks a button

import streamlit as st
import pandas as pd
from random import choice

# title
st.title('Ratschläge für betreuende Angehörige')

problem_list = [
    'Kommunikation',
    'Essen und Trinken',
    'Körperpflege',
    'Mobilität',
    'Ernährung',
    'Finanzen',
    'Psychische Gesundheit',
    'Soziale Kontakte',
    'Sonstiges']

# dropdown to select problem
problem = st.selectbox('Welches Problem betrifft dich?', problem_list)
if problem == 'Essen und Trinken':
    st.info('Für dieses Thema haben wir gute Ratschläge.')
else:
    st.warning('Für dieses Thema haben wir leider noch keine Ratschläge. Im Moment gibt es nur Ratschläge für Essen und Trinken.')



# Use utf-8 encoding to avoid errors.
with open('advice.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# splite text by '-' and remove empty strings and trailing whitespaces
advice_list = [x.strip() for x in text.split('-') if x.strip()]

# button
if st.button('Gib mir einen Ratschlag!') & (problem == 'Essen und Trinken'):
    # display random row from data
    st.write(choice(advice_list))

