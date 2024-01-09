import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('penyakit_jantung.sav' , 'rb'))

st.title('Prediksi Penyakit Jantung')