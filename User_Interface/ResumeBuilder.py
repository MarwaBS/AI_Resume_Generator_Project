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
# Write text

st.markdown(
    "<div style='text-align: center; font-size: 24px;'>Enter information for document creation</div>",
    unsafe_allow_html=True,
)
# Create a button, that when clicked, shows a text

st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <a href="http://localhost:8501/Resume" target="_self"><button style="width: 100px;">Next</button></a>
    </div>
    """,
    unsafe_allow_html=True,
)


