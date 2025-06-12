from config import API_KEY
import openai
from docx import Document

# Configure the OpenAI client
client = openai.OpenAI(api_key=API_KEY)

def read_docx(filepath):
    doc = Document(filepath)
    return "\n".join([para.text for para in doc.paragraphs])

def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

resume = read_docx("./master_resume.docx")
job_desc = read_file("./job_description.txt")

prompts = [
    f"Compare this resume with the job description. What are the top 5 missing skills?",
    f"Rewrite the resume to better match the job.",
    f"Add important keywords from the job description into the resume.",
    f"Rewrite the summary section for better alignment.",
    f"Make the bullet points more achievement-focused.",
    f"afer everything make a doc file keeping all the formatting exactly same as it was in the resume file"

]

for i, prompt in enumerate(prompts):
    full_prompt = f"{prompt}\n\nResume:\n{resume}\n\nJob Description:\n{job_desc}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": full_prompt}]
    )

    with open(f"./output/prompt_{i+1}.txt", "w") as f:
        f.write(response.choices[0].message.content)
