import streamlit as st
import mercadopago

# ======================================
# 🔑 CONFIGURAÇÕES - SUBSTITUA AQUI!
# ======================================
ACCESS_TOKEN = "APP_USR-9f409612-b346-4437-a1d7-33589ad29133"  # Ex: "APP_USR-1234567890..."
PLANO_ID = "dadca597a91f47be81a6133103eacfa5"         # Ex: "dadca597a91f47be81a6133103eacfa5"
# ======================================

# Inicializa a conexão com o Mercado Pago
sdk = mercadopago.SDK(ACCESS_TOKEN)

# Configura a página
st.set_page_config(
    page_title="Assinatura - Minha Conversa com Jesus",
    page_icon="🙏",
    layout="centered"
)

# Tela principal
st.title("🙏 Minha Conversa com Jesus")
st.write("""
Bem-vindo ao aplicativo **Minha Conversa com Jesus**!

Para acessar o conteúdo completo, faça sua assinatura:
""")

# Coleta o e-mail do usuário
email = st.text_input("📧 Digite seu e-mail:")

if st.button("📝 Assinar Agora") and email:
    try:
        # Cria a assinatura no Mercado Pago
        assinatura = sdk.preapproval().create({
            "preapproval_plan_id": PLANO_ID,
            "payer_email": email,
            "back_url": "https://seusite.com/obrigado",  # Página após pagamento
            "notification_url": "https://seusite.com/webhook"  # Para avisos
        })
        
        # Verifica se o 'init_point' está na resposta e exibe o link de pagamento
        init_point = assinatura.get('response', {}).get('init_point')
        if init_point:
            st.success("✅ Pronto! Clique no link abaixo para finalizar:")
            st.markdown(f"[Ir para o Pagamento]({init_point})", unsafe_allow_html=True)
        else:
            st.error("❌ Ocorreu um erro ao gerar o link de pagamento.")
            st.info(f"Detalhes da resposta do Mercado Pago: {assinatura.get('response')}")
        
    except Exception as e:
        st.error(f"❌ Ocorreu um erro: {str(e)}")
        st.info("Por favor, tente novamente ou entre em contato com nosso suporte.")

# Rodapé
st.markdown("---")
st.write("Dúvidas? Entre em contato: contato@seusite.com")
        st.info("Por favor, tente novamente ou entre em contato com nosso suporte.")

# Rodapé
st.markdown("---")
st.write("Dúvidas? Entre em contato: contato@seusite.com")
