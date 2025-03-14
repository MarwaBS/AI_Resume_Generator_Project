# AI Resume Generator

# AI Resume Generator

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [How It Works](#how-it-works)
  - [Personal Information](#personal-information)
  - [Education](#education)
  - [Projects](#projects)
  - [Work Experience](#work-experience)
  - [Cover Letter](#cover-letter)
- [The Program](#the-program)
- [Contributing](#contributing)
- [License](#license)
- [Presentation](#presentation)
- [The Team](#the-team)

---

## Project Overview

This project is a **user-friendly AI-powered Resume and Cover Letter Generator** designed to help users create professional, polished resumes and cover letters quickly. It leverages **Python**, **Machine Learning**, and **Natural Language Processing (NLP)** to generate tailored resumes and cover letters based on user input. The application provides an interactive interface powered by **Streamlit**, where users can input their details, such as personal information, work experience, education, skills, and certifications. The app then formats the data into structured templates, ensuring clarity and professionalism.

---

## Features
- **AI-Powered Resume Generation**: Generates professional resumes based on user input.
- **AI-Powered Cover Letters**: Tailors cover letters to job descriptions and company details.
- **Personal Information**: Supports adding contact details and professional summaries.
- **Natural Language Processing (NLP)**: Extracts key information from user input and understands context.
- **Keyword Optimization**: Suggests relevant keywords based on job descriptions.
- **Automatic Formatting**: Ensures consistent and professional formatting for resumes and cover letters.
- **Downloadable Formats**: Supports PDF, DOCX, and other common formats.
- **User-Friendly Interface**: Provides an intuitive and easy-to-use experience.

---

## Technologies Used
This project was built using the following technologies:

1. **OpenAI**: 
   - Used for generating or correcting text content in the resume and cover letter (e.g., professional summaries, job descriptions, etc.).
   - Ensures the text is polished, grammatically correct, and professional.

2. **Streamlit**: 
   - Used to create the user-friendly web interface for the Resume Builder App.
   - Allows users to input their information and interact with the app seamlessly.

3. **FPDF**: 
   - Used to generate the final resume and cover letter in PDF format.
   - Ensures the documents are well-formatted and ready for download.

4. **Jinja2**: 
   - Used for templating the resume and cover letter structure.
   - Allows dynamic insertion of user data into predefined HTML or Markdown templates.

5. **Markdown**: 
   - Used to format text content (e.g., bullet points, headings, etc.) in the resume and cover letter.
   - Ensures the content is clean and well-structured.

6. **PDFKit**: 
   - Used as an alternative PDF generation tool (if applicable).
   - Converts HTML or Markdown content into PDF format.

7. **LanguageTool (language_tool_python)**: 
   - Used for grammar and spelling correction.
   - Ensures the resume and cover letter content is error-free and professional.

8. **Logging**: 
   - Used to track and log errors, warnings, and other important events during the app's execution.
   - Helps with debugging and monitoring the app's performance.

9. **OS**: 
   - Used for file and directory operations (e.g., saving the generated PDF).
   - Ensures the app can handle file paths and system-related tasks.

10. **Time**: 
    - Used for timing operations (e.g., API call delays, performance tracking).
    - Ensures the app runs efficiently and handles time-based tasks.

---

## Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.8+
- `pdfkit`, `fpdf`, `jinja2`, `markdown`, `language_tool_python`, `openai`
- `wkhtmltopdf` (for PDF conversion)
- Streamlit for generating the user interface
## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- pdfkit , fdpf 
- wkhtmltopdf (for PDF conversion)
- Streamlit for generating user interface
### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/resume-cover-letter-generator.git
   cd resume-cover-letter-generator```

2.  Set up ```openai.api_key = "your-api-key-here"````

3. Run the application:
   streamlit run home.py # If using Streamlit.
   
   - Open your web browser and navigate to http://localhost:8501 (or the appropriate address).
   - Follow the on-screen instructions to input your information and generate your resume or cover letter.

### The Program

  **Real World Application**

The Resume Generator has real-world applications across various industries by streamlining the resume creation process for job seekers. Whether for recent graduates, career changers, or professionals looking to update their resumes, this tool provides a fast, efficient, and user-friendly way to craft well-structured, professional resumes.

Recruiters and hiring managers often prioritize well-formatted resumes, and this program ensures consistent styling, clear organization, and ATS (Applicant Tracking System) compatibility, improving the chances of landing interviews. Additionally, businesses and career coaching services can integrate this tool into their platforms to assist clients in resume-building, making it a valuable asset in the job market.

**How to Generate a Cover Letter**

Modify `test_user_info` with your details and run:

```bash
python cover_letter_generator.py
```

This will generate a Markdown file, an HTML file, and a PDF of the cover letter.

**How to Generate a Resume**

Modify `user_data` with your details and run:

```bash
python resume_generator.py
```

This will generate a professional resume in multiple formats.

**Program File Structure**

```
resume-cover-letter-generator/
|-- templates/
|   |-- resume_template.jinja2
|   |-- cover_letter_template.jinja2
|-- output/
|   |-- generated resume and cover letter files
|-- cover_letter_generator.py
|-- resume_generator.py
|-- resume.css
|-- home.py
|-- ui_resume.py
|-- ui_cover_letter.py
|-- requirements.txt
|-- README.md
```

**Dependencies**

- `openai`
- `jinja2`
- `markdown`
- `pdfkit`
- `wkhtmltopdf`
- `language_tool_python`
- `logging`

**Logging and Error Handling**

- Logs are saved to `resume_generator.log` and `cover_letter_generator.log`.
- Errors in AI generation or PDF conversion are logged and displayed.

## How It Works:

The AI Resume Builder utilizes the following technologies:

- ### Natural Language Processing (NLP)
The application uses **NLP techniques** to process and enhance user input. Specifically, it leverages the following:

1. **Text Correction**:
   - Uses **OpenAI's GPT models** to correct grammar, spelling, and sentence structure in user-provided text (e.g., professional summaries, job descriptions).
   - Ensures the content is polished, professional, and error-free.

2. **Keyword Extraction**:
   - Identifies and suggests relevant keywords based on job descriptions and user input.
   - Helps optimize resumes for **Applicant Tracking Systems (ATS)**.

3. **Content Generation**:
   - Generates professional summaries, job descriptions, and cover letter content using **OpenAI's language models**.
   - Ensures the generated content is tailored to the user's input and job requirements.

4. **Text Formatting**:
   - Uses **Markdown** and **Jinja2 templates** to structure and format the resume and cover letter content.
   - Ensures consistent and professional formatting across all generated documents.
- **Machine Learning (ML)**: The system employs ML models, such as GPT-based text generation models, to create personalized resume content. These models are trained on large datasets of resumes and job descriptions to ensure the generated content is relevant and professional.

- **Keyword Optimization**: The application uses keyword extraction algorithms to identify and suggest industry-specific keywords based on job descriptions. This ensures the resume is optimized for Applicant Tracking Systems (ATS) and increases the chances of passing initial screening processes.

 **Template Engine**: The application uses a templating engine like Jinja2 to dynamically insert user data into pre-designed resume templates. This ensures consistent and professional formatting across all generated resumes.

The process involves:

1. **User Input:** The user provides their information through the web interface.
2. **Data Processing:** The input is processed using NLP techniques to extract key information.
3. **Content Generation:** The AI models generate resume content based on the extracted information.
4. **Template Application:** The generated content is applied to the selected resume template.
5. **Formatting and Optimization:** The resume is formatted and optimized for keywords.
6. **Output:** The user can download the resume in the desired format.

![Image 1](perso_info.png)

**Personal Information**
The first screen of the application serves as the user input form, where users provide essential details for generating their resume or cover letter. It includes fields for the user's full name, email, phone number, LinkedIn URL, GitHub profile, years of experience, professional summary, and key skills. The interface is designed to be clean and intuitive, ensuring a seamless experience while entering information.

![Image 2](Education.png)

**Education**
The second screen allows users to input their educational background by providing details such as degree, institution, start date, end date, and additional details about their studies. Users can add multiple entries to accommodate various degrees or institutions they have attended. The interface includes an "Add Another" button, enabling users to input multiple schools seamlessly. Each entry is structured clearly, ensuring that users can easily review and edit their educational history before proceeding.

![Image 3](project.png)
**Projects**
The third screen focuses on the user's project experience, allowing them to input details for each project they have worked on. Users can enter the project title, a brief description outlining its purpose and impact, and the technologies used. The interface supports adding multiple projects with an "Add Another" button, ensuring users can showcase a diverse range of work. This structured approach helps highlight technical expertise and practical experience effectively.

![Image 4](work_exp.png)

**Work Experience**
The final screen is dedicated to the user's work experience, where they can input details about their previous and current job roles. Users enter their job title, company name, start date, end date, and a description of their responsibilities and achievements. Like the previous sections, this screen allows users to add multiple jobs, ensuring a comprehensive work history. This structured input helps create a well-rounded resume that effectively showcases professional experience.

![Image 4](cover_letter.png)

**Cover Letter**
The app also includes a dedicated section for generating AI-powered cover letters. Users can input the job title, company name, and job description, and the app will generate a professional cover letter tailored to the job. The cover letter is formatted using Jinja2 templates and can be downloaded in PDF format.

## Conclusion
The AI Resume Generator is a powerful tool designed to simplify the process of creating professional resumes and cover letters. By leveraging AI-powered content generation, natural language processing, and user-friendly interfaces, this application ensures that users can create polished, tailored resumes and cover letters in minutes. Whether you're a recent graduate, a career changer, or a seasoned professional, this tool helps you showcase your skills and experience effectively.

With features like automatic formatting, keyword optimization, and AI-powered cover letters, the app is designed to help users stand out in today's competitive job market. The intuitive interface and seamless integration of technologies like OpenAI, Streamlit, and FPDF make it easy for anyone to generate high-quality resumes and cover letters.

We encourage you to try the AI Resume Generator and experience the convenience of creating professional documents with just a few clicks. Your feedback and contributions are always welcome as we continue to improve and expand the capabilities of this tool.
 
### License

MIT License

## Presentation

[AI Resume Generator Presentation](https://docs.google.com/presentation/d/1dYNcGzHZJ7riSncaC3UqS4uJGNvLJwGZ/edit?usp=sharing&ouid=115049080126679246379&rtpof=true&sd=true)

## The Team

[vinayakgrover](https://github.com/vinayakgrover)

[MarwaBS](https://github.com/MarwaBS)

[nabray07](https://github.com/nabray07)

[rgoldstein24](https://github.com/rgoldstein24)
