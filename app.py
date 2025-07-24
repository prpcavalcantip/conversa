import streamlit as st
import re
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(
    page_title="Minha Conversa com Jesus",
    page_icon="✝️",
    layout="centered",
)

st.markdown(
    """
    <style>
    /* Container principal e estilos gerais */
    body {
        background: linear-gradient(135deg, #f8f9fa, #e0f7fa);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #34495e;
        margin: 0;
        padding: 0;
    }
    .container {
        max-width: 720px;
        background: white;
        margin: 3rem auto 4rem;
        padding: 2.5rem 3rem;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
    }
    h1 {
        font-size: 3.2rem;
        font-weight: 900;
        color: #00796b;
        text-align: center;
        margin-bottom: 0.3rem;
        letter-spacing: 2px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.1);
    }
    .subtitle {
        font-size: 1.5rem;
        color: #004d40;
        text-align: center;
        margin-bottom: 2.5rem;
        font-weight: 600;
    }
    input[type="text"] {
        font-size: 1.15rem;
        padding: 14px 18px;
        border: 2px solid #00796b !important;
        border-radius: 12px !important;
        transition: border-color 0.3s ease;
        width: 100%;
        box-sizing: border-box;
    }
    input[type="text"]:focus {
        outline: none;
        border-color: #004d40 !important;
        box-shadow: 0 0 6px #004d40aa !important;
    }
    /* Esconde o botão original do Streamlit */
    #streamlit-button {
        opacity: 0;
        position: absolute;
        pointer-events: none;
        height: 0;
        width: 0;
    }
    /* Botão fake customizado */
    .custom-button {
        display: inline-block;
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
    }
    .custom-button:hover {
        background-color: #00796b;
        box-shadow: 0 12px 40px rgba(0, 121, 107, 0.85);
    }
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
    footer {
        text-align: center;
        color: #00796b;
        font-size: 0.95rem;
        margin-bottom: 2rem;
        font-weight: 600;
    }
    footer a {
        color: #004d40;
        text-decoration: none;
        font-weight: 700;
    }
    footer a:hover {
        text-decoration: underline;
    }
    </style>

    <script>
    // Função para clicar no botão oculto do Streamlit ao clicar no botão fake
    function triggerStreamlitButton() {
        const btn = document.getElementById("streamlit-button");
        if (btn) {
            btn.click();
        }
    }
    </script>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown("<h1>Minha Conversa com Jesus</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">Como você está se sentindo hoje? Compartilhe e receba um devocional especial.</p>', unsafe_allow_html=True)

feeling = st.text_input(
    label="Descreva em poucas palavras seu estado emocional:",
    max_chars=120,
    placeholder="Ex: me sinto ansioso, cansado e desmotivado",
    key="feeling_input",
)

# Botão "real" invisível
botao_real = st.button("Gerar Devocional", key="btn_real")

# Botão fake estilizado em HTML
st.markdown(
    """
    <div class="custom-button" onclick="triggerStreamlitButton()">
        Gerar Devocional
    </div>
    """,
    unsafe_allow_html=True,
)

# Função para converter **texto** em <strong>texto</strong>
def formatar_negrito(texto):
    return re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', texto)

def gerar_devocional(sentimento):
    prompt_template = """
Você é um assistente espiritual cristão muito acolhedor e profundo. Quando alguém compartilha seu sentimento, responda com um devocional especial e mais aprofundado, estruturado assim:

1. **Palavra de Jesus:** Um versículo dito por Jesus nos Evangelhos relacionado ao sentimento: "{sentimento}". Cite o livro e versículo.
2. **Reflexão:** Uma reflexão bem profunda, de 4 a 5 parágrafos, mostrando como Jesus consola, fortalece e guia em situações assim, trazendo esperança e transformação.
3. **Oração:** Uma oração calorosa e personalizada, convidando Jesus para restaurar, confortar e renovar a fé da pessoa.
4. **Práticas diárias:** Três sugestões práticas, simples e eficazes para viver essa Palavra hoje e fortalecer a fé no dia a dia.

Use linguagem clara, amorosa e inspiradora, escreva em português, e formate o texto com títulos em negrito **como neste exemplo**.

Agora, crie o devocional para o sentimento: "{sentimento}".
"""
    prompt = prompt_template.format(sentimento=sentimento)

    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.75,
    )
    return resposta.choices[0].message.content.strip()

if botao_real and feeling:
    with st.spinner("Gerando seu devocional..."):
        try:
            devocional = gerar_devocional(feeling)
            devocional_formatado = formatar_negrito(devocional)
            st.markdown(f'<div class="devotional-box">{devocional_formatado}</div>', unsafe_allow_html=True)
            st.success("Devocional gerado com sucesso! 🙏")
        except Exception as e:
            st.error("Erro ao gerar o devocional. Verifique sua chave da OpenAI ou tente novamente.")
            st.exception(e)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    """
    <footer>
        © 2025 Minha Conversa com Jesus | Feito com ❤️ em Streamlit
    </footer>
    """,
    unsafe_allow_html=True,
)
