import streamlit as st
import openai

# Pegando a chave OpenAI dos secrets do Streamlit Cloud
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

# =========== TEMA VISUAL PROFISSIONAL ===============
st.set_page_config(
    page_title="Minha Conversa com Jesus",
    page_icon="🙏",
    layout="centered",
)

# Customização CSS
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

# =================== APP PRINCIPAL ====================
st.title("🙏 Minha Conversa com Jesus")

st.markdown("""
Bem-vindo ao aplicativo **Minha Conversa com Jesus**!

Aqui você pode pedir conselhos e orientações de Jesus para sua vida.
""")

# ============= SESSÃO: Conselhos de Jesus =================
st.markdown("---")
st.header("Veja os conselhos de Jesus para você")

user_question = st.text_area(
    "Digite sua dúvida, angústia ou peça um conselho:",
    placeholder="Exemplo: Estou triste, preciso de forças. Ou: Jesus, como posso ser mais paciente?"
)

if st.button("🙌 Ouvir conselho de Jesus"):
    if user_question.strip():
        with st.spinner("Jesus está pensando na melhor resposta para você..."):
            prompt = (
                "Responda como se fosse Jesus, em primeira pessoa, usando linguagem atual, "
                "com acolhimento, empatia e sabedoria. Não cite versículos, apenas fale como Jesus falaria hoje, "
                "com conselhos amorosos. Pergunta do usuário: "
                f"{user_question.strip()}"
            )
            try:
                resposta = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Você é Jesus, responde em primeira pessoa, com acolhimento e empatia, em linguagem atual."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=250,
                    temperature=0.9
                )
                conselho = resposta.choices[0].message.content.strip()
                st.success(f"💬 Jesus responde:\n\n{conselho}")
            except Exception as e:
                st.error("❌ Não foi possível obter a resposta agora.")
                st.info(f"Erro técnico: {str(e)}")
    else:
        st.warning("Por favor, escreva sua dúvida ou pedido de conselho acima.")

# ============= RODAPÉ =================
st.markdown("---")
st.write("Dúvidas? Entre em contato: contato@seusite.com")
st.caption("Desenvolvido com carinho e tecnologia para você. © 2024 Minha Conversa com Jesus")
