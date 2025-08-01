import streamlit as st
import openai

# Configuração da API
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Configuração da página
st.set_page_config(
    page_title="Minha Conversa com Jesus",
    page_icon="🕊️",
    layout="centered",
)

# CSS personalizado
st.markdown("""
    <style>
    /* Estilo geral */
    .stApp {
        background: linear-gradient(120deg, #e0f7fa, #b2ebf2);
        padding: 20px;
    }
    .block-container {
        max-width: 700px;
        margin: auto;
        background: white;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #01579b;
        font-family: 'Lora', serif;
    }
    p, div, span {
        font-family: 'Roboto', sans-serif;
        color: #333;
    }

    /* Inputs e botões */
    .stTextArea textarea {
        border-radius: 8px;
        border: 1.5px solid #0288d1;
        background: #f0f8ff;
        color: #222;
        font-size: 16px;
        padding: 12px;
        transition: border-color 0.3s;
    }
    .stTextArea textarea:focus {
        border-color: #01579b;
        box-shadow: 0 0 5px rgba(2, 136, 209, 0.3);
    }
    .stButton > button {
        background-color: #0288d1 !important;
        color: white !important;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 500;
        border: none;
        font-size: 16px;
        cursor: pointer;
        box-shadow: 0 2px 6px rgba(2, 136, 209, 0.2);
        transition: all 0.3s;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
    }
    .stButton > button:hover {
        background-color: #01579b !important;
        transform: translateY(-1px);
    }
    .stButton > button:focus {
        outline: 2px solid #01579b;
    }

    /* Alertas e mensagens */
    .stAlert, .stSuccess, .stError {
        border-radius: 8px;
        margin: 16px 0;
    }
    .stSuccess > div {
        background: #e6f7fa !important;
        border: 1px solid #a7d8de;
    }

    /* Seção de doação */
    .donation-box {
        background: #e6f7fa;
        border: 1px solid #a7d8de;
        border-radius: 8px;
        padding: 20px;
        margin: 24px 0;
        text-align: center;
    }
    .pix-key {
        background: #fff;
        padding: 8px 12px;
        border-radius: 6px;
        border: 1px solid #a7d8de;
        font-size: 14px;
        word-break: break-all;
        display: inline-block;
        margin: 12px 0;
    }

    /* WhatsApp link */
    .whatsapp-link:hover {
        opacity: 0.8;
    }

    /* Responsividade */
    @media (max-width: 600px) {
        .block-container {
            padding: 16px;
        }
        h1 {
            font-size: 24px;
        }
        .stButton > button {
            padding: 12px;
            font-size: 14px;
        }
        .stTextArea textarea {
            font-size: 14px;
        }
        .donation-box {
            padding: 16px;
        }
        .pix-key {
            font-size: 12px;
        }
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Lora:wght@500&family=Roboto:wght@400;500&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Cabeçalho
st.title("🕊️ Minha Conversa com Jesus")

# Introdução
st.markdown("""
Bem-vindo ao **Minha Conversa com Jesus**!  
Aqui você pode compartilhar como está se sentindo e receber um devocional e um conselho inspirado nas palavras de Jesus.
""")

# Separador
st.markdown("---")

# Formulário de input
with st.form(key="devocional_form"):
    sentimento_user = st.text_area(
        "Como estou me sentindo hoje:",
        placeholder="Exemplo: Estou ansioso, busco paz interior. Sinto gratidão. Estou triste e preciso de forças. Quero ser mais paciente...",
        height=120
    )
    col1, col2 = st.columns([3, 1])
    with col2:
        submit_button = st.form_submit_button("✨ Gerar Devocional", type="primary")

# Processamento do formulário
if submit_button and sentimento_user.strip():
    with st.spinner("Gerando devocional e conselho de Jesus para você..."):
        prompt_devocional = (
            f"Crie uma devocional cristã sobre '{sentimento_user.strip()}'. "
            "Divida em três partes: "
            "1) Texto para meditação: um texto longo (300-400 palavras), profundamente reflexivo, acolhedor, com linguagem atual, sem citar versículos, que conecte emocionalmente e espiritualmente com o sentimento descrito, oferecendo insights e esperança. "
            "2) Oração: uma oração curta (50-100 palavras), profunda, em linguagem atual, que expresse confiança e conexão com Deus. "
            "3) Práticas para vida diária: 3-5 sugestões simples e concretas para viver esse tema no cotidiano."
        )

        prompt_jesus = (
            f"Responda como se fosse Jesus, em primeira pessoa, usando linguagem atual, sempre baseado nas palavras de Jesus nos evangelhos. "
            f"Com acolhimento, empatia e sabedoria, sobre: '{sentimento_user.strip()}'. "
            "Não cite versículos, apenas fale como Jesus falaria hoje, com conselhos amorosos. "
            "Não utilize a expressão 'querido amigo' ou 'querido(a)'. Vá direto ao conselho, de forma acolhedora e prática."
        )

        try:
            # Devocional
            resposta_devocional = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um pastor cristão, acolhedor, reflexivo, atual, simples e prático."},
                    {"role": "user", "content": prompt_devocional}
                ],
                max_tokens=800,  # Aumentado para acomodar texto mais longo
                temperature=0.85
            )
            texto_devocional = resposta_devocional.choices[0].message.content.strip()

            # Conselho de Jesus
            resposta_jesus = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": (
                        "Você é Jesus, responde em primeira pessoa, com acolhimento e empatia, em linguagem atual. "
                        "Não utilize a expressão 'querido amigo' ou 'querido(a)'. Vá direto ao conselho, de forma acolhedora e prática."
                    )},
                    {"role": "user", "content": prompt_jesus}
                ],
                max_tokens=200,
                temperature=0.8
            )
            texto_jesus = resposta_jesus.choices[0].message.content.strip()

            # Exibir resultados
            st.markdown("---")
            st.markdown(f"🌅 **Devocional:**\n\n{texto_devocional}", unsafe_allow_html=True)
            st.markdown("---")
            st.markdown(f"💬 **Conselho de Jesus (baseado nos evangelhos):**\n\n{texto_jesus}", unsafe_allow_html=True)

        except Exception as e:
            st.error("❌ Não foi possível obter a resposta agora.")
            st.info(f"Erro técnico: {str(e)}")

elif submit_button:
    st.warning("Por favor, escreva como está se sentindo hoje.")

# Seção de doação
st.markdown("---")
st.markdown("""
<div class="donation-box">
    <strong>Este aplicativo será sempre gratuito.</strong><br>
    Se você for tocado por Deus, compartilhe este app com quem precisa.<br>
    Caso deseje, pode fazer uma oferta de qualquer valor para apoiar o ministério.<br><br>
    <span style="font-size:16px">Escaneie o QR Code ou copie a chave Pix abaixo:</span><br><br>
    <span class="pix-key">00020126360014BR.GOV.BCB.PIX0114+55819983118985204000053039865802BR5924PAULO CAVALCANTI PEREIRA6006RECIFE622605227UlW9vI9m9waJalgNzeJKI63049F25</span>
</div>
""", unsafe_allow_html=True)

# QR Code
st.image("QRCODE.jpeg", caption="Faça sua oferta escaneando o QR Code", width=200)

# WhatsApp
st.markdown("---")
st.markdown(
    """
    <a href="https://wa.me/5581998311898" target="_blank" class="whatsapp-link" style="text-decoration: none;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="24" style="vertical-align:middle; margin-right:8px"/>
        <span style="font-size:16px; color:#01579b; vertical-align:middle;">Fale no WhatsApp: <strong>81998311898</strong></span>
    </a>
    """,
    unsafe_allow_html=True
)

# Rodapé
st.markdown("---")
st.caption("Desenvolvido com carinho e tecnologia para você. © 2025 Minha Conversa com Jesus")
