from groq import Groq
import json
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

GROQ_API = os.getenv("GROQ_API")
print(GROQ_API)

def generate_summary(results, query):
    client = Groq(api_key=GROQ_API)
    completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "system",
            "content": f"""
                You are a virtual assistant for students wishing to get into Government colleges of Rajasthan, India.
                Your task is to answer the students' / parents or guardians' queries regarding the admission process, eligibility criteria, and other details aobut hostels, scholarships, and other facilities.
                Along with the query, youre provided with the following context: "{results}"
                You have been asked the following question: "{query}
                Be factually correct and provide the most relevant information to the user."
            """
        },
    ],
    temperature=0.2,
    max_tokens=1700,
    top_p=1,
    stream=False,
    stop=None,
    )

    return completion.choices[0].message.content

def main():
    results = ''''''
    query = "Summarise the academic calendar for the Bachelor of Technology (B.Tech) for odd Semester"
    summary = generate_summary(results, query)
    print(summary)


if __name__ == '__main__':
    main()
