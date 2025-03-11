import streamlit as st

# Give a title to our app
st.markdown("<h1 style='text-align: center;'>Resume and Cover Letter builder</h1>", unsafe_allow_html=True)

st.markdown(
            """
            <div style="text-align: center;">
                
            </div>
            """,
            unsafe_allow_html=True,
        )
from PIL import Image
image_url = "https://th.bing.com/th/id/OIP.lyXd0humrEprnVJ3RdTBLAHaHa?w=201&h=201&c=7&r=0&o=5&pid=1.7"
st.markdown(
            f"""
    <div style="display: flex; justify-content: center;">
        <img src="{image_url}" width="300">
    </div>
            """,
            unsafe_allow_html=True,
        )
st.markdown(
            """
            <div style="text-align: center;">
                Enter Information for document generation
            </div>
            """,
            unsafe_allow_html=True,
        )
st.markdown("""
    <style>
    .stRadio [role=radiogroup]{
        align-items: center;
        justify-content: center;
    }
    </style>
""",unsafe_allow_html=True)
