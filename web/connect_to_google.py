import gspread
import os
from dotenv import load_dotenv

load_dotenv()
WEBAPP_PROJECT_ID = os.environ.get("WEBAPP_PROJECT_ID")
WEBAPP_PRIVATE_KEY_ID = os.environ.get("WEBAPP_PRIVATE_KEY_ID")
WEBAPP_PRIVATE_KEY = os.environ.get("WEBAPP_PRIVATE_KEY")
WEBAPP_CLIENT_EMAIL = os.environ.get("WEBAPP_CLIENT_EMAIL")
WEBAPP_CLIENT_ID = os.environ.get("WEBAPP_CLIENT_ID")
WEBAPP_CLIENT_X509_CERT_URL = os.environ.get("WEBAPP_CLIENT_X509_CERT_URL")

credentials = {
  "type": "service_account",
  "project_id": WEBAPP_PROJECT_ID,
  "private_key_id": WEBAPP_PRIVATE_KEY_ID,
  "private_key": WEBAPP_PRIVATE_KEY,
  "client_email": WEBAPP_CLIENT_EMAIL,
  "client_id": WEBAPP_CLIENT_ID,
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": WEBAPP_CLIENT_X509_CERT_URL
}

webapp_google_spread = gspread.service_account_from_dict(credentials)
sh = webapp_google_spread.open('flask-website')

sh_profile = sh.get_worksheet(0)
sh_contacts = sh.get_worksheet(1)
