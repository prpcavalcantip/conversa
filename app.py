import streamlit as st
import openai
import os
import datetime
import requests

# Chaves e tokens
openai.api_key = st.secrets["OPENAI_API_KEY"]
ACCESS_TOKEN = st.secrets["MP_ACCESS_TOKEN"]  # Token seguro

# ID do plano já criado no Mercado Pago
PLAN_ID = "54796041"

# Função para verificar assinatura
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

# Função para gerar link de checkout com plano fixo
def gerar_link_checkout(email):
    url = "https://api.mercadopago.com/preapproval"  # Assinatura recorrente
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "preapproval_plan_id": PLAN_ID,
        "payer_email": email,
        "back_url": "https://conversa-pcstpleylurpnhtwgamfkb.streamlit.app/",
        "reason": "Assinatura anual - Minha Conversa com Jesus"
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in (200, 201):
            return response.json()["init_point"]
        else:
            st.error(f"Erro ao gerar link de checkout: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error("Erro na requisição de checkout: " + str(e))
        return None

# Função para salvar histórico
def salvar_historico(usuario, mensagem):
    filename = f"historico_{usuario}.txt"
    with open(filename, "a") as f:
        f.write(f"{datetime.datetime.now().isoformat()} - {mensagem}\n")

# Função para carregar histórico
def carregar_historico(usuario):
    filename = f"historico_{usuario}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read()
    return ""

# Função para gerar mensagem
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

# Formulário de login
def login_form():
    st.markdown("""
        <div style='text-align:center; margin-bottom:20px;'>
            <h2>Assine para acessar o app</h2>
        </div>
    """, unsafe_allow_html=True)

    email = st.text_input("Digite seu e-mail para verificar ou criar sua assinatura:")

    if email:
        checkout_url = gerar_link_checkout(email)
        if checkout_url:
            st.markdown(f"<div style='text-align:center; margin-bottom:20px;'><a href='{checkout_url}' target='_blank'><button style='background-color:#007bff; color:white; padding:12px 24px; font-size:16px; border:none; border-radius:8px;'>Assinar agora</button></a></div>", unsafe_allow_html=True)

    st.divider()
    st.subheader("Login")
    if st.button("Entrar"):
        if verificar_assinatura_por_email(email):
            st.session_state["usuario_logado"] = email
            st.success("Assinatura verificada. Bem-vindo!")
        else:
            st.error("Assinatura não encontrada. Assine para acessar.")

# Interface principal do app
def app():
    st.title("🙏 Minha Conversa com Jesus")

    if "usuario_logado" not in st.session_state:
        login_form()
        return

    usuario = st.session_state["usuario_logado"]
    mensagem_usuario = st.text_area("Como você está se sentindo hoje?")
    if st.button("Gerar devocional"):
        resposta = gerar_mensagem(mensagem_usuario)
        st.write("**Resposta de Jesus:**")
        st.write(resposta)
        salvar_historico(usuario, f"Você: {mensagem_usuario}\nJesus: {resposta}")

    st.subheader("Histórico")
    historico = carregar_historico(usuario)
    st.text_area("", value=historico, height=200)

if __name__ == "__main__":
    app()
