import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate and create the gspread client
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], scope)
gc = gspread.authorize(creds)

# Open the Google Spreadsheet by its key
sheet = gc.open_by_key('1JHjy2V0pTLcUJqUwOxwcY1aa3x6BylZAiWCz097k0KI').sheet1  # Use the correct sheet name or index

# Streamlit app code
st.title('Google Spreadsheet Appender')
new_entry = st.text_input('Enter your entry:')
if st.button('Append to Google Spreadsheet'):
    if new_entry:
        sheet.append_row([new_entry])
        st.success('Entry appended successfully.')
    else:
        st.warning('Please enter some text to append.')
