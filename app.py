import streamlit as st

st.set_page_config(page_title="Assinatura - Minha Conversa com Jesus", page_icon="🙏")

st.title("🙏 Minha Conversa com Jesus")
st.write("Para acessar o conteúdo completo, clique no botão abaixo e faça sua assinatura:")

checkout_url = "https://www.mercadopago.com.br/subscriptions/checkout?preapproval_plan_id=dadca597a91f47be81a6133103eacfa5"

st.markdown(f"""
    <a href="{checkout_url}" name="MP-payButton" class="blue-button" target="_blank">Assinar agora</a>
    <style>
    .blue-button {{
        background-color: #3483FA;
        color: white;
        padding: 12px 28px;
        text-decoration: none;
        border-radius: 6px;
        display: inline-block;
        font-size: 18px;
        font-weight: bold;
        transition: background-color 0.3s;
        font-family: Arial, sans-serif;
        margin-top: 24px;
    }}
    .blue-button:hover {{
        background-color: #2a68c8;
    }}
    </style>
""", unsafe_allow_html=True)

st.info("Após realizar a assinatura, retorne a este aplicativo e faça login normalmente.")
