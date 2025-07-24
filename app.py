import streamlit as st
import re
from openai import OpenAI

# Inicializa cliente OpenAI com chave do secrets.toml
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Configurações da página
st.set_page_config(page_title="Minha Conversa com Jesus", page_icon="✝️", layout="centered")

# CSS para melhorar a interface
st.markdown(
    """
    <style>
    /* Fundo degradê */
    body {
        background: linear-gradient(135deg, #e0f7fa, #b2dfdb);
        margin: 0;
        padding: 0 1rem 3rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Título centralizado e estilizado */
    h1 {
        text-align: center;
        color: #00796b;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
        font-weight: 900;
        font-size: 3rem;
        letter-spacing: 2px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.1);
    }

    /* Subtítulo */
    .subtitle {
        text-align: center;
        color: #004d40;
        font-size: 1.25rem;
        margin-bottom: 2rem;
        font-weight: 600;
    }

    /* Input text estilizado */
    div.stTextInput > div > input {
        font-size: 1.15rem !important;
        padding: 14px 18px !important;
        border-radius: 12px !important;
        border: 2px solid #00796b !important;
        box-shadow: none !important;
        transition: border-color 0.3s ease;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }
    div.stTextInput > div > input:focus {
        border-color: #004d40 !important;
        box-shadow: 0 0 8px #004d40aa !important;
        outline: none !important;
    }

    /* Botão estilizado */
    div.stButton > button {
        background-color: #009688;
        color: white;
        font-weight: 800;
        font-size: 1.2rem;
        padding: 0.9rem 2.5rem;
        border-radius: 30px;
        border: none;
        box-shadow: 0 8px 25px rgba(0, 150, 136, 0.6);
        cursor: pointer;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        width: 100%;
        max-width: 300px;
        margin-left: auto;
        margin-right: auto;
        display: block;
    }
    div.stButton > button:hover {
        background-color: #00796b;
        box-shadow: 0 12px 40px rgba(0, 121, 107, 0.85);
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
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }

    /* Rodapé */
    footer {
        text-align: center;
        color: #004d40;
        margin-top: 4rem;
        font-size: 1rem;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título e subtítulo
st.markdown("<h1>Minha Conversa com Jesus</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">Como você está se sentindo hoje? Compartilhe e receba um devocional especial.</p>', unsafe_allow_html=True)

# Input sentimento
feeling = st.text_input(
    label="Descreva em poucas palavras seu estado emocional:",
    max_chars=120,
    placeholder="Ex: me sinto ansioso, cansado e desmotivado",
)

def formatar_negrito(texto):
    return re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', texto)

def gerar_devocional(sentimento):
    prompt = f"""
Você é um assistente espiritual cristão muito acolhedor e profundo. Quando alguém compartilha seu sentimento, responda com um devocional especial e mais aprofundado, estruturado assim:

1. **Palavra de Jesus:** Um versículo dito por Jesus nos Evangelhos relacionado ao sentimento: "{sentimento}". Cite o livro e versículo.
2. **Reflexão:** Uma reflexão bem profunda, de 4 a 5 parágrafos, mostrando como Jesus consola, fortalece e guia em situações assim, trazendo esperança e transformação.
3. **Oração:** Uma oração calorosa e personalizada, convidando Jesus para restaurar, confortar e renovar a fé da pessoa.
4. **Práticas diárias:** Três sugestões práticas, simples e eficazes para viver essa Palavra hoje e fortalecer a fé no dia a dia.

Use linguagem clara, amorosa e inspiradora, escreva em português, e formate o texto com títulos em negrito **como neste exemplo**.

Agora, crie o devocional para o sentimento: "{sentimento}".
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.75,
    )
    return response.choices[0].message.content.strip()

if st.button("Gerar Devocional") and feeling:
    with st.spinner("Gerando seu devocional..."):
        try:
            devocional = gerar_devocional(feeling)
            devocional_formatado = formatar_negrito(devocional)
            st.markdown(
                f'<div class="devotional-box">{devocional_formatado}</div>',
                unsafe_allow_html=True,
            )
            st.success("Devocional gerado com sucesso! 🙏")
        except Exception as e:
            st.error("Erro ao gerar o devocional. Verifique sua chave da OpenAI ou tente novamente.")
            st.exception(e)

st.markdown(
    """
    <footer>
        © 2025 Minha Conversa com Jesus | Feito com ❤️ pelo Pastor PAULO
    </footer>
    """,
    unsafe_allow_html=True,
)
