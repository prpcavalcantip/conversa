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
"""
st.markdown(css, unsafe_allow_html=True)

# Título
st.markdown("<div class='titulo'>🕊️ Minha Conversa com Jesus</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Como você está se sentindo hoje?</div>", unsafe_allow_html=True)

# Entrada do usuário
with st.container():
    feeling = st.text_input("Descreva em poucas palavras seu estado emocional:")

# Função para gerar devocional
def gerar_devocional(sentimento):
    if not sentimento.strip():
        return "Por favor, descreva seu estado emocional para gerar o devocional."
    
    prompt = f"""
    Você é um devocionalista cristão. Crie uma devocional profundamente rica e detalhada com base nas palavras de Jesus, considerando o sentimento descrito: \"{sentimento}\". 
    A devocional deve conter:
    - Um versículo bíblico dito por Jesus, diretamente citado dos evangelhos, com referência clara (ex.: Mateus 11:28);
    - Uma reflexão longa, acolhedora e teologicamente profunda sobre o sentimento, conectando-o detalhadamente com os ensinamentos e a vida de Jesus nos evangelhos;
    - Uma oração inspiradora, longa e pessoal, que reflita profundamente o sentimento do usuário e peça orientação divina;
    - Três sugestões específicas e práticas de atividades diárias para fortalecer a fé, adaptadas ao contexto emocional e baseadas nos ensinamentos de Jesus;
    - Uma seção chamada 'Conselhos de Jesus para você', onde Jesus fala diretamente ao usuário em primeira pessoa, chamando-o de 'filho', em linguagem atual, amigável e baseada nos evangelhos (ex.: Mateus, Marcos, Lucas, João), oferecendo conselhos pessoais, práticos e encorajadores para o dia a dia.
    Seja pastoral, profundamente bíblico, sensível ao estado emocional do usuário e evite superficialidade.
    """
    try:
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um devocionalista cristão,
