import streamlit as st
import streamlit_google_oauth as oauth

client_id = st.secrets["GOOGLE_CLIENT_ID"]
client_secret = st.secrets["GOOGLE_CLIENT_SECRET"]
redirect_uri = st.secrets["GOOGLE_REDIRECT_URI"]

login_info = oauth.login(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        logout_button_text="Logout",
    )
if login_info:
    user_id, user_email = login_info
    st.write(f"Welcome {user_email}")