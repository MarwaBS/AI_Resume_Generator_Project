import jinja2
import markdown
import pdfkit
import openai  # Import OpenAI API
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename="cover_letter_generator.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize Jinja2 environment with the templates folder
env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

# Configure OpenAI API
openai.api_key = "your api key here "

def ai_generate_cover_letter(user_info, job_description, company_info):
    """
    Generate an AI-enhanced cover letter based on user profile, job description, and company info using OpenAI.
    """
    try:
        prompt = f"""
        User Profile: {user_info}
        Job Description: {job_description}
        Company Information: {company_info}

        Based on this information, generate a professional, tailored cover letter for this job application. 
        Ensure the letter highlights the user's relevant skills, experience, and qualifications. 
        Align the tone and language with industry standards and company expectations. 
        Avoid redundancy and focus on demonstrating how the user fits perfectly for this job.
        Conclude the letter with "Sincerely, [User's Name]" without repeating the name again.
        """
        logging.info(f"Prompt sent to OpenAI: {prompt}")
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use GPT-3.5
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )
        if response.choices and response.choices[0].text:
            cover_letter = response.choices[0].text.strip()
            logging.info(f"Generated Cover Letter: {cover_letter}")
            return cover_letter
        else:
            logging.error("OpenAI API returned no valid response.")
            return None
    except openai.RateLimitError as e:
        logging.error(f"OpenAI API rate limit exceeded: {e}")
        return None
    except openai.APIError as e:
        logging.error(f"OpenAI API error: {e}")
        return None
    except Exception as e:
        logging.error(f"Error generating cover letter with OpenAI: {e}")
        return None

def generate_cover_letter(data):
    """
    Generate a cover letter using the AI-enhanced function with better formatting.
    """
    job_description = """
    Tech Corp is looking for a Data Scientist who is proficient in Python, TensorFlow, and machine learning techniques. 
    The ideal candidate will have experience with data analytics, predictive modeling, and customer segmentation. 
    They should be able to work with large datasets and communicate findings clearly to business stakeholders.
    """

    company_info = """
    Tech Corp is an innovative company at the forefront of machine learning and AI applications, with a strong focus on customer analytics and predictive insights.
    """

    ai_cover_letter = ai_generate_cover_letter(data, job_description, company_info)

    if not ai_cover_letter:
        print("Failed to generate cover letter.")
        return

    user_filename = data["name"].replace(" ", "_").lower()
    markdown_file = f"output/{user_filename}_cover_letter.md"
    html_file = f"output/{user_filename}_cover_letter.html"
    pdf_file = f"output/{user_filename}_cover_letter.pdf"

    with open(markdown_file, "w") as file:
        file.write(ai_cover_letter)

    print(f"Cover letter successfully generated as {markdown_file}")

    try:
        context = {
            'user_name': data["name"],
            'cover_letter_text': ai_cover_letter
        }
        html_content = render_template('cover_letter_template.jinja2', context)

        with open(html_file, "w") as html_f:
            html_f.write(html_content)

        pdfkit.from_file(html_file, pdf_file)
        print(f"Cover letter successfully converted to {pdf_file}")
    except Exception as e:
        print(f"Error converting cover letter to PDF: {e}")

test_user_info = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "555-1234",
    "skills": ["Python", "JavaScript", "HTML", "CSS", "Django", "React", "SQL"],
    "summary": "A highly skilled software engineer with expertise in developing applications and collaborating with teams."
}
test_job_description = "Tech Corp is looking for a Data Scientist proficient in Python, TensorFlow, and machine learning."
test_company_info = "Tech Corp is at the forefront of machine learning and AI applications."

print(ai_generate_cover_letter(test_user_info, test_job_description, test_company_info))
