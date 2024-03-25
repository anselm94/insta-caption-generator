from dotenv import load_dotenv

import streamlit as st

from app import show_app
from auth import show_login

load_dotenv()

if "auth" not in st.session_state:
    show_login()  # show the login page if not logged in
else:
    show_app()  # show the app if logged in
