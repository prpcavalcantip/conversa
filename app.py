import streamlit as st
import os
from PIL import Image
from openai import OpenAI

# Inicializar cliente OpenAI com a chave do Streamlit Secrets
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except KeyError:
    st.error("Erro: Chave da API OpenAI não encontrada. Configure-a em st.secrets.")
    st.stop()

# Layout e estilo
st.set_page_config(page_title="Minha Conversa com Jesus", page_icon="🕊️", layout="centered")

# Estilo CSS
css = """
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
        color:
