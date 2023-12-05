import requests
import streamlit as st

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Realty Watchers", page_icon=":computer:", layout="wide")
style = "<style>h1, h2, h3 {text-align: center;}</style>"
st.markdown(style, unsafe_allow_html=True)
# ---- HEADER SECTION ----
col1, col2, col3 = st.columns(3)

with col1:
    st.image('logo.png', caption='')

with col2:
    st.write(' ')
    st.header("*****Realty Watchers*****")
    st.subheader("     We allow you to keep up with fast moving invesment property by doing the tedious work of checking hourly for you.")

with col3:
    st.image('logo.png', caption='')
# ---- WHAT I DO ----
with st.container():
        st.subheader(
            """
                           If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any oportunities.
                           Please contact me William.Brenza@gmail.com
            """
        )
    #with right_column:
       
      
    
