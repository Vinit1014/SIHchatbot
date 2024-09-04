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
    results = """
Rajasthan Technical University Kota
Academic Calendar for odd/ Even Semester for Session 2024-25
Course: Bachelor of Technology (B.Tech) for odd Semester
Semester
I
III
V
VII
Induction Program
02.09.2024
Commencement of Classes
18.09.2024
01-08-2024
20-08-2024
20-08-2024
Commencement of First Mid Term
06.11.2024
26-09-2024
07-10-2024
07-10-2024
Commencement of Second Mid Term
05.12.2024
04-11-2024
28-11-2024
28-11-2024
Last Working Day
23.12.2024
23-11-2024
07-12-2024
07-12-2024
Commencement of Practical Exams
20.01.2025
25-11-2024
09-12-2024
09-12-2024
Commencement of Theory Exams
07.01.2025
10-12-2024
16-12-2024
17-12-2024
Course : Bachelor of Technology (B.Tech) for Even Semester
Semester
II
IV
VI
VIII
Commencement of Classes
03.02.2025
02-01-2025
02-01-2025
02-01-2025
First Mid Term
24.03.2025
17-02-2025
17-02-2025
17-02-2025
Second Mid Term
28.04.2025
24-03-2025
24-03-2025
24-02-2025
Last Working Day
10.05.2025
19-04-2025
19-04-2025
19-04-2025
Commencement of Practical Exams
12.05.2025
21-04-2025
21-04-2025
21-04-2025
Commencement of Theory Exams
26.05.2025
06-05-2025
05-05-2025
06-05-2025
Project (VIII)
10-05-2025 to 20-05-2025
Practical Training ( After II Sem.)
16-06-2025 to 30-06-2025
Practical Training (After IV Sem.)
19-05-2025 to 02-07-2025
Practical Training (After VI Sem.)
19-05-2025 to 02-07-2025
Course : Bachelor of Technology (B.Arch.) for odd Semester
Semester
I
III
V
VII
IX
Induction Program
02.09.2024				
Commencement of Classes
18.09.2024	
01-08-2024
20-08-2024
20-08-2024
20-08-2024
Commencement of First Mid Term
06.11.2024
26-09-2024
07-10-2024
07-10-2024
07-10-2024
Commencement of Second Mid Term
05.12.2024
04-11-2024
28-11-2024
28-11-2024
28-11-2024
Last Working Day
23.12.2024
23-11-2024
07-12-2024
07-12-2024
07-12-2024
Commencement of Practical Exams
20.01.2025
25-11-2024
09-12-2024
09-12-2024
09-12-2024
Commencement of Theory Exams
07.01.2025
10-12-2024
16-12-2024
17-12-2024
17-12-2024
Course : Bachelor of Technology (B.Arch.) for Even Semester
Semester
II
IV
VI
VIII
X
Commencement of Classes
03.02.2025
02-01-2025
02-01-2025
02-01-2025
02-01-2025
First Mid Term
24.03.2025
17-02-2025
17-02-2025
17-02-2025
17-02-2025
Second Mid Term
28.04.2025
24-03-2025
24-03-2025
24-02-2025
24-02-2025
Last Working Day
10.05.2025
19-04-2025
19-04-2025
19-04-2025
19-04-2025
Commencement of Practical Exams
12.05.2025
21-04-2025
21-04-2025
21-04-2025
21-04-2025
Commencement of Theory Exams
26.05.2025
06-05-2025
05-05-2025
06-05-2025
06-05-2025
Project (VIII)
10-05-2025 to 20-05-2025
Practical Training ( After II Sem.)
16-06-2025 to 30-06-2025
Practical Training (After IV Sem.)
19-05-2025 to 02-07-2025
Practical Training (After VI Sem.)
19-05-2025 to 02-07-2025
Course :Master of Technology (M.TECH) for Odd Semester
Semester
I
III
Commencement of Classes

15-07-2024
Commencement of First Mid Term

02-09-2024
Commencement of Second Mid Term

21-10-2024
Last Working Day

08-11-2024
Commencement of Practical Exams

11-11-2024
Commencement of Theory Exams

10-12-2024
Winter Break
Course :Master of Technology (M.TECH) for Even Semester
Semester
II
IV
Commencement of Classes

02-01-2025
First Mid Term

Second Mid Term

Last Working Day

Commencement of Practical Exams

Commencement of Theory Exams

Last date for Submission of Dissertation 30-06-2025
Summer Vacation
Course :Master of Architecture (M.ARCH) for Odd Semester
Semester
I
III
Commencement of Classes

15-07-2024
Commencement of First Mid Term

02-09-2024
Commencement of Second Mid Term

21-10-2024
Last Working Day

08-11-2024
Commencement of Practical Exams

11-11-2024
Commencement of Theory Exams

10-12-2024
Winter Break
Course : Bachelor of Technology (M.ARCH) for Even Semester
Semester
II
IV
Commencement of Classes

02-01-2025
First Mid Term

Second Mid Term

Last Working Day

Commencement of Practical Exams

Commencement of Theory Exams

Last date for Submission of Dissertation 30-06-2025
Summer Vacation
Course : Master of Business Administration (MBA) for Odd Semester
Semester
I
III
Commencement of Classes
18-09-2024
01-09-2024
Commencement of First Mid Term
06-11-2024
07-10-2024
Commencement of Second Mid Term
05-12-2024
11-11-2024
Last Working Day
23-12-2024
24-12-2024
Commencement of Practical Exams
25-01-2024
01-01-2025
Commencement of Theory Exams
07-01-2024	
08-01-2025
Winter Break
25-12-2024 to 31-12-2024
25-12-2024 to 31.12.2024
Course : Master of Business Administration (MBA) for Even Semester
Semester
II
IV
Commencement of Classes
03-02-2025
01-02-2025
First Mid Term
24-03-2025
03-03-2025
Second Mid Term
28-04-2025
21-04-2025
Last Working Day
10-05-2025
31-05-2025
Project Work
-	
01-06-2025 to 10-06-2025
Commencement of Practical Exams
12-05-2025
12-06-2025
Commencement of Theory Exams
27-05-2025
18-06-2025
Summer Training Project
14-06-2025 to 31-07-2025
Course :Master of Computer Application (MCA) for Odd Semester
Semester
I
III
Commencement of Classes
18-09-2024
01-09-2024
Commencement of First Mid Term
06-11-2024
07-10-2024
Commencement of Second Mid Term
05-12-2024
11-11-2024
Last Working Day
23-12-2024
24-12-2024
Commencement of Practical Exams
25-01-2024
01-01-2025
Commencement of Theory Exams
07-01-2024
08-01-2025
Winter Break
25-12-2024 to 31-12-2024
25-12-2024 to 31-12-2024
Course : Master of Computer Application (MCA) for Even Semester
Semester
II
IV
Commencement of Classes
03-02-2025
01-02-2025
First Mid Term
24-03-2025
03-03-2025
Second Mid Term
28-04-2025
21-04-2025
Last Working Day
10-05-2025
31-05-2025
Commencement of Practical Exams
12-05-2025
02-06-2025
Commencement of Theory Exams
27-05-2025
18-06-2025
Summer Industrial Training
14-06-2025 to 31-07-2025
Course : Bachelor of Non-Engineering (Non-Engineering) for odd Semester
Semester
I
III
V
VII
Induction Program

Commencement of Classes

01-08-2024
Commencement of First Mid Term

26-09-2024
Commencement of Second Mid Term

04-11-2024
Last Working Day

23-11-2024
Commencement of Practical Exams

25-11-2024
Commencement of Theory Exams

10-12-2024
Course : Bachelor of Non-Engineering (Non-Engineering) for Even Semester
Semester
II
IV
VI
VIII
Commencement of Classes
02-01-2025
First Mid Term

17-02-2025
Second Mid Term

24-03-2025
Last Working Day

19-04-2025
Commencement of Practical Exams

21-04-2025
Commencement of Theory Exams

06-05-2025
Project (VIII)
Practical Training ( After II Sem.)
16-06-2025 to 30-06-2025
Practical Training (After IV Sem.)
Practical Training (After VI Sem.)
Academic Calender M. Tech part-time 2023-24  Click here
Notice regarding amendment in period pf practical training for B.Tech. IV & VI Semester classes
Course: Bachelor’s Program in Non- Engineering (B.Des./BFA/BE/BFAD)
Course: Bachelor’s Program in Non- Engineering (B.Des./BFA/BE/BFAD)
Semester
II
IV
VI
VIII
 
Commencement of Classes
26.02.2024
 	 	 
First Mid Term
02.04.2024
 	 	 
Second Mid Term
03.06.2024
 	 	 
Last Working Day
10.06.2024
 	 	 
Commencement of Practical Exams
01.07.2024
 	 	 
Commencement of Theory Exams
19.06.2024
 	 	 
Project (VIII)
 
Practical Training (After II Sem.)
15.07.2024 To 31.07.2024
Practical Training (After IV Sem.)
 
Practical Training (After VI Sem.)
 
Commencement of Classes for next Odd Semesters (2023-24)
I
III
V
VII
01.08.2024
01.08.2024
 	 
Course: Master of Computer Applications (MCA) For Even Semester
Course: Master of Computer Applications (MCA) For Even Semester
Semester
II
IV
Commencement of Classes
01.03.2024
19.02.2024
First Mid Term
08.04.2024
26.03.2024
Second Mid Term
27.05.2024
01.05.2024
Last Working Day
15.06.2024
31.05.2024
Commencement of Practical Exams
18.06.2024
11.06.2024
Commencement of Theory Exams
27.06.2024
21.06.2024
Summer Training Project
15.07.2024 To 31.08.2024
Nil
Course: Master of Business Administration (MBA) For Even Semester
Course: Master of Business Administration (MBA) For Even Semester
Semester
II
IV
Commencement of Classes
01.03.2024
19.02.2024
First Mid Term
08.04.2024
26.03.2024
Second Mid Term
27.05.2024
01.05.2024
Last Working Day
15.06.2024
31.05.2024
Project Work
Nil
01.06.2024 To 10.06.2024
Commencement of Practical Exams
18.06.2024
11.06.2024
Commencement of Theory Exams
27.06.2024
21.06.2024
Summer Training Project
15.07.2024 To 31.08.2024
Nil
Course: Master of Architecture (M Arch.) For Even Semester
Course: Master of Architecture (M Arch.) For Even Semester
Semester
II
IV
Commencement of Classes
26.02.2024
02.02.2024
First Mid Term
02.04.2024
Second Mid Term
03.06.2024
Last Working Day
10.06.2024
Commencement of Practical Exams
01.07.2024
Commencement of Theory Exams
19.06.2024
Summer Vacation
Last date for submission of dissertation would be 30.07.2024
Course: Master of Technology (M.Tech.) For Even Semester
Course: Master of Technology (M.Tech.) For Even Semester
Semester
II
IV
Commencement of Classes
26.02.2024
02.02.2024
First Mid Term
02.04.2024
Second Mid Term
03.06.2024
Last Working Day
10.06.2024
Commencement of Practical Exams
01.07.2024
Commencement of Theory Exams
19.06.2024
Summer Vacation
Last date for submission of dissertation would be 30.07.2024
Course: Bachelor of Architecture (B.ARCH.)
Course: Bachelor of Architecture (B.ARCH.)
Semester
II
IV
VI
VIII
X
Commencement of Classes
26.02.2024
15.02.2024
15.02.2024
02.01.2024
02.01.2024
First Mid Term
02.04.2024
20.03.2024
20.03.2024
-
15.02.2024
Second Mid Term
03.06.2024
06.05.2024
06.05.2024
-
21.03.2024
Last Working Day
10.06.2024
31.05.2024
31.05.2024
-
20.04.2024
Commencement of Practical Exams
01.07.2024
03.06.2024
03.06.2024
-
22.04.2024
Commencement of Theory Exams
19.06.2024
14.06.2024
15.06.2024
-
02.05.2024
Course: Bachelor of Technology (B.TECH.)
Course: Bachelor of Technology (B.TECH.)
Semester
II
IV
VI
VIII
Commencement of Classes
26.02.2024
15.02.2024
15.02.2024
02.01.2024
First Mid Term
02.04.2024
20.03.2024
20.03.2024
15.02.2024
Second Mid Term
03.06.2024
06.05.2024
06.05.2024
21.03.2024
Last Working Day
10.06.2024
31.05.2024
31.05.2024
20.04.2024
Commencement of Practical Exams
01.07.2024
03.06.2024
03.06.2024
22.04.2024
Commencement of Theory Exams
19.06.2024
14.06.2024
15.06.2024
02.05.2024
Project (VIII)
06.05.2024 to 15.05.2024
Practical Training (After II Sem.)
15.07.2024 To 31.07.2024
Practical Training (After IV Sem.)
01.07.2024 To 17.08.2024
Practical Training (After VI Sem.)
01.07.2024 To 17.08.2024
Commencement of Classes for next Odd Semesters (2023-24)
I
III
V
VII
01.08.2024
01.08.2024
20.08.2024
20.08.2024

"""
    query = "Summarise the academic calendar for the Bachelor of Technology (B.Tech) for odd Semester"
    summary = generate_summary(results, query)
    print(summary)


if __name__ == '__main__':
    main()
