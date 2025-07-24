import streamlit as st
import re
from openai import OpenAI

# Inicializa o cliente OpenAI com chave segura do Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Configuração da página
st.set_page_config(
    page_title="Minha Conversa com Jesus",
    page_icon="✝️",
    layout="centered",
)

# CSS para interface moderna, colorida e responsiva
st.markdown(
    """
    <style>
    /* Fundo degradê suave */
    body {
        background: linear-gradient(135deg, #f8f9fa, #e0f7fa);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #34495e;
        margin: 0;
        padding: 0;
    }
    /* Container principal */
    .container {
        max-width: 720px;
        background: white;
        margin: 3rem auto 4rem;
        padding: 2.5rem 3rem;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
    }
    /* Título principal */
    h1 {
        font-size: 3.2rem;
        font-weight: 900;
        color: #00796b;
        text-align: center;
        margin-bottom: 0.3rem;
        letter-spacing: 2px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.1);
    }
    /* Subtítulo */
    .subtitle {
        font-size: 1.5rem;
        color: #004d40;
        text-align: center;
        margin-bottom: 2.5rem;
        font-weight: 600;
    }
    /* Caixa do input */
    .stTextInput > div > div > input {
        font-size: 1.15rem;
        padding: 14px 18px;
        border: 2px solid #00796b;
        border-radius: 12px;
        transition: border-color 0.3s ease;
    }
    .stTextInput > div > div > input:focus {
        outline: none;
        border-color: #004d40;
        box-shadow: 0 0 6px #004d40aa;
    }
    /* Botão customizado */
    button[kind="primary"] {
        background-color: #00796b !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
        padding: 0.75rem 2.5rem !important;
        border-radius: 15px !i
