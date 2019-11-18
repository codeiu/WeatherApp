import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json

SCOPE = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/drive']
SECRET_FILE = "weather-app-key.json"
SPREADSHEET = "Weather App Info"

# Authentication
credentials = ServiceAccountCredentials.from_json_keyfile_name(SECRET_FILE,SCOPE)
gc = gspread.authorize(credentials)

# Get spreadsheet and create DataFrame
workbook = gc.open(SPREADSHEET)
sheet = workbook.sheet1
df = pd.DataFrame(sheet.get_all_records())

def getContacts():
    return df.values.tolist()
