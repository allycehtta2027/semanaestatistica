# streamlit run aula04.py

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("gato")
    st.image('https://static.streamlit.io/examples/cat.jpg')

with col2:
    st.header("cachorro")
    st.image('https://static.streamlit.io/examples/dog.jpg')

with col3:
    st.header("coruja")
    st.image('https://static.streamlit.io/examples/owl.jpg')