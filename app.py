import streamlit as st
import openai
import os

st.set_page_config(page_title="Minha Conversa com Jesus", page_icon="🙏", layout="centered")

st.markdown("""
<style>
body { background-color: #f7f9fa; }
.main { display: flex; flex-direction: column; align-items: center; }
[data-testid="stAppViewContainer"] { 
    background: #f7f9fa;
}
h1, .stMarkdown { text-align: center; }
.big-font { font-size: 20px !important; }
</style>
""", unsafe_allow_html=True)

st.title("Minha Conversa com Jesus")

st.markdown('<div class="big-font">Como você está se sentindo hoje?</div>', unsafe_allow_html=True)
feeling = st.text_input("", max_chars=80)

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
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=350,
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Erro ao gerar mensagem: {str(e)}"

if feeling:
    st.markdown("---")
    st.markdown("### Devocional de hoje")
    devotional = generate_devotional(feeling)
    st.markdown(f"<div class='big-font'>{devotional}</div>", unsafe_allow_html=True)

    # Salvar histórico local (opcional)
    try:
        with open("devocional_history.txt", "a", encoding="utf-8") as f:
            f.write(f"\nSentimento: {feeling}\n{devotional}\n{'='*40}\n")
    except Exception:
        pass

st.markdown("""
<style>
.stTextInput > div > input { font-size: 18px; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<center><small>Feito com ❤️ usando Streamlit & OpenAI</small></center>", unsafe_allow_html=True)

# Configurar a chave da OpenAI via variável de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")
