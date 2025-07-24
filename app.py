import streamlit as st
import re
from openai import OpenAI  # nova forma de usar a biblioteca

# Cria o cliente com a chave do Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Configuração da página
st.set_page_config(page_title="Minha Conversa com Jesus", page_icon="✝️", layout="centered")

# Título
st.markdown(
    """
    <h1 style='text-align: center; font-size: 2.5em; margin-bottom: 30px;'>
        Minha Conversa com Jesus
    </h1>
    """,
    unsafe_allow_html=True
)

# Pergunta ao usuário
st.markdown(
    """
    <div style='text-align: center; font-size: 1.25em; margin-bottom: 20px;'>
        Como você está se sentindo hoje?
    </div>
    """,
    unsafe_allow_html=True
)

# Campo de entrada
feeling = st.text_input(
    label="Descreva em poucas palavras seu estado emocional:",
    max_chars=120,
    placeholder="Ex: me sinto ansioso, cansado e desmotivado"
)

# Função para converter **texto** em <strong>texto</strong>
def formatar_negrito(texto):
    return re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', texto)

# Função para gerar o devocional com base no sentimento
def gerar_devocional(sentimento):
    prompt = f"""
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
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=700,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

# Botão para gerar o devocional
if st.button("Gerar Devocional") and feeling:
    with st.spinner('Gerando seu devocional...'):
        devocional = gerar_devocional(feeling)
        devocional_formatado = formatar_negrito(devocional)
        st.markdown(
            f"""
            <div style='background-color: #f9fafb; border-radius: 16px; padding: 24px; margin-top: 24px; 
            text-align: left; max-width: 600px; margin-left: auto; margin-right: auto; 
            font-size: 1.12em; line-height: 1.6; white-space: pre-wrap;'>
            {devocional_formatado}
            </div>
            """,
            unsafe_allow_html=True
        )
        st.success("Devocional gerado com sucesso! 🙏")

# Rodapé
st.markdown(
    """
    <div style='text-align: center; font-size: 1em; margin-top: 50px; color: #6c757d;'>
        © 2025 Minha Conversa com Jesus | Feito com ❤️ em Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
