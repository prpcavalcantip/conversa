import streamlit as st
from openai import OpenAI
import base64

# Inicializa o cliente OpenAI
client = OpenAI()

st.set_page_config(page_title="Minha Conversa com Jesus", page_icon="🙏", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: #f4f6f9;
        color: #333333;
    }
    .stButton > button {
        background-color: #ff6f61;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 8px;
    }
    .stButton > button:hover {
        background-color: #ff4f41;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🙏 Minha Conversa com Jesus")
st.subheader("Como você está se sentindo hoje?")

feeling = st.text_input("Descreva em poucas palavras seu estado emocional:", placeholder="Ex: cansado, triste, sem esperança")

# Função para gerar a devocional
def gerar_devocional(sentimento):
    prompt = f"""
    Você é um conselheiro espiritual cristão. A partir do sentimento descrito abaixo, crie uma devocional curta e profunda com base nas palavras de Jesus.

    A devocional deve conter:
    1. Um versículo ou ensino de Jesus.
    2. Uma reflexão pessoal e acolhedora.
    3. Uma oração baseada nesse sentimento.
    4. Uma prática diária que ajude a pessoa a viver melhor esse dia.

    Sentimento: {sentimento}
    """
    
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=800
    )

    return resposta.choices[0].message.content.strip()

# Gera a devocional
if st.button("Gerar Devocional 🙏"):
    if feeling.strip() == "":
        st.warning("Por favor, escreva como está se sentindo.")
    else:
        with st.spinner("Gerando sua devocional..."):
            try:
                devocional = gerar_devocional(feeling)
                st.markdown("---")
                st.markdown(devocional)
                st.markdown("---")

                st.success("✨ Esperamos que sua alma tenha sido tocada.")

                # Mensagem de doação
                st.markdown("""
                <div style='text-align: center;'>
                    <h4>🙏 Este aplicativo sempre será gratuito.</h4>
                    <p>Se você foi abençoado, compartilhe com alguém que precisa.</p>
                    <p>Se desejar fazer uma doação de qualquer valor, agradecemos de coração ❤️</p>
                </div>
                """, unsafe_allow_html=True)

                # Exibir QR Code e PIX
                st.image("/mnt/data/QRCODE.jpeg", width=250)

                st.markdown("""
                <p style='text-align: center;'>
                <strong>PAULO CAVALCANTI PEREIRA</strong><br>
                +55 (81) 99831-1898<br>
                <code>00020126360014BR.GOV.BCB.PIX0114+55819983118985204000053039865802BR5924PAULO CAVALCANTI PEREIRA6006RECIFE622605227UlW9vI9m9waJalgNzeJKI63049F25</code>
                </p>
                """, unsafe_allow_html=True)

            except Exception as e:
                st.error("Ocorreu um erro ao gerar o devocional. Verifique sua chave da OpenAI ou tente novamente.")

# Rodapé com assinatura personalizada
st.markdown("""
---
<div style='text-align: center; color: gray;'>
    Feito ❤️ pelo Pastor Paulo Cavalcanti
</div>
""", unsafe_allow_html=True)
