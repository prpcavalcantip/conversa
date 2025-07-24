import streamlit as st
import os
from PIL import Image
from openai import OpenAI

# Inicializar cliente OpenAI com a chave do Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Layout e estilo
st.set_page_config(page_title="Minha Conversa com Jesus", page_icon="🙏", layout="centered")
st.markdown("""
    <style>
        .titulo {
            font-size: 36px;
            font-weight: bold;
            color: #4B0082;
            text-align: center;
        }
        .subtitulo {
            font-size: 20px;
            color: #555;
            text-align: center;
        }
        .caixa {
            background-color: #f2f2f2;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        }
        .botao {
            background-color: #4B0082;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
        }
        footer {
            text-align: center;
            font-size: 14px;
            color: gray;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<div class='titulo'>🙏 Minha Conversa com Jesus</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitulo'>Como você está se sentindo hoje?</div>", unsafe_allow_html=True)

# Entrada do usuário
with st.container():
    feeling = st.text_input("Descreva em poucas palavras seu estado emocional:")

# Função para gerar devocional
def gerar_devocional(sentimento):
    prompt = f"""
    Você é um devocionalista cristão. Crie uma devocional profunda com base nas palavras de Jesus, considerando o sentimento descrito: "{sentimento}". 
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
        max_tokens=800
    )
    return resposta.choices[0].message.content

# Geração
if st.button("✨ Gerar Devocional", key="botao_gerar"):
    if feeling:
        with st.spinner("Gerando sua devocional..."):
            try:
                devocional = gerar_devocional(feeling)
                st.markdown("---")
                st.markdown(devocional)
            except Exception as e:
                st.error(f"Ocorreu um erro ao gerar a devocional: {e}")
    else:
        st.warning("Por favor, descreva como está se sentindo.")

# Mensagem de apoio
st.markdown("---")
st.subheader("🙌 Este aplicativo sempre será gratuito.")
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
