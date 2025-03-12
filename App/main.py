from cover_letter_generator import generate_cover_letter
from resume_generator import generate_resume
def main():
    # Example user input (dictionary)
    user_data = {
        "title": "Data Scientist",  # Job title
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "123-456-7890",
        "address": "123 Main St, City, Country",
        "linkedin": "linkedin.com/in/johndoe",
        "github": "github.com/johndoe",
        "summary": "Passionate Data Scientist with 5+ years of experience in machine learning and AI.",
        "experience": [
            {
                "title": "Data Scientist",
                "company": "Tech Corp",
                "dates": "2022 - Present",
                "description": "Built ML models for predictive analytics and customer segmentation."
            },
            {
                "title": "Machine Learning Intern",
                "company": "AI Innovations",
                "dates": "2021 - 2022",
                "description": "Assisted in developing NLP pipelines for text classification."
            }
        ],
        "skills": "Python, TensorFlow, SQL, PyTorch, Scikit-learn",
        "projects": [
            {
                "name": "AI Resume Generator",
                "description": "Developed a resume builder using NLP to automate resume creation.",
                "technologies": "Python, Streamlit, SpaCy"
            }
        ],
        "education": [
            {
                "degree": "Master of Science in Data Science",
                "institution": "University of Tech",
                "dates": "2019 - 2021",
                "details": "Graduated with honors. Relevant coursework: Machine Learning, Big Data, Statistics."
            }
        ],
        "contact_info": {
            "email": "john@example.com",
            "phone": "123-456-7890",
            "address": "123 Main St, City, Country"
        }
    }

   
    # generate_resume(user_data)

    # Generate a cover letter
    cover_letter_data = {
        "name": user_data["name"],
        "address": user_data["address"],
        "phone": user_data["phone"],
        "email": user_data["email"],
        "date": "March 9, 2025",  # Current date
        "hiring_manager_name": "Jane Smith",  # Hiring manager's name
        "company_name": "Tech Corp",  # Company name
        "company_address": "456 Tech St, City, Country",  # Company address
        "job_title": "Data Scientist",  # Job title the user is applying for
        "platform": "LinkedIn",  # Platform where the job was found
        "quantifiable_achievement": "a 15% increase in customer engagement",  # Achievement
        "relevant_experience_or_skills": "machine learning, data analysis, and predictive modeling",  # Relevant skills/experience
        "previous_company": "AI Innovations",  # Previous company
        "key_achievement_or_responsibility": "developed NLP pipelines and predictive models",  # Achievement/responsibility
        "how_it_relates_to_the_job": "these skills will help in data-driven decision-making at Tech Corp",  # How it relates
        "what_interests_you_about_the_company_or_role": "the opportunity to work on impactful AI projects and innovative technologies"  # Interest in the role
    }
    
    generate_cover_letter(cover_letter_data)

if __name__ == "__main__":
    main()
