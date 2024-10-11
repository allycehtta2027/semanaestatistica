import streamlit as st
import pandas as pd

st.title("carregue o seu Dataset")

upload = st.file_uploader("Escolha o seu arquivo", type="csv")
if upload is not None: 
    df = pd.read_csv(upload)
    st.dataframe(df)