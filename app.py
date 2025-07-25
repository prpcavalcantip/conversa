import streamlit as st
import os
from PIL import Image
from openai import OpenAI

# Inicializar cliente OpenAI com a chave do Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Layout e estilo
st.set_page_config(page_title="Minha Conversa com Jesus", page_icon="🕊️", layout="centered")
st.markdown("""
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
