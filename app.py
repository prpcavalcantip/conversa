import streamlit as st
import os
import openai

st.set_page_config(
    page_title="Minha Conversa com Jesus",
    page_icon="🙏",
    layout="centered",
    initial_sidebar_state="auto"
)

# Estilo customizado com CSS
st.markdown("""
    <style>
        .main-container {
            background-color: #f7fafc;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
            margin-top: 2rem;
        }
        .title {
            font-size: 2.7rem;
            text-align: center;
            font-weight: bold;
            color: #4a5568;
            margin-bottom: 0.5rem;
        }
        .subtitle {
            text-align: center;
            font-size: 1.1rem;
            color: #718096;
            margin-bottom: 2.5rem;
        }
        .footer {
            text-align: center;
            font-size: 0.9rem;
            color: #a0aec0;
            margin-top: 3rem;
        }
        .stTextInput > label {
            font-weight: bold;
            font-size: 1.08rem;
            color: #2d3748;
        }
        .stButton > button {
            background-color: #3182ce !important;
            color: white !important;
            border-radius: 8px !important;
            padding: 0.5rem 1.5rem !important;
            font-size: 1.09rem !important;
        }
        .response-box {
            background-color: #edf2f7;
            border-radius: 10px;
            padding: 1.5rem;
            margin-top: 1.5rem;
            box-shadow: 0 2px 12px rgba(49, 130, 206, 0.09);
            font-size: 1.12rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="title">🙏 Minha Conversa com Jesus</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Receba uma mensagem devocional cristã personalizada.<br>Digite como você está se sentindo hoje.</div>', unsafe_allow_html=True)

feeling = st.text_input("Como você está se sentindo?", max_chars=100)

def generate_devotional(feeling):
    prompt = f"""
Você é um assistente espiritual cristão. Sempre que receber uma frase sobre um sentimento, gere uma mensagem devocional curta e reconfortante, seguindo este formato:

1. Palavra de Jesus: Cite um versículo falado por Jesus (dos Evangelhos), relacionado ao sentimento do usuário.
2. Reflexão: Escreva uma breve reflexão que conecte o versículo ao sentimento.
3. Oração: Escreva uma oração curta sobre o tema.
4. Desafio do dia: Sugira uma ação prática para o usuário se aproximar de Jesus hoje.

Exemplo de entrada: Me sinto cansado e sem direção.
Exemplo de saída:
Palavra de Jesus: "Vinde a mim todos os cansados e sobrecarregados, e eu vos aliviarei." (Mateus 11:28)
Reflexão: Jesus te convida a descansar nEle, entregando sua ansiedade...
Oração: Senhor, eu entrego meu cansaço a Ti...
Desafio do dia: Separe 5 minutos para entregar sua ansiedade a Jesus.

Agora, gere a mensagem para o sentimento: "{feeling}".
Responda sempre em português.
"""
    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-4-1106-nano",  # Ou o modelo que você preferir
            messages=[{"role": "user", "content": prompt}],
            max_tokens=350,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro ao gerar mensagem: {str(e)}"

if st.button("💬 Gerar devocional"):
    if feeling.strip() == "":
        st.warning("Por favor, digite como você está se sentindo.")
    else:
        devotional = generate_devotional(feeling)
        st.markdown(f'<div class="response-box">{devotional}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="footer">Feito com ❤️ usando Streamlit & OpenAI</div>', unsafe_allow_html=True)
        devotional = generate_devotional(feeling)
        st.markdown(devotional)

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Feito com ❤️ usando Streamlit & OpenAI")
