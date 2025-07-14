import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image


# Grade Calculation
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "D"


# Pass/Fail Status
def calculate_status(marks):
    return "Pass" if all(mark >= 40 for mark in marks) else "Fail"


# Generate Bar Chart
def generate_chart(subjects, marks, output_path):
    plt.figure(figsize=(6, 4))
    plt.bar(subjects, marks, color="skyblue")
    plt.title("Subject-wise Marks")
    plt.ylabel("Marks")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


# Generate PDF Marksheet
def generate_marksheet(data_row):
    name = data_row['Name']
    roll = data_row['Roll']
    semester = data_row['Semester']

    # New subject list
    subjects = ['Computer Network', 'Database Systems', 'EVS', 'IIS', 'System Software']
    marks = [data_row[subj] for subj in subjects]

    total = sum(marks)
    percentage = round(total / len(subjects), 2)
    grade = calculate_grade(percentage)
    status = calculate_status(marks)

    chart_path = f"{roll}_chart.png"
    generate_chart(subjects, marks, chart_path)

    pdf_path = f"{roll}_marksheet.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # College Logo
    try:
        elements.append(Image("logo.png", width=120, height=60))
    except:
        elements.append(Paragraph("<< College Logo Missing >>", styles['Normal']))
    elements.append(Spacer(1, 8))

    # Title and Info
    elements.append(Paragraph("D Y PATIL INTERNATIONAL UNIVERSITY", styles['Title']))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(f"<b>Name:</b> {name}", styles['Normal']))
    elements.append(Paragraph(f"<b>Roll No:</b> {roll}", styles['Normal']))
    elements.append(Paragraph(f"<b>Semester:</b> {semester}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Marks Table
    table_data = [['Subject', 'Marks']] + list(zip(subjects, marks))
    table = Table(table_data, colWidths=[200, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Summary
    elements.append(Paragraph(f"<b>Total Marks:</b> {total}", styles['Normal']))
    elements.append(Paragraph(f"<b>Percentage:</b> {percentage}%", styles['Normal']))
    elements.append(Paragraph(f"<b>Grade:</b> {grade}", styles['Normal']))
    elements.append(Paragraph(f"<b>Status:</b> {status}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Chart
    elements.append(Paragraph("Marks Distribution Chart", styles['Heading3']))
    elements.append(Image(chart_path, width=400, height=250))

    doc.build(elements)
    print(f"Generated: {pdf_path}")


# Main
if __name__ == "__main__":
    df = pd.read_csv("student_data.csv")
    for _, row in df.iterrows():
        generate_marksheet(row)
