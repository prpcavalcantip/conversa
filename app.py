import streamlit as st
import datetime
import re

# -------------- CONFIGURAÇÃO DA PÁGINA --------------
st.set_page_config(
    page_title="Minha Conversa com Jesus",
    layout="centered",
    page_icon="✝️"
)

# -------------- CSS PERSONALIZADO --------------
st.markdown("""
    <style>
        body {
            background-color: #e9f2fa !important;
        }
        .main .block-container {
            background: #e9f2fa !important;
            color: #24292f;
        }
        .title-div {
            background: #fff;
            border-radius: 18px;
            padding: 18px 10px 12px 10px;
            margin-bottom: 18px;
            border: 1.5px solid #b3c6e0;
            box-shadow: 0 2px 8px rgba(32,80,129,0.08);
        }
        .input-div {
            text-align: center;
            font-size: 1.25em;
            margin-bottom: 20px;
            color: #205081;
            font-weight: 500;
        }
        .custom-card {
            background-color: #fff;
            border: 1.5px solid #b3c6e0;
            border-radius: 16px;
            padding: 24px;
            margin-top: 24px;
            text-align: left;
            max-width: 540px;
            margin-left: auto;
            margin-right: auto;
            font-size: 1.13em;
            line-height: 1.7;
            color: #24292f;
            box-shadow: 0 2px 10px rgba(32,80,129,0.06);
        }
        .stTextInput > div > div > input {
            font-size: 1.1em;
        }
        .stButton button {
            color: #fff;
            background: linear-gradient(90deg,#205081 70%,#3e82c4 100%);
            border: 0px;
            border-radius: 8px;
            padding: 0.6em 1.5em;
            font-size: 1.1em;
            font-weight: 600;
            margin-bottom: 10px;
            transition: 0.2s;
        }
        .stButton button:hover {
            filter: brightness(1.08);
            border: 1.5px solid #205081;
        }
        strong {
            color: #205081;
            font-weight: 700;
        }
        .suggestion {
            background: #f0f6fb;
            border-left: 4px solid #205081;
            border-radius: 7px;
            padding: 7px 15px 7px 14px;
            margin: 6px 0 0 0;
            font-size: 1em;
        }
        .whatsapp-link {
            color: #25d366 !important;
            text-decoration: none;
            font-weight: 700;
        }
        .historico-card {
            background: #fff;
            border: 1px solid #b3c6e0;
            border-radius: 10px;
            margin-bottom: 18px;
            padding: 10px 18px;
            color: #205081;
            font-size: 1em;
        }
    </style>
""", unsafe_allow_html=True)

# -------------- MENSAGEM DE BOAS-VINDAS --------------
st.markdown("""
<div style='text-align: center; margin-top: 20px; margin-bottom: 10px;'>
    <h2 style='color: #205081; font-family: Arial, sans-serif;'>Bem-vindo ao Minha Conversa com Jesus!</h2>
    <p style='font-size: 1.1em; color: #333; margin-bottom: 30px;'>
        É uma alegria ter você aqui.<br>
        Viva um tempo de inspiração, reflexão e conexão com a Palavra de Jesus.<br>
    </p>
</div>
""", unsafe_allow_html=True)

# SUPORTE WHATSAPP
st.info(
    "Em caso de dúvidas, fale com nosso suporte pelo WhatsApp:"
)
st.markdown(
    "📱 <a href='https://wa.me/5581998311898' class='whatsapp-link' target='_blank'>81 99831-1898</a>",
    unsafe_allow_html=True
)

st.markdown("---")

# -------------- SIMULAÇÃO DE BANCO DE DADOS DE USUÁRIOS --------------
USUARIOS = {
    "usuario@email.com": "senha123",
    "demo@email.com": "demo123",
    # Adicione mais usuários conforme necessário.
}

# -------------- AUTENTICAÇÃO --------------
if "usuario_logado" not in st.session_state:
    st.session_state["usuario_logado"] = None

