# page1.py
import streamlit as st
from PIL import Image
import time

st.header('Resume and Cover Letter builder')

with st.form(key='form1'):
    
    name = st.text_input("Full Name:", placeholder="e.g., John Doe")
    email = st.text_input("Email:", placeholder="e.g., john.doe@example.com")
    ph_number = st.text_input("Phone number:", placeholder="e.g., 123-456-7890")
    linkedIn = st.text_input("LinkedIn profile URL (optional):", placeholder="e.g., linkedin.com/in/johndoe")
    gitHub = st.text_input("GitHub profile (optional):", placeholder="e.g., github.com/johndoe")
    level = st.slider("Years of experience:", 1, 35)
    
    text_field = st.text_area("Enter your professional summary :")
    # Add CSS to make text bigger
    st.markdown(
        """
        <style>
        textarea {
            font-size: 1rem !important;
        }
        input {
            font-size: 1rem !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    
    submit_button1 = st.form_submit_button(label='Next')


if submit_button1:
    st.session_state['name'] = name
    st.session_state['email'] = email
    st.session_state['ph_number'] = ph_number
    st.session_state['linkedIn'] = linkedIn
    st.session_state['gitHub'] = gitHub
    st.session_state['level'] = level
    
    try:
        st.switch_page("pages/Resume(cont).py")
    except AttributeError:
        st.error("Please upgrade streamlit to version 1.25.0 or higher to use this feature.")
