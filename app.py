import streamlit as st

MERCADO_PAGO_LINK = "https://www.mercadopago.com.br/checkout/v1/redirect?preference-id=TEST-bb5e1499-f585-4763-b8aa-d792a3fe4201"

if "assinante" not in st.session_state:
    st.session_state["assinante"] = False

if not st.session_state["assinante"]:
    st.markdown("## Assine para acessar o conteúdo completo!")
    st.markdown(f"[**Clique aqui para assinar por 1 ano**]({MERCADO_PAGO_LINK})", unsafe_allow_html=True)
    st.info("Após o pagamento, digite o e-mail que você usou para liberar o acesso. O administrador precisa aprovar sua assinatura.")
    email_pagamento = st.text_input("E-mail usado no pagamento:")
    if st.button("Verificar pagamento"):
        st.write("Função de verificação aqui.")
    st.stop()

st.write("Conteúdo exclusivo para assinantes!")
