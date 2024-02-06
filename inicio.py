import streamlit as st
#import streamlit_authenticator as stauth
from PIL import Image
import base64
from dependencias import set_png_as_page_bg, show_hide

path_favicon = './img/er.ico'
im = Image.open(path_favicon)
st.set_page_config(page_title='RIME LOGISTIC', page_icon= im, initial_sidebar_state='collapsed')

set_png_as_page_bg(r'./img/transporte.jpg')

placeholder = st.empty()

with placeholder.container():
    col1, col2, col3 = st.columns([1,4,1])
    with col2:
        path_logo = './img/logo_rimesoft.png'
        image = Image.open(path_logo)
        st.image(image, use_column_width=True)
    col4,col5,col6 = st.columns([1,6,1])
    with col5:
        st.markdown("<h5 style='font-family: 'Play', sans-serif;'>Dimensiona y Predice el Riesgo de tus Transportes</h5>", unsafe_allow_html=True)
    col7,col8,col9,col10,col11 = st.columns(5)
    with col9:
        login_button = st.button("Empezar")

if login_button:
    placeholder.empty()
    col12, col13, col14 = st.columns([1,3,1])
    with col13:
        tab1, tab2 = st.tabs(["Inicio de Sesión", "Registrarse"])
        with tab1:
            st.header("A cat")