import streamlit as st

st.set_page_config(page_title="Minha Conversa com Jesus", page_icon="🙏")

st.title("🙏 Minha Conversa com Jesus")

st.write("""
Bem-vindo ao aplicativo **Minha Conversa com Jesus**.

Aqui você pode desfrutar de reflexões, mensagens e conversas inspiradoras.  
Aproveite o conteúdo à vontade!
""")

# Aqui você pode adicionar mais conteúdo do app, como textos, perguntas, imagens, etc.

st.header("Mensagem do Dia")
st.write("""
*"Confie no Senhor de todo o seu coração e não se apoie em seu próprio entendimento."*  
**Provérbios 3:5**
""")

st.header("Deixe sua reflexão")
reflexao = st.text_area("Compartilhe o que está sentindo ou pensando hoje:")

if reflexao:
    st.success("Obrigado por compartilhar sua reflexão! 🙏")

# Fique à vontade para personalizar e expandir o conteúdo do app.
