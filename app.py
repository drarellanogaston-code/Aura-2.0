import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Aura 2.0 | Nexo 2026", layout="wide")

st.markdown("<style>.stApp { background-color: #050505; color: #00FF41; }</style>", unsafe_allow_html=True)
st.title("📟 Aura 2.0 - Puente de Silicio")

api_key = st.sidebar.text_input("Ingresa tu API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Usamos el modelo más básico y estable para asegurar conexión
        genai.GenerativeModel('gemini-pro')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Escribe aquí..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            response = model.generate_content(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.markdown(response.text)
                
    except Exception as e:
        st.error(f"⚠️ Error técnico: {str(e)}")
else:
    st.info("Introduce tu llave API en la izquierda para activar el puente.")
    
