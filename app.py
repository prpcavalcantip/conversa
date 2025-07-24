import streamlit as st
from openai import OpenAI
from PIL import Image
import base64

# Inicializa o cliente da OpenAI
client = OpenAI()

# Função para gerar devocional
def gerar_devocional(sentimento):
    prompt = f"""
    Você é um conselheiro espiritual cristão. Escreva uma devocional profunda com base em como a pessoa está se sentindo.
    Inclua:
    1. Um versículo apropriado das palavras de Jesus.
    2. Uma mensagem de esperança com profundidade bíblica.
    3. Uma oração personalizada.
    4. Uma sugestão prática para o dia.
    
    Sentimento da pessoa: {sentimento}
    """
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um conselheiro espiritual cristão."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7
    )
    return resposta.choices[0].message.content

# Configura a página
st.set_page_config(page_title="Minha Conversa com Jesus", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #f4f4f9;
        }
        .main {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        h1, h4 {
            text-align: center;
            color: #2c3e50;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #888;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("## 🙏 Minha Conversa com Jesus")
st.markdown("### Como você está se sentindo hoje?")

feeling = st.text_input("Descreva em poucas palavras seu estado emocional:")

if st.button("Gerar Devocional", use_container_width=True):
    if feeling:
        with st.spinner("Gerando sua devocional..."):
            try:
                devocional = gerar_devocional(feeling)
                st.markdown("---")
                st.markdown(devocional)
                st.markdown("---")

                st.success("Se essa mensagem tocou seu coração, compartilhe com alguém. 🙌")
                st.markdown("""
                <div style='text-align: center;'>
                    <h4>Este aplicativo sempre será gratuito.</h4>
                    <p>Se você quiser fazer uma doação de qualquer valor, agradecemos. 🙏</p>
                </div>
                """, unsafe_allow_html=True)

                # Exibe QR Code
                imagem = Image.open("/mnt/data/QRCODE.jpeg")
                st.image(imagem, caption="Paulo Cavalcanti Pereira", use_column_width=True)

                # Copia e Cola
                chave_pix = "00020126360014BR.GOV.BCB.PIX0114+55819983118985204000053039865802BR5924PAULO CAVALCANTI PEREIRA6006RECIFE622605227UlW9vI9m9waJalgNzeJKI63049F25"
                st.code(chave_pix, language="text")

            except Exception as e:
                st.error(f"Ocorreu um erro ao gerar a devocional: {e}")
    else:
        st.warning("Por favor, descreva seu sentimento para gerar a devocional.")

st.markdown("""
    <div class="footer">
        Feito ❤️ pelo Pastor Paulo Cavalcanti
    </div>
""", unsafe_allow_html=True)
