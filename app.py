import streamlit as st
import mercadopago
import openai  # Você pode usar outra API se preferir

# =================== CONFIGURAÇÕES ======================
ACCESS_TOKEN = "APP_USR-9f409612-b346-4437-a1d7-33589ad29133"
PLANO_ID = "dadca597a91f47be81a6133103eacfa5"
OPENAI_API_KEY = "sua-openai-key"  # Insira aqui sua chave da OpenAI
openai.api_key = OPENAI_API_KEY

# =========== TEMA VISUAL PROFISSIONAL ===============
st.set_page_config(
    page_title="Assinatura - Minha Conversa com Jesus",
    page_icon="🙏",
    layout="centered",
    initial_sidebar_state="auto"
)

# Customização CSS
st.markdown("""
    <style>
    body, .main {
        background: linear-gradient(120deg, #f7fafc 0%, #c9e6ff 100%);
    }
    .stTextInput>div>div>input {
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

Para acessar o conteúdo completo, faça sua assinatura:
""")

# Coleta o e-mail do usuário
email = st.text_input("📧 Digite seu e-mail:")

if st.button("📝 Assinar Agora") and email:
    try:
        # Cria a assinatura no Mercado Pago
        sdk = mercadopago.SDK(ACCESS_TOKEN)
        assinatura = sdk.preapproval().create({
            "preapproval_plan_id": PLANO_ID,
            "payer_email": email,
            "back_url": "https://seusite.com/obrigado",
            "notification_url": "https://seusite.com/webhook"
        })

        init_point = assinatura.get('response', {}).get('init_point')
        if init_point:
            st.success("✅ Pronto! Clique no link abaixo para finalizar:")
            st.markdown(f"[Ir para o Pagamento]({init_point})", unsafe_allow_html=True)
        else:
            st.error("❌ Ocorreu um erro ao gerar o link de pagamento.")
            st.info(f"Detalhes da resposta do Mercado Pago: {assinatura.get('response')}")
    except Exception as e:
        st.error(f"❌ Ocorreu um erro: {str(e)}")
        st.info("Por favor, tente novamente ou entre em contato com nosso suporte.")

# ============= NOVA SESSÃO: Conselhos de Jesus =================
st.markdown("---")
st.header("Veja os conselhos de Jesus para você")

user_question = st.text_area(
    "Digite sua dúvida, angústia ou peça um conselho:",
    placeholder="Exemplo: Estou triste, preciso de forças. Ou: Jesus, como posso ser mais paciente?"
)

if st.button("🙌 Ouvir conselho de Jesus"):
    if user_question.strip():
        with st.spinner("Jesus está pensando na melhor resposta para você..."):
            # Chamada à OpenAI (ChatGPT) para resposta em linguagem atual e primeira pessoa
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

# ============= FINAL ================
st.caption("Desenvolvido com carinho e tecnologia para você. © 2024 Minha Conversa com Jesus")
