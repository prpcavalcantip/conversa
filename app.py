import streamlit as st
import re
from openai import OpenAI

# Inicializa o cliente OpenAI com a chave segura
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Configuração da página
st.set_page_config(
    page_title="Minha Conversa com Jesus",
    page_icon="✝️",
    layout="centered",
)

# Estilos CSS personalizados para melhorar visual
st.markdown(
    """
    <style>
    body {
        background: #f0f2f6;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #333;
    }
    .title {
        font-size: 3rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-size: 1.4rem;
        color: #34495e;
        margin-bottom: 2rem;
    }
    .input-box {
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    .button {
        background-color: #2980b9;
        color: white;
        font-weight: 600;
        padding: 0.6rem 1.5rem;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        font-size: 1.1rem;
        transition: background-color 0.3s ease;
    }
    .button:hover {
        background-color: #1f618d;
    }
    .devotional-box {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        max-width: 650px;
        margin: 2rem auto 4rem;
        font-size: 1.15rem;
        line-height: 1.6;
        color: #2c3e50;
        white-space: pre-wrap;
    }
    .footer {
        text-align: center;
        color: #7f8c8d;
        margin-top: 4rem;
        margin-bottom: 2rem;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título e subtítulo
st.markdown("<h1 class='title'>Minha Conversa com Jesus</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Como você está se sentindo hoje? Compartilhe e receba um devocional especial.</p>", unsafe_allow_html=True)

# Campo de entrada do sentimento
feeling = st.text_input(
    label="Descreva em poucas palavras seu estado emocional:",
    max_chars=120,
    placeholder="Ex: me sinto ansioso, cansado e desmotivado",
    key="feeling_input",
)

# Função para formatar negrito **texto** em <strong>texto</strong>
def formatar_negrito(texto):
    return re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', texto)

# Função para gerar devocional com oração e práticas
def gerar_devocional(sentimento):
    prompt_template = """
Você é um assistente espiritual cristão muito acolhedor e profundo. Quando alguém compartilha seu sentimento, responda com um devocional especial, estruturado assim:

1. **Palavra de Jesus:** Um versículo ditado por Jesus nos Evangelhos relacionado ao sentimento: "{sentimento}". Cite o livro e versículo.
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
            st.markdown(f"<div class='devotional-box'>{devocional_formatado}</div>", unsafe_allow_html=True)
            st.success("Devocional gerado com sucesso! 🙏")
        except Exception as e:
            st.error("Erro ao gerar o devocional. Verifique sua chave da OpenAI ou tente novamente.")
            st.exception(e)

# Rodapé
st.markdown("<div class='footer'>© 2025 Minha Conversa com Jesus | Feito com ❤️ em Streamlit</div>", unsafe_allow_html=True)
