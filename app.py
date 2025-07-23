import streamlit as st
import openai
import os
import datetime
import requests

# Chaves e tokens
openai.api_key = st.secrets["OPENAI_API_KEY"]
ACCESS_TOKEN = "SUA_CHAVE_DE_ACESSO_DO_MERCADO_PAGO"
PLANO_ID = 54796041

# Link fixo de redirecionamento após assinatura
BACK_URL = "https://seuapp.com/obrigado"  # altere para a URL real do seu app

# Função para gerar link de checkout dinâmico via API Mercado Pago
def gerar_link_checkout(email_cliente):
    url = "https://api.mercadopago.com/preapproval"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "payer_email": email_cliente,
        "preapproval_plan_id": PLANO_ID,
        "back_url": BACK_URL,
        "reason": "Assinatura anual Minha Conversa com Jesus"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        return response.json().get("init_point")
    else:
        st.error(f"Erro ao gerar link de checkout: {response.status_code} - {response.text}")
        return None

# Função para verificar assinatura no Mercado Pago via API
@st.cache_data(ttl=600)
def verificar_assinatura_por_email(email):
    url = "https://api.mercadopago.com/preapproval/search"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    params = {
        "status": "authorized",
        "limit": 100
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            results = response.json().get("results", [])
            for assinatura in results:
                if assinatura.get("payer_email") == email:
                    return True
        return False
    except Exception as e:
        st.error("Erro ao verificar assinatura: " + str(e))
        return False

# Função para salvar histórico
def salvar_historico(usuario, mensagem):
    filename = f"historico_{usuario}.txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now().isoformat()} - {mensagem}\n")

# Função para carregar histórico
def carregar_historico(usuario):
    filename = f"historico_{usuario}.txt"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Função para gerar mensagem devocional com OpenAI
def gerar_mensagem(mensagem_usuario):
    prompt = f"Sou Jesus respondendo a um devocional. Mensagem do usuário: '{mensagem_usuario}'. Minha resposta:"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é Jesus respondendo mensagens devocionais."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Erro ao gerar mensagem: {str(e)}"

# ------------------ INTERFACE ------------------

st.set_page_config(
    page_title="Minha Conversa com Jesus",
    layout="centered",
    page_icon="✝️"
)

st.markdown("<h1 style='text-align: center; color: #205081;'>Minha Conversa com Jesus</h1>", unsafe_allow_html=True)

# -------------- BOTÃO ASSINAR AGORA NO TOPO --------------

st.markdown("### Faça sua assinatura anual para acessar o conteúdo exclusivo")

email_assinatura = st.text_input("Digite seu e-mail para gerar o link de assinatura:")

if st.button("Gerar link para Assinar agora"):
    if email_assinatura and "@" in email_assinatura:
        link_checkout = gerar_link_checkout(email_assinatura)
        if link_checkout:
            st.markdown(f"[Clique aqui para assinar]({link_checkout})", unsafe_allow_html=True)
            st.info("O link abrirá em nova aba. Complete a assinatura para acessar.")
    else:
        st.error("Por favor, insira um e-mail válido.")

st.markdown("---")

# ---------------- LOGIN ----------------

if "usuario_logado" not in st.session_state:
    st.session_state["usuario_logado"] = None

def login_form():
    st.subheader("Área de Login")

    email = st.text_input("Digite seu e-mail para entrar")
    if st.button("Entrar"):
        if verificar_assinatura_por_email(email):
            st.session_state["usuario_logado"] = email
            st.success("Assinatura verificada. Bem-vindo!")
            st.experimental_rerun()
        else:
            st.error("Nenhuma assinatura ativa encontrada para este e-mail. Por favor, assine para acessar.")

if not st.session_state["usuario_logado"]:
    login_form()
    st.stop()

# ---------------- ÁREA EXCLUSIVA PARA USUÁRIOS LOGADOS ----------------

usuario = st.session_state["usuario_logado"]

mensagem_usuario = st.text_area("Como você está se sentindo hoje?")

if st.button("Gerar devocional") and mensagem_usuario:
    resposta = gerar_mensagem(mensagem_usuario)
    st.markdown("**Resposta de Jesus:**")
    st.write(resposta)
    salvar_historico(usuario, f"Você: {mensagem_usuario}\nJesus: {resposta}")

st.subheader("Seu Histórico")
historico = carregar_historico(usuario)
st.text_area("", value=historico, height=200)

# Rodapé
st.markdown(
    "<div style='text-align: center; font-size: 1em; margin-top: 50px; color: #6c757d;'>"
    "© 2025 Minha Conversa com Jesus | Feito com ❤️ pelo Pastor Paulo Cavalcanti"
    "</div>",
    unsafe_allow_html=True
)
