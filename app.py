import streamlit as st
import os
from PIL import Image
from openai import OpenAI

# Inicializar cliente OpenAI com a chave do Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Layout e estilo
st.set_page_config(page_title="Minha Conversa com Jesus", page_icon="🕊️", layout="centered")
st.markdown("""
    <style>
        /* Fundo principal */
        .stApp {
            background-color: #F5F6F5; /* Branco Nuvem */
        }
        /* Estilo para o título */
        .titulo {
            font-size: 38px;
            font-weight: bold;
            color: #6B4EAA; /* Roxo Espiritual */
            text-align: center;
            margin-top: 20px;
        }
        /* Estilo para o subtítulo */
        .subtitulo {
            font-size: 20px;
            color: #A3BFFA; /* Cinza Suave */
            text-align: center;
            margin-bottom: 30px;
        }
        /* Estilo para caixas de conteúdo */
        .caixa {
            background-color: #F5F6F5; /* Branco Nuvem */
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
            margin-bottom: 30px;
            color: #6B4EAA; /* Roxo Espiritual */
            border: 1px solid #A3BFFA; /* Cinza Suave */
        }
        /* Estilo para botões */
        .stButton>button {
            background-color: #4A90E2; /* Azul Sereno */
            color: #F5F6F5; /* Branco Nuvem */
            font-size: 18px;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #A3BFFA; /* Cinza Suave */
            color: #6B4EAA; /* Roxo Espiritual */
        }
        /* Estilo para entradas de texto */
        .stTextInput>div>input {
            background-color: #F5F6F5; /* Branco Nuvem */
            color: #6B4EAA; /* Roxo Espiritual */
            border: 1px solid #A3BFFA; /* Cinza Suave */
            border-radius: 8px;
        }
        /* Estilo para destaques */
        .highlight {
            color: #F7E4A5; /* Dourado Claro */
            font-weight: bold;
        }
        /* Estilo para o rodapé */
        footer {
            text-align: center;
            font-size: 14px;
            color: #A3BFFA; /* Cinza Suave */
            margin-top: 30px;
        }
        /* Estilo para a imagem do QR Code */
        .stImage>img {
            border: 2px solid #A3BFFA; /* Cinza Suave */
            border-radius: 8px;
        }
        /* Estilo para o código Pix */
        .stCodeBlock {
            background-color: #F5F6F5; /* Branco Nuvem */
            border: 1px solid #A3BFFA; /* Cinza Suave */
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<div class='titulo'>🕊️ Minha Conversa com Jesus</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Como você está se sentindo hoje?</div>", unsafe_allow_html=True)

# Entrada do usuário
with st.container():
    feeling = st.text_input("Descreva em poucas palavras seu estado emocional:")

# Função para gerar devocional
def gerar_devocional(sentimento):
    prompt = f"""
    Você é um devocionalista cristão. Crie uma devocional profunda com base nas palavras de Jesus, considerando o sentimento descrito: \"{sentimento}\". 
    A devocional deve conter:
    - Um versículo bíblico dito por Jesus;
    - Uma breve reflexão sobre o sentimento à luz da fé cristã;
    - Uma oração inspiradora;
    - Duas sugestões de práticas diárias para fortalecer a fé.
    Seja acolhedor, pastoral e profundamente bíblico.
    """

    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um devocionalista cristão."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )
    return resposta.choices[0].message.content

# Função para recado de Jesus
def recado_de_jesus():
    prompt = """
    Fale como se fosse Jesus, em primeira pessoa. Traga uma mensagem curta, acolhedora, e cheia de esperança baseada nas palavras e ensinos que estão nos evangelhos. Seja pessoal, como se Jesus estivesse falando diretamente ao coração da pessoa que está lendo.
    """
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você está interpretando Jesus Cristo de forma fiel ao Novo Testamento."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )
    return resposta.choices[0].message.content

# Gerar devocional
if st.button("✨ Gerar Devocional", key="botao_gerar"):
    if feeling:
        with st.spinner("Gerando sua devocional..."):
            try:
                devocional = gerar_devocional(feeling)
                st.markdown("---")
                st.subheader("🕊️ Devocional do Dia")
                st.markdown(f"<div class='caixa'>{devocional}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Ocorreu um erro ao gerar a devocional: {e}")
    else:
        st.warning("Por favor, descreva como está se sentindo.")

# Nova seção: Recado de Jesus
st.markdown("---")
st.subheader("📖 Um recado de Jesus para você")
if st.button("📰 Ouvir a voz do Mestre", key="botao_recado"):
    with st.spinner("Jesus está te respondendo..."):
        try:
            mensagem = recado_de_jesus()
            st.markdown(f"<div class='caixa'>{mensagem}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Erro ao gerar o recado: {e}")

# Mensagem de apoio
st.markdown("---")
st.subheader("🤝 Este aplicativo sempre será gratuito.")
st.markdown("Se ele te abençoou, compartilhe com mais alguém.")
st.markdown("Se desejar, você pode fazer uma doação de qualquer valor. Deus te abençoe!")

# Pix e QR Code
col1, col2 = st.columns([1, 2])
with col1:
    try:
        qr_path = "QRCODE.jpeg"
        if os.path.exists(qr_path):
            qr_img = Image.open(qr_path)
            st.image(qr_img, caption="Doe via Pix", width=200)
        else:
            st.warning("QR Code não encontrado. Envie o arquivo novamente.")
    except Exception as e:
        st.error(f"Erro ao carregar QR Code: {e}")
with col2:
    st.markdown("**Chave Pix (copia e cola):**")
    chave_pix = "00020126360014BR.GOV.BCB.PIX0114+55819983118985204000053039865802BR5924PAULO CAVALCANTI PEREIRA6006RECIFE622605227UlW9vI9m9waJalgNzeJKI63049F25"
    st.code(chave_pix, language="text")

# Rodapé
st.markdown("""<footer>Feito ❤️ pelo Pastor Paulo Cavalcanti.</footer>""", unsafe_allow_html=True)
