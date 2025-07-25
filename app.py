import streamlit as st
import os
from PIL import Image
from openai import OpenAI

# Verifica chave da API
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except KeyError:
    st.error("Erro: Chave da API OpenAI não encontrada. Configure-a em st.secrets.")
    st.stop()

# Configuração da página
st.set_page_config(page_title="Minha Conversa com Jesus", page_icon="🕊️", layout="centered")

# Estilo CSS
css = '''
<style>
    .stApp {
        background-color: #FFFFFF;
        color: #2D2A32;
    }
    .titulo {
        font-size: 36px;
        font-weight: bold;
        color: #4B0082;
        text-align: center;
    }
    .subtitulo {
        font-size: 20px;
        color: #555;
        text-align: center;
    }
    .caixa {
        background-color: #f2f2f2;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
    }
    .botao {
        background-color: #4B0082;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
    }
    footer {
        text-align: center;
        font-size: 14px;
        color: gray;
        margin-top: 20px;
    }
    .doacao {
        text-align: center;
        margin-top: 20px;
        color: #2D2A32;
    }
</style>
'''
st.markdown(css, unsafe_allow_html=True)

# Título
st.markdown("<div class='titulo'>🕊️ Minha Conversa com Jesus</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Como você está se sentindo hoje?</div>", unsafe_allow_html=True)

# Entrada do sentimento
feeling = st.text_input("Descreva em poucas palavras seu estado emocional:")

# Função para gerar devocional
def gerar_devocional(sentimento):
    pass  # Corpo mínimo para evitar erro de sintaxe
