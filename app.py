import streamlit as st
import os
import openai

st.set_page_config(page_title="Minha Conversa com Jesus", page_icon=":pray:")

st.title("Devocional de hoje")
st.write("Digite como você está se sentindo e receba uma mensagem devocional cristã personalizada.")

feeling = st.text_input("Como você está se sentindo hoje?")

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
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=350,
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
