import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Resume and Cover Letter Builder", page_icon="\U0001F4C4", layout="wide")

# App Header with Logo
st.markdown("""
    <div style="text-align: center;">
        <h1 style='color: #2E86C1;'>\U0001F4C4 Resume and Cover Letter Builder</h1>
        <img src="https://th.bing.com/th/id/OIP.lyXd0humrEprnVJ3RdTBLAHaHa?w=201&h=201&c=7&r=0&o=5&pid=1.7" width="150">
        <p style='font-size: 18px;'>Effortlessly create professional resumes and cover letters.</p>
    </div>
    """, unsafe_allow_html=True)

# Initialize session state for saving data
if 'user_details' not in st.session_state:
    st.session_state.user_details = {}

# Sidebar Navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Resume", "Cover Letter"])

# Home Page
if page == "Home":
    st.subheader("Welcome to the Resume and Cover Letter Builder!")

    # Ask the user what they want to generate
    st.write("Please select what you would like to generate:")
    option = st.radio(
        "Choose an option:",
        ["Generate Resume Only", "Generate Resume + Cover Letter"],
        index=0  # Default to "Generate Resume Only"
    )

    # Save the user's choice in session state
    if option == "Generate Resume Only":
        st.session_state.user_details['resume'] = True
        st.session_state.user_details['cover'] = False
    else:
        st.session_state.user_details['resume'] = True
        st.session_state.user_details['cover'] = True

    # Display a message based on the user's choice
    if st.session_state.user_details['resume'] and not st.session_state.user_details['cover']:
        st.success("You have chosen to generate a **Resume Only**. Navigate to the **Resume** section using the sidebar.")
    elif st.session_state.user_details['resume'] and st.session_state.user_details['cover']:
        st.success("You have chosen to generate a **Resume + Cover Letter**. Navigate to the **Resume** and **Cover Letter** sections using the sidebar.")

# Resume Section
if page == "Resume":
    from ui_resume import resume_section
    resume_section()

# Cover Letter Section
if page == "Cover Letter":
    from ui_cover_letter import cover_letter_section
    cover_letter_section()

st.sidebar.markdown("---")
st.sidebar.info("Built with Streamlit")