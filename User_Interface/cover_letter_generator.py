import openai  # Import OpenAI API
import jinja2
import markdown
import pdfkit
import os
from language_tool_python import LanguageTool  # Import for spelling/grammar correction
from datetime import datetime  # For current date

# Configure OpenAI API
openai.api_key ="api ki "
# 
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
    current_date = datetime.now().strftime("%B %d, %Y")  # Get current date
    prompt = f"""
    User Profile: {user_info}
    Job Description: {job_description}
    Company Information: {company_info}

    Based on this information, generate a professional, tailored cover letter for this job application.
    Start the letter with the user's contact information (name: {user_info['name']}, email, phone) at the top.
    Follow this with the date ({current_date}), recipient's name, company name, and address.
    Use a salutation like "Dear [Recipient's Name]," (e.g., "Dear {user_info['hiring_manager']},").
    Ensure the letter highlights the user's relevant skills, experience, and qualifications.
    Align the tone and language with industry standards and company expectations.
    Avoid redundancy and focus on demonstrating how the user fits perfectly for this job.
    Conclude the letter with "Sincerely, {user_info['name']}" without repeating the name again.
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
    job_description = data.get("job_description", "")
    company_info = f"{data.get('company_name', '')} is looking for a {data.get('job_title', '')}."

    ai_cover_letter = ai_generate_cover_letter(data, job_description, company_info)

    if not ai_cover_letter:
        print("Failed to generate cover letter.")
        return None

    # Remove square brackets around the user's name
    ai_cover_letter = ai_cover_letter.replace(f"[{data['name']}]", data['name'])

    corrected_cover_letter = correct_text(ai_cover_letter)  # Enhance text with grammar correction

    return corrected_cover_letter

def save_cover_letter(data, cover_letter):
    """
    Save the generated cover letter to a file.
    """
    user_filename = data["name"].replace(" ", "_").lower()
    os.makedirs("output", exist_ok=True)  # Create output directory if it doesn't exist

    # Save as Markdown
    markdown_file = f"output/{user_filename}_cover_letter.md"
    with open(markdown_file, "w") as file:
        file.write(cover_letter)
    print(f"Cover letter successfully saved as {markdown_file}")

    # Save as HTML and PDF
    try:
        context = {
            'user_name': data["name"],
            'cover_letter_text': cover_letter
        }
        html_content = render_template('cover_letter_template.jinja2', context)

        # Save as HTML
        html_file = f"output/{user_filename}_cover_letter.html"
        with open(html_file, "w") as html_f:
            html_f.write(html_content)

        # Convert HTML to PDF
        pdf_file = f"output/{user_filename}_cover_letter.pdf"
        pdfkit.from_file(html_file, pdf_file)
        print(f"Cover letter successfully converted to {pdf_file}")
    except Exception as e:
        print(f"Error converting cover letter to PDF: {e}")

# Example usage
# if __name__ == "__main__":
#     user_data = {
#         "name": "John Doe",
#         "email": "john.doe@example.com",
#         "phone": "(123) 456-7890",
#         "hiring_manager": "Jane Smith",
#         "job_title": "Data Scientist",
#         "company_name": "Tech Corp",
#         "job_description": """
#         Tech Corp is looking for a Data Scientist who is proficient in Python, TensorFlow, and machine learning techniques.
#         The ideal candidate will have experience with data analytics, predictive modeling, and customer segmentation.
#         They should be able to work with large datasets and communicate findings clearly to business stakeholders.
#         """
#     }

#     cover_letter = generate_cover_letter(user_data)
#     if cover_letter:
#         save_cover_letter(user_data, cover_letter)