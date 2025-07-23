import streamlit as st
import openai
import os

# Configuração do Streamlit
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

# Função para gerar o devocional via OpenAI (nova API)
def gerar_devocional(sentimento):
    prompt = f"""
Você é um assistente espiritual cristão. Quando alguém compartilha como está se sentindo, responda com um devocional mais aprofundado, acolhedor e reflexivo. Siga esta estrutura, escrevendo sempre em português:

1. Palavra de Jesus: Escolha um versículo dito por Jesus nos Evangelhos que se relacione com o sentimento: "{sentimento}". Cite o livro e o versículo.
2. Reflexão: Escreva uma reflexão mais profunda (aprox. 2-3 parágrafos) conectando o versículo ao sentimento relatado, mostrando como as palavras de Jesus podem transformar a situação, trazendo consolo, direção e esperança.
3. Oração: Escreva uma oração personalizada, baseada no sentimento e na Palavra escolhida, convidando Jesus para a situação da pessoa.
4. Sugestões práticas para o dia: Ofereça pelo menos duas sugestões simples, concretas e atuais para a pessoa viver aquela Palavra de Jesus no dia de hoje (por exemplo: separar um tempo de silêncio, enviar uma mensagem para alguém, anotar motivos de gratidão, etc).

Seja sempre acolhedor, empático e positivo. Use uma linguagem acessível e frases claras.

Exemplo:
- Palavra de Jesus: "Vinde a mim todos os cansados e sobrecarregados, e eu vos aliviarei." (Mateus 11:28)
- Reflexão: Jesus conhece profundamente o seu coração e entende o peso que você está carregando. Suas palavras são um convite a entregar todas as preocupações e buscar nEle o verdadeiro descanso. Mesmo nos dias mais exaustivos, Jesus permanece ao seu lado, pronto para renovar suas forças e acalmar sua mente. Confie que Ele se importa com cada detalhe da sua vida e deseja aliviar seu fardo.
- Oração: Senhor Jesus, reconheço meu cansaço e minha limitação. Entrego a Ti tudo o que tem pesado sobre mim e peço que me envolva com Tua paz e amor. Ajuda-me a confiar mais em Ti a cada dia. Amém.
- Sugestões práticas para o dia:
  • Separe 5 minutos para fazer uma oração silenciosa entregando suas preocupações a Jesus.
  • Escreva uma lista de fardos que deseja entregar e, ao final do dia, agradeça por cada um deles.

Agora gere o devocional para: "{sentimento}"
"""
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=700,
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
