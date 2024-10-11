# crie um algoritmo que descubra um numero secreto

# criar numero secreto

# titulo de aplicação

# dar uma mensagem de boas vindas

# receber o chute do usuario

# verificar o chute com o numero secreto

# mostrar uma mensagem personalizado

import streamlit as st
import random

# Função para sortear um número entre 1 e 10
def sorteia_numero_entre(inicio, fim):
    return random.randint(inicio, fim)

# Inicializa o número secreto se não estiver definido
if 'numero_secreto' not in st.session_state:
    st.session_state.numero_secreto = sorteia_numero_entre(1, 10)

# Título da aplicação
st.title("Bem-vindo ao Jogo do Número Secreto!")

# Mensagem de boas-vindas
st.write("Tente adivinhar o número secreto entre 1 e 10.")

# Receber chute do usuário
chute = st.number_input("Digite seu palpite:", min_value=1, max_value=10)

# Verificar o chute com o número secreto
if st.button('Verificar'):
    numero_secreto = st.session_state.numero_secreto
    
    if chute == numero_secreto:
        st.success(f"Parabéns! Você adivinhou o número secreto: {numero_secreto}")
        st.balloons()
        st.snow()
        # Reinicia o jogo
        st.session_state.numero_secreto = sorteia_numero_entre(1, 10)
    elif chute < numero_secreto:
        st.warning("Seu palpite é muito baixo. Tente novamente.")
    else:
        st.warning("Seu palpite é muito alto. Tente novamente.")
