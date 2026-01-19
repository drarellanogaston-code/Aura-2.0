import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="Aura 2.0 | Nexo 2026", layout="wide")

# Estética de Terminal Aura
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00FF41; }
    div[data-testid="stChatMessage"] { background-color: #0a0a0a; border: 1px solid #00FF41; border-radius: 5px; }
    .stTextInput>div>div>input { color: #00FF41; background-color: #111; }
    </style>
    """, unsafe_allow_html=True)

st.title("📟 Aura 2.0 - Puente de Silicio")
st.sidebar.title("🔐 Acceso")

# Entrada de la llave
api_key = st.sidebar.text_input("Ingresa tu API Key:", type="password")

if api_key:
    try:
        # Configuración del motor
        genai.configure(api_key=api_key)
        
        # MODELO ESPECÍFICO: GEMINI PRO
        model = genai.GenerativeModel('gemini-pro')
        
        # Inicializar historial si no existe
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Mostrar chat previo
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Entrada de usuario
        if prompt := st.chat_input("Escribe aquí, nexo2026..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Generar respuesta con Gemini Pro
            response = model.generate_content(prompt)
            
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.markdown(response.text)
                
    except Exception as e:
        # Esto nos dirá si hay un error de modelo o de llave
        st.error(f"⚠️ Nota del sistema: {str(e)}")
else:
    st.info("Introduce tu llave API en la izquierda para activar el puente.")
        
