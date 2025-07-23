import streamlit as st

# Configuração da página
st.set_page_config(page_title="Minha Conversa com Jesus", layout="centered")

# MENSAGEM DE BOAS-VINDAS
st.markdown("""
<div style='text-align: center; margin-top: 30px; margin-bottom: 10px;'>
    <h2 style='color: #205081; font-family: Arial, sans-serif;'>Bem-vindo ao Minha Conversa com Jesus!</h2>
    <p style='font-size: 1.1em; color: #333; margin-bottom: 30px;'>
        É uma alegria ter você aqui.<br>
        Viva um tempo de inspiração, reflexão e conexão com a Palavra de Jesus.<br>
        Para acessar todo o conteúdo, faça sua assinatura anual abaixo:
    </p>
</div>
""", unsafe_allow_html=True)

# BOTÃO DE ASSINATURA AZUL DESTACADO
st.markdown("""
<div style='text-align: center; margin-bottom: 30px;'>
    <a href="https://www.mercadopago.com.br/subscriptions/checkout?preapproval_plan_id=dadca597a91f47be81a6133103eacfa5" 
       name="MP-payButton" 
       style="
          background-color: #3483FA;
          color: #fff;
          padding: 14px 32px;
          text-decoration: none;
          border-radius: 8px;
          display: inline-block;
          font-size: 1.15em;
          font-weight: 600;
          font-family: Arial, sans-serif;
          transition: background 0.3s;
          box-shadow: 0 2px 8px rgba(52,131,250,0.1);
          border: none;
      ">
      Assinar agora
    </a>
</div>
""", unsafe_allow_html=True)

# INSTRUÇÃO APÓS O BOTÃO
st.info("Após o pagamento, seu acesso ao conteúdo exclusivo será liberado automaticamente ou após confirmação. Em caso de dúvidas, entre em contato com o suporte.")

# --- Conteúdo do app após assinatura ---
st.markdown("---")
st.markdown("""
### Sobre o App

Este aplicativo oferece devocionais diários, reflexões e orações para fortalecer sua caminhada com Jesus.
Aproveite cada mensagem e viva um tempo de renovação espiritual!

*(Após a assinatura, conteúdo exclusivo aparecerá aqui conforme a lógica do seu app.)*
""")
