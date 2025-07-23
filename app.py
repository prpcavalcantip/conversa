import streamlit as st

st.set_page_config(page_title="Assinatura - Minha Conversa com Jesus", page_icon="🙏")

st.title("🙏 Minha Conversa com Jesus")

st.write("""
Bem-vindo ao aplicativo **Minha Conversa com Jesus**.

Para acessar o conteúdo completo, realize sua assinatura clicando no botão abaixo:
""")

checkout_url = "https://www.mercadopago.com.br/subscriptions/checkout?preapproval_plan_id=dadca597a91f47be81a6133103eacfa5"

st.markdown(f"""
    <div style="display: flex; justify-content: center; margin-top: 30px; margin-bottom: 30px;">
        <a href="{checkout_url}" name="MP-payButton" class="blue-button" target="_blank">Assinar agora</a>
    </div>
    <style>
    .blue-button {{
        background-color: #3483FA;
        color: white;
        padding: 14px 32px;
        text-decoration: none;
        border-radius: 8px;
        display: inline-block;
        font-size: 20px;
        font-weight: bold;
        transition: background-color 0.3s;
        font-family: Arial, sans-serif;
        box-shadow: 0 2px 6px rgba(0,0,0,0.12);
        border: none;
    }}
    .blue-button:hover {{
        background-color: #2a68c8;
    }}
    </style>
""", unsafe_allow_html=True)

st.info("Após concluir a assinatura, retorne a este aplicativo e faça login normalmente para acessar todas as funcionalidades.")
