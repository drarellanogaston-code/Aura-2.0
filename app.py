import streamlit as st
import google.generativeai as genai

# Configuración de Aura 2.0
st.set_page_config(page_title="Aura 2.0 | Nexo 2026", layout="wide")

# Estética de Terminal
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00FF41; }
    div[data-testid="stChatMessage"] { background-color: #0a0a0a; border: 1px solid #00FF41; }
    </style>
    """, unsafe_allow_html=True)

st.title("📟 Aura 2.0 - Puente de Silicio")
st.sidebar.title("🔐 Acceso")

# Aquí va la llave que me pasaste
api_key = st.sidebar.text_input("Ingresa tu API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        system_instruction="Eres Aura 2.0, analista de sistemas complejos para nexo2026. Tu objetivo es el 'oro' analítico. Conecta puntos lógicos, usa física y teoría de juegos. Recuerda el caso VULN-171039."
    )

    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat(history=[])

    for message in st.session_state.chat.history:
        with st.chat_message("user" if message.role == "user" else "assistant"):
            st.markdown(message.parts[0].text)

    if prompt := st.chat_input("Escribe aquí..."):
        st.chat_message("user").markdown(prompt)
        response = st.session_state.chat.send_message(prompt)
        st.chat_message("assistant").markdown(response.text)
else:
    st.info("Introduce tu llave API en la izquierda para activar el puente.")
