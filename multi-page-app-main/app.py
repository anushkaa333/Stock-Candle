import streamlit as st
from multiapp import MultiApp
from apps import home, data, model # import your app modules here


#import libraries
import pyrebase

from datetime import datetime



#configuration
firebaseConfig = {
  'apiKey': "AIzaSyD77BfmCYnREsOm5ccGPcICR4NGXuzHqP4",
  'authDomain': "stock-eb968.firebaseapp.com",
  'projectId': "stock-eb968",
  'databaseURL': "https://stock-eb968-default-rtdb.firebaseio.com/",
  'storageBucket': "stock-eb968.appspot.com",
  'messagingSenderId': "983107711191",
  'appId': "1:983107711191:web:f655d875f4170c617bc092",
 ' measurementId': "G-HT1ETMS7J1"
}


#firebase authentication

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#database
db= firebase.database()
storage = firebase.storage()

st.sidebar.title("Login / Sign Up")

#authentication

choice = st.sidebar.selectbox('login/signup', ['Login', 'Sign up'])
email = st.sidebar.text_input('Enter email')
password = st.sidebar.text_input('Enter password', type = 'password')

if choice == 'Sign up':
    
    handle = st.sidebar.text_input('Please input your app handle name', value = 'Default')
    submit = st.sidebar.button('Create my account')

    if submit : 
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Your account is created successfully')
        st.balloons()

        #sign in
        user = auth.sign_in_with_email_and_password(email, password)
        db.child(user['localId']).child("Handle").set(handle)
        db.child(user['localId']).child("ID").set(user['localId'])
        st.title('Welcome ' + handle)
        st.info('Login via login drop down')
if choice == 'Login' :
    login = st.sidebar.button('Login')
    if login :
        user = auth.sign_in_with_email_and_password(email, password)
        #st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>')
        st.success('You have logged in successfully')
    



app = MultiApp()

#st.markdown("""
# Multi-Page App

#This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).

#""")



# Add all your application here
app.add_app("Home", home.app)
#app.add_app("Data", data.app)
app.add_app("Model", model.app)
# The main app
app.run()
