import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env
load_dotenv()

# Configuração da página
st.set_page_config(page_title="Minha Conversa com Jesus", page_icon="🙏")
st.title("Minha Conversa com Jesus")
st.write("Digite como você está se sentindo e receba uma mensagem devocional cristã personalizada.")

# Cache local para evitar chamadas repetidas
@st.cache_data(show_spinner=False)
def generate_cached_devotional(feeling):
    return generate_devotional(feeling)

# Função principal para gerar devocional
def generate_devotional(feeling):
    prompt = f"""
Você é um assistente espiritual cristão. Sempre que receber uma frase sobre um sentimento, GERE UMA MENSAGEM DE DEVOCIONAL CRISTÃ seguindo EXATAMENTE este formato em Markdown:

**Palavra de Jesus:**  
<Cite um versículo falado por Jesus nos Evangelhos, relacionado ao sentimento do usuário, com referência bíblica.>

**Reflexão:**  
<Escreva uma breve reflexão que conecte o versículo ao sentimento do usuário.>

**Oração:**  
<Escreva uma oração curta sobre o tema, começando com "Senhor Jesus...".>

**Desafio do dia:**  
<Sugira uma ação prática para o usuário se aproximar de Jesus hoje, de forma simples e direta.>

Agora gere a mensagem para o sentimento: "{feeling}".
Responda sempre em português, usando o formato acima.
"""
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Erro ao gerar mensagem: {str(e)}"

# Interface principal
feeling = st.text_input("Como você está se sentindo hoje?")

if st.button("Gerar devocional"):
    if feeling.strip() == "":
        st.warning("Por favor, digite como você está se sentindo.")
    else:
        with st.spinner("Gerando sua conversa com Jesus..."):
            devotional = generate_cached_devotional(feeling.lower().strip())
            st.markdown(devotional)

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Feito com ❤️ usando Streamlit & OpenAI")



