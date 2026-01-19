import streamlit as st
import google.generativeai as genai

# Configuración visual de la terminal
st.set_page_config(page_title="Aura 2.0 | Nexo 2026", layout="wide")
st.markdown("<style>.stApp { background-color: #050505; color: #00FF41; }</style>", unsafe_allow_html=True)
st.title("📟 Aura 2.0 - Puente de Silicio")

# Acceso lateral para la API Key
api_key = st.sidebar.text_input("Ingresa tu API Key:", type="password")

if api_key:
    try:
        # Configuración de la conexión
        genai.configure(api_key=api_key)
        
        # Cambio solicitado: Usamos gemini-pro (el resto del flujo es flash/rápido)
        aura_model = genai.GenerativeModel('gemini-pro')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Mostrar historial de chat
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Lógica de chat
        if prompt := st.chat_input("Escribe aquí..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Generación de respuesta
            response = aura_model.generate_content(prompt)
            
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.markdown(response.text)
                
    except Exception as e:
        st.error(f"⚠️ Nota del sistema: {str(e)}")
else:
    st.info("Introduce tu llave API en la izquierda para activar el puente.")
        
