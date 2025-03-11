import openai  # Import OpenAI API
import jinja2
import markdown
import pdfkit
import os
from language_tool_python import LanguageTool  # Import for spelling/grammar correction

# Configure OpenAI API
openai.api_key = "api key"

def correct_text(text):
    """
    Corrects spelling and grammar in the given text using language-tool-python.
    """
    tool = None
    try:
        tool = LanguageTool('en-US')  # Initialize language tool
        corrected_text = tool.correct(text)  # Correct grammar and spelling
        return corrected_text
    finally:
        if tool:
            tool.close()  # Explicitly close the LanguageTool instance

def render_template(template_path, context):
    """
    Render a Jinja2 template with the given context.
    """
    template_loader = jinja2.FileSystemLoader(searchpath="./templates")  # Load templates
    template_env = jinja2.Environment(loader=template_loader)  # Initialize Jinja2 environment
    template = template_env.get_template(template_path)  # Get specified template
    return template.render(context)  # Render template with provided context

def ai_generate_cover_letter(user_info, job_description, company_info):
    """
    Generate an AI-enhanced cover letter based on user profile, job description, and company info using OpenAI API.
    """
    prompt = f"""
    User Profile: {user_info}
    Job Description: {job_description}
    Company Information: {company_info}

    Based on this information, generate a professional, tailored cover letter for this job application.
    Start the letter with the user's contact information (name, email, phone) at the top.
    Follow this with the date, recipient's name, company name, and address.
    Use a salutation like "Dear [Recipient's Name]," (e.g., "Dear Ms. Smith,").
    Ensure the letter highlights the user's relevant skills, experience, and qualifications.
    Align the tone and language with industry standards and company expectations.
    Avoid redundancy and focus on demonstrating how the user fits perfectly for this job.
    Conclude the letter with "Sincerely, [User's Name]" without repeating the name again.
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        cover_letter = response["choices"][0]["message"]["content"].strip()
        return cover_letter
    except Exception as e:
        print(f"Error generating cover letter: {e}")
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

    corrected_cover_letter = correct_text(ai_cover_letter)  # Enhance text with grammar correction

    user_filename = data["name"].replace(" ", "_").lower()
    markdown_file = f"output/{user_filename}_cover_letter.md"
    html_file = f"output/{user_filename}_cover_letter.html"
    pdf_file = f"output/{user_filename}_cover_letter.pdf"

    # Save as Markdown
    with open(markdown_file, "w") as file:
        file.write(corrected_cover_letter)

    print(f"Cover letter successfully generated as {markdown_file}")

    # Render HTML and PDF
    try:
        context = {
            'user_name': data["name"],
            'cover_letter_text': corrected_cover_letter
        }
        html_content = render_template('cover_letter_template.jinja2', context)

        # Save as HTML
        with open(html_file, "w") as html_f:
            html_f.write(html_content)

        # Convert HTML to PDF
        pdfkit.from_file(html_file, pdf_file)
        print(f"Cover letter successfully converted to {pdf_file}")
    except Exception as e:
        print(f"Error converting cover letter to PDF: {e}")