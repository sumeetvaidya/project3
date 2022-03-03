#=======================
#Streamlit main app
#=======================

import streamlit as st
from multiapp import MultiApp

#import your app modules here
from apps import biometric_login, boarding_pass 

app = MultiApp()

st.sidebar.image("./app-logo.png", width=64)
# Add all your application here
app.add_app("Biometric Login", biometric_login.app)
app.add_app("Boarding Pass", boarding_pass.app)

# The main app
app.run()
