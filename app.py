import streamlit as st
import re
from openai import OpenAI

# Inicializa cliente OpenAI com chave do secrets.toml
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Configurações da página
st.set_page_config(page_title="Minha Conversa com Jesus", page_icon="✝️", layout="centered")

# CSS e JS para esconder botão original e criar botão customizado
st.markdown(
    """
    <style>
    /* Esconder botão padrão do Streamlit */
    button[kind="primary"] {
        display: none !important;
    }

    /* Botão customizado */
    .custom-button {
        background-color: #009688;
        color: white;
        font-weight: 800;
        font-size: 1.3rem;
        padding: 1rem 3rem;
        border-radius: 30px;
        box-shadow: 0 8px 25px rgba(0, 150, 136, 0.6);
        border: none;
        cursor: pointer;
        user-select: none;
        text-transform: uppercase;
        letter-spacing: 1.1px;
        text-align: center;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        margin-top: 10px;
        display: inline-block;
    }
    .custom-button:hover {
        background-color: #00796b;
        box-shadow: 0 12px 40px rgba(0, 121, 107, 0.85);
    }

    /* Estilo título */
    h1 {
        text-align: center;
        color: #00796b;
        margin-bottom: 1rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 900;
        font-size: 3rem;
        letter-spacing: 2px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.1);
    }

    /* Subtítulo */
    p.subtitle {
        text-align: center;
        font-size: 1.25rem;
        color: #004d40;
        margin-bottom: 2rem;
        font-weight: 600;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Input text */
    input[type="text"] {
        font-size: 1.15rem;
        padding: 14px 18px;
        border: 2px solid #00796b !important;
        border-radius: 12px !important;
        transition: border-color 0.3s ease;
        width: 100%;
        box-sizing: border-box;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin-bottom: 20px;
    }
    input[type="text"]:focus {
        outline: none;
        border-color: #004d40 !important;
        box-shadow: 0 0 6px #004d40aa !important;
    }

    /* Caixa devocional */
    .devotional-box {
        background: #e0f2f1;
        padding: 2rem 2.5rem;
        border-radius: 30px;
        box-shadow: 0 8px 28px rgba(0, 121, 107, 0.15);
        font-size: 1.18rem;
        line-height: 1.7;
        color: #004d40;
        white-space: pre-wrap;
        margin-top: 2.5rem;
        font-weight: 500;
        border: 2px solid #004d40;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Fundo da página */
    body {
        background: linear-gradient(135deg, #f8f9fa, #e0f7fa);
        margin: 0;
        padding: 0 1rem 3rem;
    }
    </style>

    <script>
    // Dispara clique do botão original do Streamlit invisível
    function triggerStreamlitButton() {
        const buttons = window.parent.document.querySelectorAll('button[kind="primary"]');
        if (buttons.length > 0) {
            buttons[0].click();
        }
    }
    </script>
    """,
    unsafe_allow_html=True,
)

# Título e subtítulo
st.markdown("<h1>Minha Conversa com Jesus</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">Como você está se sentindo hoje? Compartilhe e receba um devocional especial.</p>', unsafe_allow_html=True)

# Input do sentimento
feeling = st.text_input(
    label="Descreva em poucas palavras seu estado emocional:",
    max_chars=120,
    placeholder="Ex: me sinto ansioso, cansado e desmotivado",
    key="feeling_input",
)

# Botão original invisível
botao_real = st.button("Gerar Devocional")

# Botão customizado que dispara o clique do botão real
st.markdown(
    """
    <div class="custom-button" onclick="triggerStreamlitButton()">
        Gerar Devocional
    </div>
    """,
    unsafe_allow_html=True,
)

# Função para formatar negrito (convertendo **texto** em <strong>texto</strong>)
def forma
