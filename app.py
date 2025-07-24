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
        border-radius: 15px !important;
        box-shadow: 0 6px 20px rgba(0,121,107,0.5) !important;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
    }
    button[kind="primary"]:hover {
        background-color: #004d40 !important;
        box-shadow: 0 10px 30px rgba(0,77,64,0.7) !important;
        cursor: pointer;
    }
    /* Caixa do devocional */
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
    }
    /* Rodapé */
    footer {
        text-align: center;
        color: #00796b;
        font-size: 0.95rem;
        margin-bottom: 2rem;
        font-weight: 600;
    }
    /* Links no rodapé */
    footer a {
        color: #004d40;
        text-decoration: none;
        font-weight: 700;
    }
    footer a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Container para centralizar conteúdo
st.markdown('<div class="container">', unsafe_allow_html=True)

# Título e subtítulo
st.markdown("<h1>Minha Conversa com Jesus</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">Como você está se sentindo hoje? Compartilhe e receba um devocional especial.</p>', unsafe_allow_html=True)

# Campo de entrada do sentimento
feeling = st.text_input(
    label="Descreva em poucas palavras seu estado emocional:",
    max_chars=120,
    placeholder="Ex: me sinto ansioso, cansado e desmotivado",
    key="feeling_input",
)

# Função para converter **texto** em <strong>texto</strong>
def formatar_negrito(texto):
    return re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', texto)

# Função para gerar devocional
def gerar_devocional(sentimento):
    prompt_template = """
Você é um assistente espiritual cristão muito acolhedor e profundo. Quando alguém compartilha seu sentimento, responda com um devocional especial, estruturado assim:

1. **Palavra de Jesus:** Um versículo dito por Jesus nos Evangelhos relacionado ao sentimento: "{sentimento}". Cite o livro e versículo.
2. **Reflexão:** Uma reflexão profunda, de 3 a 4 parágrafos, mostrando como Jesus consola, fortalece e guia em situações como essa.
3. **Oração:** Uma oração personalizada, convidando Jesus para confortar e transformar o coração da pessoa.
4. **Práticas diárias:** Três sugestões práticas, simples e efetivas para viver essa Palavra hoje e fortalecer a fé.

Use uma linguagem clara, amorosa e inspiradora, escreva em português, e formate o texto com títulos em negrito **como neste exemplo**.

Agora, crie o devocional para o sentimento: "{sentimento}".
"""
    prompt = prompt_template.format(sentimento=sentimento)

    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=900,
        temperature=0.75,
    )
    return resposta.choices[0].message.content.strip()

# Botão para gerar devocional
if st.button("Gerar Devocional") and feeling:
    with st.spinner("Gerando seu devocional..."):
        try:
            devocional = gerar_devocional(feeling)
            devocional_formatado = formatar_negrito(devocional)
            st.markdown(f'<div class="devotional-box">{devocional_formatado}</div>', unsafe_allow_html=True)
            st.success("Devocional gerado com sucesso! 🙏")
        except Exception as e:
            st.error("Erro ao gerar o devocional. Verifique sua chave da OpenAI ou tente novamente.")
            st.exception(e)

# Fecha container
st.markdown('</div>', unsafe_allow_html=True)

# Rodapé
st.markdown(
    """
    <footer>
        © 2025 Minha Conversa com Jesus | Feito com ❤️ em Streamlit
    </footer>
    """,
    unsafe_allow_html=True,
)
