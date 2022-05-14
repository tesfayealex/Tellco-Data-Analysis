from dashboard import overview, engagment, exprience, satisfaction
from multiapp import MultiApp
import streamlit as st
import sys
sys.path.insert(0, './scripts')

# import your app modules here

st.set_page_config(page_title="TellCo Telecom Analytics", layout="wide")

app = MultiApp()


st.sidebar.markdown("""
# TellCo's User Analytics
### Multi-Page App
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
### Modifications
\t- Page Folder Based Access
\t- Presentation changed to SideBar
""")

# Add all your application here
app.add_app("User Overview Analysis", overview.app)
app.add_app("User Engagement Analysis", engagment.app)
app.add_app("User Experience Analysis", exprience.app)
app.add_app("User Satisfaction Analysis", satisfaction.app)
# app.add_app("Predict Satisfaction", model_implementation.app)

# The main app
app.run()
