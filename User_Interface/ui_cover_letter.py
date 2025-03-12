import streamlit as st

def cover_letter_section():
    st.subheader("Cover Letter Details")

    # Initialize session state for cover letter data
    if 'cover_letter_info' not in st.session_state:
        st.session_state.cover_letter_info = {}

    # Cover Letter Form
    hiring_manager = st.text_input("Hiring Manager Name (Optional):", placeholder="e.g., Jane Smith", value=st.session_state.cover_letter_info.get('hiring_manager', ''))
    job_title = st.text_input("Job Title You Are Applying For:", placeholder="e.g., Data Analyst", value=st.session_state.cover_letter_info.get('job_title', ''))
    company_name = st.text_input("Company Name:", placeholder="e.g., TechCorp Inc.", value=st.session_state.cover_letter_info.get('company_name', ''))
    job_description = st.text_area("Job Description (Paste the job description here):", value=st.session_state.cover_letter_info.get('job_description', ''))

    # Save Cover Letter Info
    if st.button("Save Cover Letter Info"):
        st.session_state.cover_letter_info = {
            'hiring_manager': hiring_manager,
            'job_title': job_title,
            'company_name': company_name,
            'job_description': job_description
        }
        st.success("Cover Letter Info Saved!")

    # Generate Cover Letter
    if st.button("Generate Cover Letter"):
        st.success("Cover Letter Generated!")  # Replace with actual cover letter generation logic