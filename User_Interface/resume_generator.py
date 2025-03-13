import jinja2
import markdown
import pdfkit
import openai  # Import OpenAI API
import os
import logging
import time
from language_tool_python import LanguageTool  # For spelling/grammar correction

# Configure logging
logging.basicConfig(filename="resume_generator.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize Jinja2 environment with the templates folder
env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

# Configure OpenAI API
openai.api_key = "api key"

def expand_text_with_openai(prompt, system_message):
    """
    Function to expand text using OpenAI API with error handling.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": system_message},
                      {"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        logging.error(f"OpenAI API error: {e}")
        return None

def expand_summary(user_info):
    prompt = f"""Given the user's profile, generate a professional summary:
    {user_info["summary"]}"""
    summary = expand_text_with_openai(prompt, "You generate concise professional summaries.")
    if summary:
        user_info["summary"] = summary
    return user_info

def expand_experience(user_info):
    for exp in user_info.get("experience", []):
        prompt = f"""Summarize this job into bullet points:
        {exp['description']}"""
        description = expand_text_with_openai(prompt, "You summarize work experiences professionally.")
        if description:
            exp["description"] = description
        time.sleep(1)
    return user_info

def expand_projects(user_info):
    for project in user_info.get("projects", []):
        if "description" in project:
            prompt = f"""Expand this project description professionally:
            {project['description']}"""
            description = expand_text_with_openai(prompt, "You summarize project details professionally.")
            if description:
                project["description"] = description
            time.sleep(1)
    return user_info

def render_template(template_path, context):
    try:
        template = env.get_template(template_path)
        return template.render(context)
    except Exception as e:
        logging.error(f"Template rendering error: {e}")
        return ""

def correct_text(text):
    tool = LanguageTool('en-US')
    corrected_text = tool.correct(text)
    tool.close()
    return corrected_text
import re

import re

def clean_text(text):
    """
    Cleans the text by replacing non-ASCII characters with a hyphen.
    """
    return re.sub(r"[^\x00-\x7F]+", "-", text)

def clean_user_data(data):
    """
    Applies cleaning function to relevant fields in user data.
    Specifically targets the 'duration' field in the 'experience' section.
    """
    if "experience" in data:
        for exp in data["experience"]:
            if "duration" in exp:
                exp["duration"] = clean_text(exp["duration"])
    return data

def generate_resume(data):
    try:
        # Step 1: Clean user data
        data = clean_user_data(data)

        # Step 2: Validate required fields
        required_fields = ["name", "email", "phone", "skills", "experience", "education", "summary", "projects"]
        if any(field not in data for field in required_fields):
            raise ValueError("Missing required fields in user data.")
        
        # Step 3: Expand sections with AI
        data = expand_summary(data)
        data = expand_experience(data)
        data = expand_projects(data)

        # Debug: Print the data being passed to the template
        # print("Data being passed to the template:", data)

        # Step 4: Render template
        rendered_content = render_template("modern_minimalist_template.jinja2", data)
        corrected_content = correct_text(rendered_content)
        
        # Step 5: Save files
        os.makedirs("output", exist_ok=True)
        user_filename = data["name"].replace(" ", "_").lower()
        markdown_file = f"output/{user_filename}_resume.md"
        html_file = f"output/{user_filename}_resume.html"
        pdf_file = f"output/{user_filename}_resume.pdf"
        
        # Save Markdown
        with open(markdown_file, "w") as md_file:
            md_file.write(corrected_content)
        
        # Convert Markdown to HTML
        html_content = markdown.markdown(corrected_content, extensions=['extra'])
        with open(html_file, "w") as html_f:
            html_f.write(f"""
            <html>
                <head>
                    <link rel="stylesheet" href="styles.css">
                </head>
                <body>
                    {html_content}
                </body>
            </html>
            """
            )
        
        # Convert HTML to PDF
        pdfkit.from_file(html_file, pdf_file, options={"enable-local-file-access": ""})
        logging.info(f"PDF successfully generated: {pdf_file}")
    except Exception as e:
        logging.error(f"Resume generation error: {e}")
        raise
# # Sample data to generate the resume
# user_data = {
#     "name": "Alex Doe",
#     "email": "Alex.doe@example.com",
#     "phone": "555-1234",
#     "skills": ["Python", "JavaScript", "HTML", "CSS", "Django", "React", "SQL"],
#     "experience": [
#         {
#             "company": "TechCorp",
#             "role": "Software Engineer",
#             "location": "San Francisco, CA",
#             "duration": "June 2018 - Present",
#             "description": "Led a team of 5 engineers to build a customer-facing web application.\nCollaborated with design and product teams to implement new features.\nOptimized backend APIs to reduce response times by 30%."
#         },
#         {
#             "company": "WebWorks",
#             "role": "Junior Developer",
#             "location": "Austin, TX",
#             "duration": "January 2016 - May 2018",
#             "description": "Developed internal tools to automate manual processes.\nWrote unit tests and maintained code quality across projects."
#         }
#     ],
#     "education": [
#         {
#             "degree": "B.Sc. in Computer Science",
#             "institution": "University of Example",
#             "year": "2015",
#             "major": "Computer Science"
#         }
#     ],
#     "summary": "A highly skilled software engineer with 5+ years of experience in developing scalable web applications and leading cross-functional teams. Passionate about solving challenging problems using modern technologies.",
#     "projects": [
#         {
#             "title": "Personal Finance App",
#             "technologies": ["React", "Node.js", "MongoDB"],
#             "description": "A personal finance tracker that helps users manage expenses and set savings goals."
#         },
#         {
#             "title": "Blog Platform",
#             "technologies": ["Django", "PostgreSQL", "AWS"],
#             "description": "A blog platform allowing users to create, edit, and share posts securely."
#         }
#     ]
# }
# generate_resume(user_data)