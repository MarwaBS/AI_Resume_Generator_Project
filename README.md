# AI Resume Generator

## Table of Contents

[Overview](#overview)

[The Program](#the-program)

[Presentation](#presentation)

[The Team](#the-team)

## Project Overview

### Overview

This project aims to create a user-friendly application designed to help users create professional and polished resumes quickly. The project leverages Python and Gradio to provide an interactive interface where users input their details, such as personal information, work experience, education, skills, and certifications. The application then formats the data into a structured resume template, ensuring clarity and professionalism.

### Key Features

- **AI-generated cover letters** tailored to job descriptions and company details.
- **AI-enhanced resumes** with optimized summaries, work experiences, and project descriptions.
- **Grammar and spelling corrections** using LanguageTool.
- **Conversion to multiple formats** (Markdown, HTML, and PDF).
- **Logging and error handling** for smooth operation.

## The Program

### Real World Application

The Resume Generator has real-world applications across various industries by streamlining the resume creation process for job seekers. Whether for recent graduates, career changers, or professionals looking to update their resumes, this tool provides a fast, efficient, and user-friendly way to craft well-structured, professional resumes.

Recruiters and hiring managers often prioritize well-formatted resumes, and this program ensures consistent styling, clear organization, and ATS (Applicant Tracking System) compatibility, improving the chances of landing interviews. Additionally, businesses and career coaching services can integrate this tool into their platforms to assist clients in resume-building, making it a valuable asset in the job market.

### Installation

#### Prerequisites

Ensure you have the following installed:

1. Python 3.8+
2. pip package manager
3. wkhtmltopdf (for PDF conversion)

#### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/resume-cover-letter-generator.git
   cd resume-cover-letter-generator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up OpenAI API key:
   ```python
   openai.api_key = "your-api-key-here"

### Usage

#### Generating a Cover Letter

Modify `test_user_info` with your details and run:

```bash
python cover_letter_generator.py
```

This will generate a Markdown file, an HTML file, and a PDF of the cover letter.

#### Generating a Resume

Modify `user_data` with your details and run:

```bash
python resume_generator.py
```

This will generate a professional resume in multiple formats.

### File Structure

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
|-- requirements.txt
|-- README.md
```

### Dependencies

- `openai`
- `jinja2`
- `markdown`
- `pdfkit`
- `wkhtmltopdf`
- `language_tool_python`
- `logging`

### Logging and Error Handling

- Logs are saved to `resume_generator.log` and `cover_letter_generator.log`.
- Errors in AI generation or PDF conversion are logged and displayed.

### License

MIT License

## Presentation

[AI Resume Generator Presentation](https://docs.google.com/presentation/d/1dYNcGzHZJ7riSncaC3UqS4uJGNvLJwGZ/edit?usp=sharing&ouid=115049080126679246379&rtpof=true&sd=true)

## The Team

[vinayakgrover](https://github.com/vinayakgrover)

[MarwaBS](https://github.com/MarwaBS)

[nabray07](https://github.com/nabray07)

[rgoldstein24](https://github.com/rgoldstein24)
