import streamlit as st
from PIL import Image

# Give a title to our app
st.header('Resume and Cover Letter builder')

with st.form("doc_form"):
    col1, col2 = st.columns(2)  # Create two columns
    # TAKE User input what they want to generate:
    with col1:
        st.markdown(
            """
            <div style="text-align: center;">
                Select Document for generation:
            </div>
            """,
            unsafe_allow_html=True,
        )
        status = st.radio("", ('Resume', 'Cover Letter'))
    with col2: 
     image_url = "https://th.bing.com/th/id/OIP.lyXd0humrEprnVJ3RdTBLAHaHa?w=201&h=201&c=7&r=0&o=5&pid=1.7"
     st.image(image_url, width=170)
    # Conditional statement to print the selected document type
    if status == 'Resume':
        st.success("Resume")
    else:
        st.success("Cover Letter")

    text_field = st.text_area("Enter your profile description")

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

    submit_form = st.form_submit_button(label="Generate")

# Checking if the form is submitted
if submit_form:
    st.write("Generating " + status + "...") #Added more helpful output.
    st.write("Profile Description:", text_field) #added profile description display.
    # Here you would add the logic to generate the resume or cover letter
    # based on the 'status' and 'text_field' values.