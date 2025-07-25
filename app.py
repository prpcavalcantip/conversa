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
    }
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# Título
st.markdown("<div class='titulo'>🕊️ Minha Conversa com Jesus</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Como você está se sentindo hoje?</div>", unsafe_allow_html=True)

# Entrada do usuário
feeling = st.text_input("Descreva em poucas palavras seu estado emocional:")

# Função para gerar devocional
def gerar_devocional(sentimento):
    if not sentimento.strip():
        return "Por favor, descreva seu estado emocional para gerar o devocional."
    
    prompt = f"""
    Você é um devocionalista cristão. Crie uma devocional profunda com base nas palavras de Jesus, considerando o sentimento descrito: \"{sentimento}\". 
    A devocional deve conter:
    - Um versículo bíblico dito por Jesus;
    - Uma breve reflexão sobre o sentimento à luz da fé cristã;
    - Uma oração inspiradora;
    - Duas sugestões de práticas diárias para fortalecer a fé.
    Seja acolhedor, pastoral e profundamente bíblico.
    """
    try:
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um devocionalista cristão, acolhedor e bíblico."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return resposta.choices[0].message.content
    except Exception as e:
        return f"Erro ao gerar devocional: {str(e)}"

# Botão para gerar devocional
if st.button("Gerar Devocional"):
    if feeling:
        with st.spinner("Gerando seu devocional..."):
            devocional = gerar_devocional(feeling)
            st.markdown("<div class='caixa'>", unsafe_allow_html=True)
            st.markdown(devocional, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("Por favor, insira seu estado emocional antes de gerar o devocional.")

# Rodapé
st.markdown("<footer>Desenvolvido com ❤️ para fortalecer sua fé</footer>", unsafe_allow_html=True)
