import streamlit as st

st.header('Resume and Cover Letter builder')
job_id=1
if 'form' not in st.session_state:
    st.session_state.form = {}

if 'jobs' not in st.session_state:
    st.session_state.jobs = []

# Initial Form Data Input
with st.form(key='initial_form'):
    st.session_state.form['job_title'] = st.text_input("Job title:")
    st.session_state.form['comp_name'] = st.text_input("Company:")
    st.session_state.form['job_desc'] = st.text_area("Job Description:")
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
    initial_submit = st.form_submit_button("Submit Current Job")

if st.button("Add Another job"):
    job_id = len(st.session_state.jobs) + 1
    st.session_state.jobs.append({
        'job_id': job_id,
        'job_title': '',
        'comp_name': '',
        'job_desc': ''
    })

for job in st.session_state.jobs:
    job_id = job['job_id']
    job['job_title'] = st.text_input(f"Job {job_id} - Title:", key=f"job_{job_id}_title")
    job['comp_name'] = st.text_input(f"Job {job_id} - Company:", key=f"job_{job_id}_company")
    job['job_desc'] = st.text_input(f"Job {job_id} - Description:", key=f"job_{job_id}_description")
    st.session_state.form[f"job_{job_id}_job_title"] = job['job_title']
    st.session_state.form[f"job_{job_id}_comp_name"] = job['comp_name']
    st.session_state.form[f"job_{job_id}_job_desc"] = job['job_desc']

if st.button("Submit All Data"):
    st.write("Form Data:")
    st.write(st.session_state.form)