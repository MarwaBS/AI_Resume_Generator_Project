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
openai.api_key = "api ker here"

def expand_summary_with_openai(user_info):
    try:
        prompt = f"""
        Given the user's profile, generate a concise and professional summary of their professional background in no more than 3 short sentences. 
        User's profile: {user_info["summary"]}
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are an AI assistant helping to generate a resume summary."},
                      {"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.7
        )
        user_info["summary"] = response["choices"][0]["message"]["content"].strip()
        return user_info
    except Exception as e:
        logging.error(f"Error expanding summary with OpenAI: {e}")
        return user_info

def expand_work_experience_with_openai(user_info):
    try:
        for exp in user_info["experience"]:
            prompt = f"""
            Summarize this job description into 3-4 concise bullet points focusing on key achievements and responsibilities:
            {exp['description']}
            """
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "You are an AI assistant summarizing work experience for a resume."},
                          {"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.7
            )
            exp["description"] = response["choices"][0]["message"]["content"].strip()
            time.sleep(1)  # Add a delay to avoid rate limits
        return user_info
    except Exception as e:
        logging.error(f"Error expanding work experience with OpenAI: {e}")
        return user_info

def expand_project_details_with_openai(user_info):
    try:
        if "projects" not in user_info or not user_info["projects"]:
            logging.warning("No projects found in user data. Skipping project expansion.")
            return user_info

        for project in user_info["projects"]:
            if "description" not in project:
                logging.warning(f"Project '{project.get('title', 'Untitled')}' is missing a description. Skipping.")
                continue

            prompt = f"""
            Expand the project description and tasks into concise, impactful details. 
            Make it sound like an achievement-driven summary that highlights key skills and technologies used:
            {project['description']}
            """
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "You are an AI assistant summarizing project details for a resume."},
                          {"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.7
            )
            project["description"] = response["choices"][0]["message"]["content"].strip()
            time.sleep(1)  # Add a delay to avoid rate limits

        return user_info
    except Exception as e:
        logging.error(f"Error expanding project details with OpenAI: {e}")
        return user_info

def render_template(template_path, context):
    """
    Render a Jinja2 template with the given context.
    """
    try:
        template = env.get_template(template_path)
        return template.render(context)
    except Exception as e:
        logging.error(f"Error rendering template: {e}")
        raise

def validate_data(data, required_fields):
    """
    Validate that all required fields are present in the data.
    """
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

def correct_text(text):
    """
    Correct spelling and grammar in the given text.
    """
    tool = LanguageTool('en-US')
    corrected_text = tool.correct(text)
    tool.close()  # Explicitly close the LanguageTool instance
    return corrected_text

def generate_resume(data):
    """
    Generate a resume using the resume template and AI-generated details.
    """
    try:
        # Step 1: Validate input data
        required_fields = ["name", "email", "phone", "skills", "experience", "education", "summary", "projects"]
        validate_data(data, required_fields)

        # Step 2: Expand details with AI
        expanded_data = expand_summary_with_openai(data)
        expanded_data = expand_work_experience_with_openai(expanded_data)
        expanded_data = expand_project_details_with_openai(expanded_data)

        # Step 3: Render template
        rendered_content = render_template("modern_minimalist_template.jinja2", expanded_data)

        # Step 4: Correct spelling and grammar
        corrected_content = correct_text(rendered_content)

        # Step 5: Save and convert to PDF
        user_filename = expanded_data["name"].replace(" ", "_").lower()
        os.makedirs("output", exist_ok=True)

        markdown_file = f"output/{user_filename}_resume.md"
        html_file = f"output/{user_filename}_resume.html"
        pdf_file = f"output/{user_filename}_resume.pdf"

        # Save Markdown
        with open(markdown_file, "w") as md_file:
            md_file.write(corrected_content)
        logging.info(f"Markdown file saved: {markdown_file}")

        # Convert Markdown to HTML
        html_content = markdown.markdown(corrected_content, extensions=['extra'])
        with open(html_file, "w") as html_f:
            html_f.write(f"""
            <html>
                <head>
                    <link rel="stylesheet" href="resume.css">
                </head>
                <body>
                    {html_content}
                </body>
            </html>
            """)
        logging.info(f"HTML file saved: {html_file}")

        # Convert HTML to PDF
        pdfkit.from_file(html_file, pdf_file, options={"enable-local-file-access": ""})
        logging.info(f"PDF file successfully generated: {pdf_file}")

    except Exception as e:
        logging.error(f"Error generating resume: {e}")
        raise

# # Sample data to generate the resume
# user_data = {
#     "name": "John Doe",
#     "email": "john.doe@example.com",
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

# # Generate the resume
# generate_resume(user_data)


