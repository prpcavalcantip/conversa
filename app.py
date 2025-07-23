import streamlit as st
import openai
import os
import datetime
import requests

# Chaves e tokens
openai.api_key = st.secrets["OPENAI_API_KEY"]
ACCESS_TOKEN = "SUA_CHAVE_DE_ACESSO_DO_MERCADO_PAGO"
LINK_ASSINATURA = "https://www.mercadopago.com.br/subscriptions"

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
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    st.markdown(f"<a href='{LINK_ASSINATURA}' target='_blank'><button style='background-color:#28a745; color:white; padding:12px 24px; font-size:16px; border:none; border-radius:8px;'>💖 Assinar agora</button></a>", unsafe_allow_html=True)
    st.markdown("</div><br>", unsafe_allow_html=True)

    with st.container():
        st.markdown("<div style='background-color:#f0f2f6; padding: 20px; border-radius: 10px;'>", unsafe_allow_html=True)
        st.subheader("🔐 Acesso ao devocional")
        email = st.text_input("Digite seu e-mail para verificar sua assinatura:")
        if st.button("Entrar"):
            if verificar_assinatura_por_email(email):
                st.session_state["usuario_logado"] = email
                st.success("Assinatura verificada. Bem-vindo!")
            else:
                st.error("Assinatura não encontrada. Assine para acessar.")

        st.markdown("<br><div style='text-align:center;'>", unsafe_allow_html=True)
        st.markdown(f"<a href='{LINK_ASSINATURA}' target='_blank'><button style='background-color:#007bff; color:white; padding:10px 20px; font-size:14px; border:none; border-radius:5px;'>Assinar agora</button></a>", unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

# Interface principal do app
def app():
    st.markdown("""
        <div style='text-align: center; padding: 10px;'>
            <h1 style='color:#2c3e50;'>🙏 Minha Conversa com Jesus</h1>
            <p style='color:#7f8c8d;'>Receba uma resposta devocional baseada nas palavras de Jesus.</p>
        </div>
    """, unsafe_allow_html=True)

    if "usuario_logado" not in st.session_state:
        login_form()
        return

    usuario = st.session_state["usuario_logado"]
    mensagem_usuario = st.text_area("Como você está se sentindo hoje?")
    if st.button("Gerar devocional"):
        resposta = gerar_mensagem(mensagem_usuario)
        st.write("**📜 Resposta de Jesus:**")
        st.markdown(f"<div style='background-color:#eaf2f8; padding: 15px; border-radius: 10px;'>{resposta}</div>", unsafe_allow_html=True)
        salvar_historico(usuario, f"Você: {mensagem_usuario}\nJesus: {resposta}")

    st.subheader("🕘 Seu histórico de conversas")
    historico = carregar_historico(usuario)
    st.text_area("", value=historico, height=200)

if __name__ == "__main__":
    app()
