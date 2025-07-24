import streamlit as st
import re
from openai import OpenAI

# Inicializa o cliente OpenAI com a chave segura
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Configura a página
st.set_page_config(page_title="Minha Conversa com Jesus", page_icon="✝️", layout="centered")

# Título
st.markdown("""
    <h1 style='text-align: center; font-size: 2.5em; margin-bottom: 30px;'>
        Minha Conversa com Jesus
    </h1>
""", unsafe_allow_html=True)

# Pergunta ao usuário
st.markdown("""
    <div style='text-align: center; font-size: 1.25em; margin-bottom: 20px;'>
        Como você está se sentindo hoje?
    </div>
""", unsafe_allow_html=True)

# Campo de entrada
feeling = st.text_input(
    label="Descreva em poucas palavras seu estado emocional:",
    max_chars=120,
    placeholder="Ex: me sinto ansioso, cansado e desmotivado"
)

# Função para converter **texto** em <strong>texto</strong>
def formatar_negrito(texto):
    return re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', texto)

# Função para gerar o devocional
def gerar_devocional(sentimento):
    prompt_template = """
Você é um assistente espiritual cristão. Quando alguém compartilha como está se sentindo, responda com um devocional mais aprofundado, acolhedor e reflexivo. Siga esta estrutura, escrevendo sempre em português:

1. Palavra de Jesus: Escolha um versículo dito por Jesus nos Evangelhos que se relacione com o sentimento: "{sentimento}". Cite o livro e o versículo.
2. Reflexão: Escreva uma reflexão mais profunda (aprox. 2-3 parágrafos) conectando o versículo ao sentimento relatado, mostrando como as palavras de Jesus podem transformar a situação, trazendo consolo, direção e esperança.
3. Oração: Escreva uma oração personalizada, baseada no sentimento e na Palavra escolhida, convidando Jesus para a situação da pessoa.
4. Sugestões práticas para o dia: Ofereça pelo menos duas sugestões simples, concretas e atuais para a pessoa viver aquela Palavra de Jesus no dia de hoje (por exemplo: separar um tempo de silêncio, enviar uma mensagem para alguém, anotar motivos de gratidão, etc).

Formate a resposta em blocos bem separados e com títulos marcados com **, assim:

**Palavra de Jesus:**  
<versículo>

**Reflexão:**  
<reflexão>

**Oração:**  
<oração>

**Sugestões práticas para o dia:**  
• <sugestão 1>  
• <sugestão 2>

Agora gere o devocional para: "{sentimento}"
"""
    prompt = prompt_template.format(sentimento=sentimento)

    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=700,
        tempera
