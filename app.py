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
        font-size: 42px;
        font-weight: bold;
        color: #4B0082;
        text-align: center;
        margin-top: 20px;
    }
    .subtitulo {
        font-size: 22px;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    .caixa {
        background-color: #F9F9FF;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0px 4px 16px rgba(0,0,0,0.07);
        margin-bottom: 30px;
        color: #2D2A32;
        border-left: 6px solid #4B0082;
    }
    .stButton>button {
        background-color: #4B0082;
        color: #FFFFFF;
        font-size: 18px;
        padding: 10px 24px;
        border: none;
        border-radius: 8px;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #9370DB;
        color: #fff;
    }
    .stTextInput>div>input {
        background-color: #F0F0FA;
        color: #2D2A32;
        border: 1px solid #BBB;
        border-radius: 8px;
    }
    footer {
        text-align: center;
        font-size: 14px;
        color: #888;
        margin-top: 30px;
    }
    .stImage>img {
        border: 2px solid #DDD;
        border-radius: 8px;
   
