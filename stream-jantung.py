import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('PENYAKIT_JANTUNG.sav' , 'rb'))

st.title('Prediksi Penyakit Jantung')
