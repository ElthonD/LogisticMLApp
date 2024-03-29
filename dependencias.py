import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re
from deta import Deta
from dotenv import load_dotenv
import base64
import os

"""
#Cargar las variables de entorno

load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")

# Inicializar con una clave de proyecto

deta = Deta(DETA_KEY)

# Esto es como crear/conectar una base de datos

db = deta.Base("dependencias")

def insert_user(email, username, password):
    
    #Inserts Users into the DB
    #:param email:
    #:param username:
    #:param password:
    #:return User Upon successful Creation:

    date_joined = str(datetime.datetime.now())

    return db.put({'key': email, 'username': username, 'password': password, 'date_joined': date_joined})

insert_user('edrc_1@outlook.com', 'admin', 'Qan40646')

def fetch_users():
    
    #Fetch Users
    #:return Dictionary of Users:
    
    users = db.fetch()
    return users.items


def get_user_emails():
    
    #Fetch User Emails
    #:return List of user emails:
    
    users = db.fetch()
    emails = []
    for user in users.items:
        emails.append(user['key'])
    return emails


def get_usernames():
    
    #Fetch Usernames
    #:return List of user usernames:
    
    users = db.fetch()
    usernames = []
    for user in users.items:
        usernames.append(user['key'])
    return usernames


def validate_email(email):
    
    #Check Email Validity
    #:param email:
    #:return True if email is valid else False:
    
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$" #tesQQ12@gmail.com

    if re.match(pattern, email):
        return True
    return False


def validate_username(username):
    
    #Checks Validity of userName
    #:param username:
    #:return True if username is valid else False:
    

    pattern = "^[a-zA-Z0-9]*$"
    if re.match(pattern, username):
        return True
    return False


def sign_up():
    with st.form(key='signup', clear_on_submit=True):
        st.subheader(':green[Sign Up]')
        email = st.text_input(':blue[Correo]', placeholder='Ingresar Correo')
        username = st.text_input(':blue[Usuario]', placeholder='Ingresar Usuario')
        password1 = st.text_input(':blue[Contraseña]', placeholder='Ingresar Contraseña', type='password')
        password2 = st.text_input(':blue[Confirmar Contraseña]', placeholder='Confirmar Contraseña', type='password')

        if email:
            if validate_email(email):
                if email not in get_user_emails():
                    if validate_username(username):
                        if username not in get_usernames():
                            if len(username) >= 2:
                                if len(password1) >= 6:
                                    if password1 == password2:
                                        # Add User to DB
                                        hashed_password = stauth.Hasher([password2]).generate()
                                        insert_user(email, username, hashed_password[0])
                                        st.success('¡Cuenta Creada Satisfactoriamente!')
                                        st.balloons()
                                    else:
                                        st.warning('Contraseñas no coinciden')
                                else:
                                    st.warning('Contraseña es muy corta')
                            else:
                                st.warning('Usuario es muy corto')
                        else:
                            st.warning('¡Usuario ya existe!')

                    else:
                        st.warning('Usuario Inválido')
                else:
                    st.warning('¡Correo ya existe!')
            else:
                st.warning('Correo Inválido')

        btn1, bt2, btn3, btn4, btn5 = st.columns(5)

        with btn3:
            st.form_submit_button('Registrarse')
"""

def show_hide():
    st.session_state.hide = not st.session_state.hide

@st.cache_data(persist=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: local;
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(0,0,0,0);
    }}
    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    [data-testid="stVerticalBlock"]{{
    top: 1.5rem;
    }}
    [data-testid="StyledLinkIconContainer"]{{
    left: 0.2rem;
    font-family: "Play", Times, serif;
    font-size: large;
    color: white;
    }}
    [data-testid="stMarkdownContainer"]{{
    font-family: "Play";
    line-height: 1;
    }}
    [data-testid="baseButton-secondary"]{{
    background-color: gray;
    border-color: gray;
    color: white;
    }}
    [data-testid="stButton"] > button:hover {{
    background-color: gray;
    border-color: gray;
    color: black;
    }}
    </style>
    """ % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

def set_png_as_pages_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    pages_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,%s");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center 100px;
    }}
    [data-testid="element-container"] {{
    position: relative;
    top: -50px;
    }}
    [data-testid="baseButton-secondary"]{{
    position: absolute;
    left: 180px;
    top: 10px;
    }}
    [data-testid="stMarkdown"]{{
    display: inline-block;
    right: 180px;
    top: 60px;
    }}
    </style>
    """ % bin_str

    st.markdown(pages_bg_img, unsafe_allow_html=True)
    return

# sign_uo()







