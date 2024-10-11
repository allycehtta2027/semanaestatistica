# import o streamlit

# entre com um número

# verifique se o número é positivo, negativo ou nulo.

   
import streamlit as st
numero = st.number_input("digite o numero: ",step=1)


# Verificar se o número é positivo, negativo ou nulo
if numero > 0:
    st.write(f"O número {numero} é positivo.")
elif numero < 0:
    st.write(f"O número {numero} é negativo.")
else:
    st.write(f"O número é nulo.")



