import streamlit as st
import os
import openai

st.set_page_config(page_title="Minha Conversa com Jesus", page_icon="🙏")

st.title("Minha Conversa com Jesus")
st.write("Digite como você está se sentindo e receba uma mensagem devocional cristã personalizada.")

feeling = st.text_input("Como você está se sentindo hoje?")

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

Exemplo de entrada: Me sinto cansado e sem direção.
Exemplo de saída:
**Palavra de Jesus:**  
"Vinde a mim todos os cansados e sobrecarregados, e eu vos aliviarei." (Mateus 11:28)

**Reflexão:**  
Jesus te convida a descansar nEle, entregando sua ansiedade e buscando Sua orientação para sua vida.

**Oração:**  
Senhor Jesus, eu entrego meu cansaço e minhas dúvidas a Ti. Guia meus passos e renova minhas forças. Amém.

**Desafio do dia:**  
Separe 5 minutos para orar e pedir direção a Jesus.

Agora gere a mensagem para o sentimento: "{feeling}".
Responda sempre em português, usando o formato acima.
"""
    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro ao gerar mensagem: {str(e)}"

if st.button("Gerar devocional"):
    if feeling.strip() == "":
        st.warning("Por favor, digite como você está se sentindo.")
    else:
        devotional = generate_devotional(feeling)
        st.markdown(devotional)

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Feito com ❤️ usando Streamlit & OpenAI")


