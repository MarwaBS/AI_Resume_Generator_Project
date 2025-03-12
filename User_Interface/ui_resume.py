import streamlit as st
import datetime
from ..App.resume_generator import generate_resume  # Import the resume generator

def resume_section():
    st.subheader("Resume Details")

    # Initialize session state for resume-related data
    if 'user_details' not in st.session_state:
        st.session_state.user_details = {}
    if 'education' not in st.session_state:
        st.session_state.education = []
    if 'projects' not in st.session_state:
        st.session_state.projects = []
    if 'work_experience' not in st.session_state:
        st.session_state.work_experience = []

    # Personal Information Section
    st.markdown("### Personal Information")
    with st.expander("Edit Personal Information", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name:", value=st.session_state.user_details.get('name', ''))
            email = st.text_input("Email:", value=st.session_state.user_details.get('email', ''))
            phone = st.text_input("Phone Number:", value=st.session_state.user_details.get('phone', ''))
        with col2:
            linkedIn = st.text_input("LinkedIn Profile:", value=st.session_state.user_details.get('linkedIn', ''))
            gitHub = st.text_input("GitHub Profile:", value=st.session_state.user_details.get('gitHub', ''))
            experience = st.slider("Years of Experience:", 1, 35, value=st.session_state.user_details.get('experience', 1))
        summary = st.text_area("Professional Summary:", value=st.session_state.user_details.get('summary', ''))
        skills = st.text_input("Skills (comma-separated):", value=st.session_state.user_details.get('skills', ''))

        # Submit button for personal information
        if st.button("Submit Personal Information"):
            st.session_state.user_details.update({
                'name': name,
                'email': email,
                'phone': phone,
                'linkedIn': linkedIn,
                'gitHub': gitHub,
                'experience': experience,
                'summary': summary,
                'skills': skills
            })
            st.success("Personal information saved!")

    # Display Personal Information
    st.markdown("#### Saved Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Name**: {st.session_state.user_details.get('name', '')}")
        st.write(f"**Email**: {st.session_state.user_details.get('email', '')}")
        st.write(f"**Phone**: {st.session_state.user_details.get('phone', '')}")
    with col2:
        st.write(f"**LinkedIn**: {st.session_state.user_details.get('linkedIn', '')}")
        st.write(f"**GitHub**: {st.session_state.user_details.get('gitHub', '')}")
        st.write(f"**Years of Experience**: {st.session_state.user_details.get('experience', '')}")
    st.write(f"**Professional Summary**: {st.session_state.user_details.get('summary', '')}")
    st.write(f"**Skills**: {st.session_state.user_details.get('skills', '')}")

    # Education Section
    st.markdown("### Education")

    # Initialize degree count in session state if not already present
    if 'degree_count' not in st.session_state:
        st.session_state.degree_count = len(st.session_state.education) if st.session_state.education else 1

    # Create a section for adding or editing education details
    with st.expander("Add Education", expanded=False):
        with st.form(key='education_form'):
            degree = st.text_input("Degree Title", value="")
            school = st.text_input("Institution", value="")
            finish_year = st.number_input("Graduation Year", min_value=1900, max_value=datetime.date.today().year, value=datetime.date.today().year)
            major = st.text_input("Major", value="")

            add_education_button = st.form_submit_button(label="Add Education")
        
        # If "Add Education" button is clicked
        if add_education_button:
            # Store the new education entry
            st.session_state.education.append({
                'title': degree,
                'institution': school,
                'finish_year': finish_year,
                'major': major
            })
            st.success("Education Details Added!")

    # Display the list of education details
    if st.session_state.education:
        st.markdown("#### Saved Education Details")
        for idx, edu in enumerate(st.session_state.education):
            with st.expander(f"Degree {idx + 1} - {edu['title']}"):
                st.write(f"**Institution**: {edu['institution']}")
                st.write(f"**Graduation Year**: {edu['finish_year']}")
                st.write(f"**Major**: {edu['major']}")

    # Projects Section
    st.markdown("### Projects")

    # Initialize project count in session state if not already present
    if 'project_count' not in st.session_state:
        st.session_state.project_count = len(st.session_state.projects) if st.session_state.projects else 1

    # Create a section for adding or editing project details
    with st.expander("Add Project", expanded=False):
        with st.form(key='project_form'):
            project_title = st.text_input("Project Title", value="")
            description = st.text_area("Description", value="")
            tech_used = st.text_input("Technologies Used", value="")

            add_project_button = st.form_submit_button(label="Add Project")
        
        # If "Add Project" button is clicked
        if add_project_button:
            # Store the new project entry
            st.session_state.projects.append({
                'title': project_title,
                'description': description,
                'tech_used': tech_used
            })
            st.success("Project Details Added!")

    # Display the list of project details
    if st.session_state.projects:
        st.markdown("#### Saved Project Details")
        for idx, project in enumerate(st.session_state.projects):
            with st.expander(f"Project {idx + 1} - {project['title']}"):
                st.write(f"**Description**: {project['description']}")
                st.write(f"**Technologies Used**: {project['tech_used']}")

    # Work Experience Section
    st.markdown("### Work Experience")

    # Initialize job count in session state if not already present
    if 'job_count' not in st.session_state:
        st.session_state.job_count = len(st.session_state.work_experience) if st.session_state.work_experience else 1

    # Create a section for adding or editing work experience details
    with st.expander("Add Work Experience", expanded=False):
        with st.form(key='work_experience_form'):
            job_title = st.text_input("Job Title", value="")
            company = st.text_input("Company Name", value="")
            location = st.text_input("Location", value="")
            start_date, end_date = st.columns(2)
            with start_date:
                start = st.date_input("Start Date", value=datetime.date.today())
            with end_date:
                end = st.date_input("End Date", value=datetime.date.today())
            description = st.text_area("Description", value="")

            add_work_experience_button = st.form_submit_button(label="Add Work Experience")
        
        # If "Add Work Experience" button is clicked
        if add_work_experience_button:
            # Store the new work experience entry
            st.session_state.work_experience.append({
                'title': job_title,
                'company': company,
                'location': location,
                'start': start,
                'end': end,
                'description': description
            })
            st.success("Work Experience Details Added!")

    # Display the list of work experience details
    if st.session_state.work_experience:
        st.markdown("#### Saved Work Experience Details")
        for idx, job in enumerate(st.session_state.work_experience):
            with st.expander(f"Job {idx + 1} - {job['title']}"):
                st.write(f"**Company**: {job['company']}")
                st.write(f"**Location**: {job['location']}")
                st.write(f"**Start Date**: {job['start']}")
                st.write(f"**End Date**: {job['end']}")
                st.write(f"**Description**: {job['description']}")

    # Generate Resume PDF
    if st.button("Generate Resume"):
        # Prepare data for resume generation
        resume_data = {
            "name": st.session_state.user_details.get('name', ''),
            "email": st.session_state.user_details.get('email', ''),
            "phone": st.session_state.user_details.get('phone', ''),
            "skills": st.session_state.user_details.get('skills', '').split(','),
            "experience": st.session_state.work_experience,
            "education": st.session_state.education,
            "summary": st.session_state.user_details.get('summary', ''),
            "projects": st.session_state.projects
        }

        # Generate the resume PDF
        try:
            pdf_file = generate_resume(resume_data)
            st.success("Resume Generated!")

            # Provide download button for the resume PDF
            with open(pdf_file, "rb") as file:
                st.download_button("Download Resume", file, file_name=pdf_file)
        except Exception as e:
            st.error(f"Error generating resume: {e}")

# Run the app
if __name__ == "__main__":
    resume_section()