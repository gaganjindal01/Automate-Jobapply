# 🤖 Automate-Jobapply

A Python tool that tailors your resume to a specific job posting using the OpenAI API. Feed it your master resume and a job description, and it produces targeted analysis and rewrites.

## What it does

For each run it generates:

1. **Gap analysis** — the top 5 skills the job asks for that your resume is missing
2. **Tailored rewrite** — the resume rewritten to better match the posting
3. **Keyword injection** — important keywords from the job description worked into the resume
4. **Summary rewrite** — a summary section aligned to the role
5. **Achievement-focused bullets** — bullet points reframed around impact

Outputs are saved as text files in `Output/`.

## Usage

```bash
pip install openai python-docx

export OPENAI_API_KEY="sk-..."

# place your files:
#   master_resume.docx     — your master resume
#   job_description.txt    — the job posting text

python Scripts/resume_editor.py
```

## Stack

Python · OpenAI API · python-docx