def login_form():
    st.markdown(
        "<div class='title-div'><h3 style='text-align:center; color:#205081;'>Área de Login</h3></div>",
        unsafe_allow_html=True
    )
    email = st.text_input("E-mail")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if email in USUARIOS and USUARIOS[email] == senha:
            st.session_state["usuario_logado"] = email
            st.success("Login realizado com sucesso!")
            st.experimental_rerun()
        else:
            st.error("E-mail ou senha incorretos.")

if not st.session_state["usuario_logado"]:
    login_form()
    st.stop()

# -------------- ÁREA EXCLUSIVA PARA USUÁRIOS LOGADOS --------------

# Título
st.markdown("""
<div class='title-div'>
    <h1 style='text-align: center; font-size: 2.0em; margin-bottom: 0; color: #205081;'>
        Minha Conversa com Jesus
    </h1>
</div>
""", unsafe_allow_html=True)

# Entrada do sentimento
st.markdown(
    "<div class='input-div'>Como você está se sentindo hoje?</div>",
    unsafe_allow_html=True
)
sentimento = st.text_input("", max_chars=120)

# Funções auxiliares para formatação
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

# Função para gerar devocional
def gerar_devocional(sentimento):
    # Simulação de resposta da OpenAI (substitua por chamada real se desejar)
    return f"""**Palavra de Jesus:**  
"Vinde a mim, todos os que estais cansados e oprimidos, e eu vos aliviarei." (Mateus 11:28)

**Reflexão:**  
Jesus nos convida a entregar a Ele nossos fardos e preocupações. Por mais difícil que pareça o dia, Sua presença traz consolo e força. Não estamos sozinhos: Ele caminha conosco e conhece cada detalhe do nosso coração.

Mesmo na angústia ou incerteza, lembre-se que você é profundamente amado(a). Permita-se descansar nos braços de Cristo, confiando que Ele cuida de você.

**Oração:**  
Senhor Jesus, entrego meus sentimentos e preocupações em Tuas mãos. Que eu encontre repouso em Ti e renove minhas forças para este dia. Amém.

**Sugestões práticas para o dia:**  
• Separe cinco minutos em silêncio para conversar com Jesus.  
• Escreva uma mensagem de carinho para alguém que você ama."""

def salvar_historico(email, sentimento, devocional):
    try:
        with open(f"historico_{email}.txt", "a", encoding="utf-8") as f:
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            f.write(f"\n---\n{data}\nSentimento: {sentimento}\n{devocional}\n")
    except Exception as e:
        st.warning("Não foi possível salvar o histórico.")

# Botão de geração do devocional
if st.button("Gerar Devocional") and sentimento:
    with st.spinner('Gerando seu devocional...'):
        devocional = gerar_devocional(sentimento)
        devocional_formatado = formatar_negrito(devocional)
        devocional_formatado = formatar_sugestoes(devocional_formatado)
        st.markdown(
            f"<div class='custom-card'>{devocional_formatado.replace(chr(10), '<br>')}</div>",
            unsafe_allow_html=True
        )
        salvar_historico(st.session_state["usuario_logado"], sentimento, devocional)

# Histórico do usuário
def exibir_historico(email):
    try:
        with open(f"historico_{email}.txt", "r", encoding="utf-8") as f:
            blocos = f.read().split("---")
            st.markdown("<br><h4 style='color:#205081'>Seu Histórico de Sentimentos e Devocionais</h4>", unsafe_allow_html=True)
            for bloco in reversed(blocos[-5:]):  # últimos 5
                if bloco.strip():
                    st.markdown(f"<div class='historico-card'>{bloco.strip().replace(chr(10),'<br>')}</div>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.info("Nenhum histórico encontrado ainda.")

if st.checkbox("Ver meu histórico"):
    exibir_historico(st.session_state["usuario_logado"])

# Rodapé
st.markdown(
    "<div style='text-align: center; font-size: 1em; margin-top: 50px; color: #6c757d;'>"
    "© 2025 Minha Conversa com Jesus | Feito com ❤️ pelo Pastor Paulo Cavalcanti"
    "</div>",
    unsafe_allow_html=True
)
    
