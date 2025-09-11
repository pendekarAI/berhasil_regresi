# Mengimpor library
import numpy as np
import pandas as pd
import streamlit as st
import pickle

# Menulis judul
st.header('Ini Aplikasi saya kereeen')

# Mendefinisikan features
rd  = 150000
mkt = 200000
adm = 250000

# Membuat menu input
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        rd = st.number_input('Masukkan nilau R&D', value=rd)
    with col2:
        mkt = st.number_input('Masukkan budget marketing', value=mkt)
    with col3:
        adm = st.number_input('Masukkan budget administrasi', value=adm)

# Memasukkan nilai wilayah
wly = st.selectbox('Masukkan Wilayah',('New York', 'Florida', 'California'))

# Menggabungkan data input
data = {
        'R&D':rd,
        'Marketing':mkt,
        'Administrasi':adm,
        'Wilayah':wly
        }

kolom = list(data.keys())

df_final = pd.DataFrame([data.values()], columns=kolom)

# Membuka model
modelku = pickle.load(open('model_regresi_terbaik.pkl', 'rb'))

# Memprediksi model
hasil = round(float(modelku.predict(df_final)),2)

# Menampilkan hasil prediksi
st.write('Prediksinya adalah = ', str(hasil))