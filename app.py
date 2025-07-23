import streamlit as st
import datetime
import re
import requests

# -------------- CONFIGURAÇÃO DA PÁGINA --------------
st.set_page_config(
    page_title="Minha Conversa com Jesus",
    layout="centered",
    page_icon="✝️"
)

# -------------- CONFIG MERCADO PAGO --------------
ACCESS_TOKEN = "SEU_ACCESS_TOKEN_AQUI"  # Substitua pelo seu token
LINK_ASSINATURA = "https://mpago.la/2g1Abc"  # Substitua pelo seu link real de assinatura

# -------------- FUNÇÃO PARA VERIFICAR ASSINATURA --------------
def verificar_assinatura_por_email(email):
    url = "https://api.mercadopago.com/preapproval/search"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    params = {"q": email}
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            results = response.json().get("results", [])
            for assinatura in results:
                if assinatura["payer_email"] == email and assinatura["status"] == "authorized":
                    return True
        return False
    except Exception as e:
        st.error("Erro ao verificar assinatura: " + str(e))
        return False

# -------------- CSS PERSONALIZADO --------------
st.markdown("""<style>body {background-color: #e9f2fa !important;} ...</style>""", unsafe_allow_html=True)

# -------------- MENSAGEM DE BOAS-VINDAS --------------
st.markdown("""<div style='text-align: center; margin-top: 20px;'>...</div>""", unsafe_allow_html=True)

st.info("Em caso de dúvidas, fale com nosso suporte pelo WhatsApp:")
st.markdown("<a href='https://wa.me/5581998311898'>81 99831-1898</a>", unsafe_allow_html=True)

st.markdown("---")

# -------------- AUTENTICAÇÃO COM API DO MERCADO PAGO --------------
if "usuario_logado" not in st.session_state:
    st.session_state["usuario_logado"] = None

def login_form():
    st.markdown("<div class='title-div'><h3 style='text-align:center;'>Área de Login</h3></div>", unsafe_allow_html=True)
    email = st.text_input("E-mail")
    if st.button("Entrar"):
        if verificar_assinatura_por_email(email):
            st.session_state["usuario_logado"] = email
            st.success("Assinatura verificada. Bem-vindo!")
        else:
            st.error("Assinatura não encontrada. Assine para acessar.")
            st.markdown(f"<a href='{LINK_ASSINATURA}' target='_blank'><button>Assinar agora</button></a>", unsafe_allow_html=True)

if not st.session_state["usuario_logado"]:
    login_form()
    st.stop()

# -------------- ÁREA EXCLUSIVA PARA USUÁRIOS LOGADOS --------------
st.markdown("<div class='title-div'><h1 style='text-align: center;'>Minha Conversa com Jesus</h1></div>", unsafe_allow_html=True)
st.markdown("<div class='input-div'>Como você está se sentindo hoje?</div>", unsafe_allow_html=True)
sentimento = st.text_input("", max_chars=120)

def formatar_negrito(texto):
    return re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', texto)

def formatar_sugestoes(texto):
    linhas = texto.split('\n')
    novas_linhas = []
    for linha in linhas:
        if linha.strip().startswith('•'):
            novas_linhas.append(f"<div class='suggestion'>{linha.strip()}</div>")
        else:
            novas_linhas.append(linha)
    return "\n".join(novas_linhas)

def gerar_devocional(sentimento):
    return f"""**Palavra de Jesus:**  \n\"Vinde a mim...\" (Mateus 11:28)\n\n**Reflexão:**  \n...\n\n**Oração:**  \n...\n\n**Sugestões práticas:**  \n• Separe cinco minutos...  \n• Escreva uma mensagem..."""

def salvar_historico(email, sentimento, devocional):
    try:
        with open(f"historico_{email}.txt", "a", encoding="utf-8") as f:
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            f.write(f"\n---\n{data}\nSentimento: {sentimento}\n{devocional}\n")
    except:
        st.warning("Não foi possível salvar o histórico.")

if st.button("Gerar Devocional") and sentimento:
    with st.spinner('Gerando seu devocional...'):
        devocional = gerar_devocional(sentimento)
        devocional_formatado = formatar_sugestoes(formatar_negrito(devocional))
        st.markdown(f"<div class='custom-card'>{devocional_formatado.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)
        salvar_historico(st.session_state["usuario_logado"], sentimento, devocional)

def exibir_historico(email):
    try:
        with open(f"historico_{email}.txt", "r", encoding="utf-8") as f:
            blocos = f.read().split("---")
            st.markdown("<h4 style='color:#205081'>Histórico</h4>", unsafe_allow_html=True)
            for bloco in reversed(blocos[-5:]):
                if bloco.strip():
                    st.markdown(f"<div class='historico-card'>{bloco.strip().replace(chr(10),'<br>')}</div>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.info("Nenhum histórico encontrado.")

if st.checkbox("Ver meu histórico"):
    exibir_historico(st.session_state["usuario_logado"])

st.markdown("<div style='text-align: center;'>© 2025 Minha Conversa com Jesus</div>", unsafe_allow_html=True)



    
