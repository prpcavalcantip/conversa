import streamlit as st
import openai
import os
from PIL import Image
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Minha Conversa com Jesus", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f8f4ff;
    }
    .titulo {
        text-align: center;
        font-size: 40px;
        color: #5b2e91;
        font-weight: bold;
    }
    .subtitulo {
        font-size: 18px;
        color: #333333;
    }
    .rodape {
        text-align: center;
        color: gray;
        margin-top: 50px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="titulo">Minha Conversa com Jesus</div>', unsafe_allow_html=True)

st.write("\n")
st.markdown('<div class="subtitulo">Como você está se sentindo hoje?</div>', unsafe_allow_html=True)

feeling = st.text_input("Descreva em poucas palavras seu estado emocional:")

if st.button("Gerar Devocional 🙏"):
    if feeling:
        with st.spinner('Gerando sua devocional...'):
            try:
                prompt = f"""
                Atue como um pastor cristão experiente e amoroso.
                Crie uma devocional profunda, baseada no ensino de Jesus, para uma pessoa que se sente: {feeling}.
                A devocional deve conter:
                - Um versículo bíblico apropriado
                - Uma reflexão profunda sobre a situação emocional
                - Uma oração personalizada
                - 2 práticas diárias que a pessoa pode seguir para se fortalecer em Deus.
                Seja acolhedor, use uma linguagem simples e cheia de esperança.
                """

                resposta = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )

                devocional = resposta.choices[0].message.content
                st.markdown("---")
                st.markdown("### Sua Devocional ✨")
                st.markdown(devocional)
                st.markdown("---")

                # Mensagem de agradecimento e doação
                st.success("Esse aplicativo sempre será gratuito. Se você gostou, compartilhe com alguém! 💌")
                st.markdown("#### Se quiser fazer uma doação de qualquer valor, agradecemos de coração:")

                # QR Code
                qrcode_path = "QRCODE.jpeg"
                if os.path.exists(qrcode_path):
                    image = Image.open(qrcode_path)
                    st.image(image, caption="Chave Pix: +5581998311898")
                else:
                    st.warning("QR Code não encontrado.")

                # Pix copia e cola
                st.code("""
00020126360014BR.GOV.BCB.PIX0114+55819983118985204000053039865802BR5924PAULO CAVALCANTI PEREIRA6006RECIFE622605227UlW9vI9m9waJalgNzeJKI63049F25
                """, language="text")

            except Exception as e:
                st.error(f"Ocorreu um erro ao gerar a devocional: {e}")
    else:
        st.warning("Por favor, escreva como você está se sentindo.")

# Rodapé com assinatura
st.markdown('<div class="rodape">Feito ❤️ pelo Pastor Paulo Cavalcanti</div>', unsafe_allow_html=True)
