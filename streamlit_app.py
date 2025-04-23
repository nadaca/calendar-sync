import streamlit as st

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from datetime import datetime, timedelta

import pandas as pd
df = pd.DataFrame()


CLIENT_CONFIG = {'web': {
    'client_id': st.secrets["client_id"],
    'project_id': st.secrets["project_id"],
    'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
    'token_uri': 'https://www.googleapis.com/oauth2/v3/token',
    'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
    'client_secret': st.secrets["client_secret"],
    'redirect_uris': st.secrets["redirect_uris"]}}

SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    flow = InstalledAppFlow.from_client_config(
        CLIENT_CONFIG, SCOPES)
    creds = flow.run_local_server(host='localhost', port=8502)

    service = build('calendar', 'v3', credentials=creds)

    # Feature 1: List all calendars
    print("Fetching all calendars:")
    calendar_list = service.calendarList().list().execute().get('items', [])
    df = pd.DataFrame(calendar_list)

    st.dataframe(df, use_container_width=True,hide_index=True)

if __name__ == '__main__':
    main()