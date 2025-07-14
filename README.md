# -AUTOMATED-REPORT-GENERATION

*COMPANY*: CODETECH IT SOLUTIONS
  
*NAME*: PRATHMESH RATHOD

*INTERN ID*: CT12DK801

*DOMAIN*: Python Programming

*DURATION*: 12 WEEKS  

*MENTOR*: NEELA SANTOSH

*DESCRIPTION*: The Student Marksheet Report Generator is a Python-based automation project designed to streamline the process of generating academic marksheets for students at D Y Patil International University. This project aims to reduce the manual effort required in preparing student result reports, improving both accuracy and efficiency. It reads student data from a structured CSV file and produces a personalized PDF marksheet for each student, complete with subject-wise marks, total, percentage, grade, status (Pass/Fail), and a visual representation of marks through bar charts. The report is designed to be professional and university-ready, incorporating elements such as the university logo and a clearly formatted layout, making it suitable for academic institutions looking to digitize their internal report systems.

The data input is provided via a CSV file named student_data.csv, which includes student information such as Roll Number, Name, Semester, and marks in five key subjects: Computer Network, Database Systems, Environmental Studies (EVS), Information and Internet Security (IIS), and System Software. The project uses Python’s pandas library for reading and processing this data, enabling quick handling of multiple records. Each student's record is processed individually, and the program calculates their total marks and percentage automatically. A grade is assigned based on the percentage using a standard academic grading scale. Furthermore, a Pass/Fail status is determined by checking whether the student has scored a minimum of 40 marks in each subject, ensuring the result is not only computed but also evaluated according to academic rules.

To make the marksheet visually appealing and informative, the project integrates matplotlib for generating bar charts. These charts display subject-wise marks in a graphical format, giving a quick visual understanding of student performance. The final PDF report is generated using the ReportLab library, which allows structured document creation. The report includes the D Y Patil International University logo at the top, followed by student details, a tabular representation of subject marks, overall result summary, and the generated performance chart. The layout is clean and professional, mirroring real-world university marksheets.

This automated approach significantly reduces the chances of human error that may occur during manual data entry or calculations. It is highly scalable; the program can generate marksheets for any number of students by simply updating the CSV file. The codebase is modular and maintainable, making it easy for institutions to extend the functionality, such as adding attendance, remarks, digital signatures, or exporting results to databases or email systems. It can be used in semester result processing, progress reporting, and annual result declarations across departments.

In terms of real-world application, this system is highly applicable for universities, colleges, schools, and coaching institutions where large volumes of result data need to be processed and delivered in a short time. It also serves as an excellent academic project to showcase the use of Python in real-life automation, file handling, data visualization, and report generation. With minimal setup, the system provides high-quality, print-ready results for academic administration. This project not only meets the requirements of Internship Task 2 under CodTech's guidelines but also stands out as a complete utility for automated academic reporting.
