import streamlit as st
import openai
import os

# Configurações iniciais do Streamlit
st.set_page_config(page_title="Minha Conversa com Jesus", page_icon="✝️", layout="centered")

# Título centralizado
st.markdown(
    "<h1 style='text-align: center; font-size: 2.5em; margin-bottom: 30px;'>Minha Conversa com Jesus</h1>",
    unsafe_allow_html=True
)

# Campo de entrada para o usuário
st.markdown(
    "<div style='text-align: center; font-size: 1.25em;'>Como você está se sentindo hoje?</div>",
    unsafe_allow_html=True
)
feeling = st.text_input("", max_chars=120)

# Função para gerar o devocional via OpenAI
def gerar_devocional(sentimento):
    prompt = f"""
Você é um assistente espiritual cristão. Quando alguém compartilha como está se sentindo, responda com um devocional curto e acolhedor. Siga essa estrutura e escreva sempre em português:

1. Palavra de Jesus: Escolha um versículo dito por Jesus nos Evangelhos que se relacione com o sentimento: "{sentimento}". Cite o livro e o versículo.
2. Reflexão: Explique brevemente como esse versículo pode confortar ou orientar a pessoa, conectando a mensagem de Jesus ao sentimento dela.
3. Oração: Escreva uma breve oração personalizada, baseada no sentimento e na Palavra escolhida.
4. Desafio do dia: Proponha uma pequena ação prática para que a pessoa se aproxime de Jesus hoje.

Seja sempre acolhedor e positivo. Mantenha fonte acessível e frases curtas.

Exemplo:
- Palavra de Jesus: "Vinde a mim todos os cansados e sobrecarregados, e eu vos aliviarei." (Mateus 11:28)
- Reflexão: Jesus te convida a descansar nEle, confiando que Ele cuida de você…
- Oração: Senhor Jesus, entrego meu cansaço e minhas preocupações em Tuas mãos…
- Desafio do dia: Reserve 5 minutos para conversar com Jesus sobre o que tem te cansado.

Agora gere o devocional para: "{sentimento}"
"""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.7,
    )
    texto = response.choices[0].message.content.strip()
    return texto

# Função para salvar histórico local
def salvar_historico(sentimento, devocional):
    try:
        with open("historico_devocional.txt", "a", encoding="utf-8") as f:
            f.write(f"\n---\nSentimento: {sentimento}\n{devocional}\n")
    except Exception as e:
        st.warning("Não foi possível salvar o histórico.")

# Quando o usuário envia o sentimento
if feeling:
    with st.spinner('Gerando seu devocional...'):
        devocional = gerar_devocional(feeling)
        # Exibe o devocional formatado, centralizado e limpo
        st.markdown(
            f"<div style='background-color: #f9fafb; border-radius: 16px; padding: 24px; margin-top: 24px; "
            f"text-align: center; font-size: 1.1em;'>"
            f"{devocional.replace(chr(10), '<br>')}"
            f"</div>", unsafe_allow_html=True
        )
        salvar_historico(feeling, devocional)

# Rodapé
st.markdown(
    "<div style='text-align: center; font-size: 1em; margin-top: 50px; color: #6c757d;'>"
    "© 2025 Minha Conversa com Jesus | Feito com Streamlit"
    "</div>", unsafe_allow_html=True
)


