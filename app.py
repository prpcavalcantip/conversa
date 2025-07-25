import streamlit as st
import openai

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
client = openai.OpenAI(api_key=OPENAI_API_KEY)

st.set_page_config(
    page_title="Minha Conversa com Jesus",
    page_icon="🙏",
    layout="centered",
)

st.markdown("""
    <style>
    body, .main {
        background: linear-gradient(120deg, #f7fafc 0%, #c9e6ff 100%);
    }
    .stTextInput>div>div>input, .stTextArea textarea {
        border-radius: 6px;
        border: 1.5px solid #4682b4;
        background: #f0f8ff;
        color: #222;
        font-size: 18px;
        padding: 8px;
    }
    .stButton>button, .stButton>button:focus {
        background-color: #4682b4 !important;
        color: #fff !important;
        border-radius: 6px;
        padding: 8px 36px;
        font-weight: bold;
        border: none;
        font-size: 18px;
        cursor: pointer;
        box-shadow: 0px 2px 8px #4682b41a;
    }
    .stButton>button:hover {
        background-color: #315c7d !important;
    }
    .stAlert, .stSuccess, .stError {
        border-radius: 6px;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #315c7d;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🙏 Minha Conversa com Jesus")

st.markdown("""
Bem-vindo ao aplicativo **Minha Conversa com Jesus**!

Aqui você pode pedir orientações para sua vida e receber um devocional e um conselho de Jesus, baseados no seu pedido.
""")

st.markdown("---")

sentimento_user = st.text_area(
    "Como estou me sentindo hoje:",
    placeholder="Exemplo: Estou ansioso, busco paz interior. Sinto gratidão. Estou triste e preciso de forças. Quero ser mais paciente..."
)

if st.button("✨ Gerar Devocional e Conselho de Jesus"):
    if sentimento_user.strip():
        with st.spinner("Gerando devocional e conselho de Jesus para você..."):
            prompt_devocional = (
                f"Crie uma devocional cristã sobre '{sentimento_user.strip()}'. "
                "Divida em três partes: "
                "1) Texto para meditação (reflexivo, acolhedor, linguagem atual, sem versículos), "
                "2) Oração (curta, profunda, atual), "
                "3) Práticas para vida diária (sugestões simples e concretas para viver esse tema)."
            )
            prompt_jesus = (
                f"Responda como se fosse Jesus, em primeira pessoa, usando linguagem atual, "
                f"com acolhimento, empatia e sabedoria, sobre: '{sentimento_user.strip()}'. "
                "Não cite versículos, apenas fale como Jesus falaria hoje, com conselhos amorosos."
            )
            try:
                resposta_devocional = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Você é um pastor cristão, acolhedor, reflexivo, atual, simples e prático."},
                        {"role": "user", "content": prompt_devocional}
                    ],
                    max_tokens=600,
                    temperature=0.85
                )
                texto_devocional = resposta_devocional.choices[0].message.content.strip()

                resposta_jesus = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Você é Jesus, responde em primeira pessoa, com acolhimento e empatia, em linguagem atual."},
                        {"role": "user", "content": prompt_jesus}
                    ],
                    max_tokens=250,
                    temperature=0.9
                )
                texto_jesus = resposta_jesus.choices[0].message.content.strip()

                st.success(f"🌅 **Devocional:**\n\n{texto_devocional}")
                st.success(f"💬 **Conselho de Jesus:**\n\n{texto_jesus}")

            except Exception as e:
                st.error("❌ Não foi possível obter a resposta agora.")
                st.info(f"Erro técnico: {str(e)}")
    else:
        st.warning("Por favor, escreva como está se sentindo hoje.")

# MENSAGEM FINAL DE GRATUIDADE E COMPARTILHAMENTO
st.markdown(
    """
    <div style="margin:32px 0 16px 0; padding:18px; background:#e6f7fa; border-radius:8px; border:1px solid #a7d8de;">
        <strong>Esse aplicativo será sempre grátis.</strong><br>
        Se você for tocado por Deus, compartilhe este app com quem está precisando.<br>
        Também, se desejar, você pode fazer uma oferta de qualquer valor para ajudar o ministério.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown(
    '<a href="https://wa.me/5581998311898" target="_blank">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="28" style="vertical-align:middle;margin-right:12px"/>'
    '<span style="font-size:18px;vertical-align:middle;">Fale no WhatsApp: <strong>81998311898</strong></span>'
    '</a>',
    unsafe_allow_html=True
)
st.caption("Desenvolvido com carinho e tecnologia para você. © 2024 Minha Conversa com Jesus")
