from fpdf import FPDF
import os
from datetime import datetime

class ResumePDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.set_y(15)
        self.cell(0, 5, "PROFESSIONAL RESUME", align="C")
        self.ln(5)
        self.set_draw_color(0, 0, 0)
        self.line(10, 22, 200, 22)
        self.ln(10)
    
    def add_section(self, title, content):
        self.set_font("Arial", "B", 12)
        self.set_fill_color(200, 220, 240)
        self.cell(0, 10, title, 0, 1, "L", 1)
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 5, content)
        self.ln(5)
    
    def add_skills(self, skills_list):
        self.set_font("Arial", "B", 12)
        self.set_fill_color(200, 220, 240)
        self.cell(0, 10, "SKILLS", 0, 1, "L", 1)
        self.set_font("Arial", "", 10)
        skills_text = "\n".join([f"- {skill}" for skill in skills_list])
        self.multi_cell(0, 5, skills_text)
        self.ln(5)

def generate_pdf_resume(user_data, filename):
    os.makedirs("outputs", exist_ok=True)
    pdf_path = os.path.join("outputs", filename)
    
    pdf = ResumePDF("P", "mm", "A4")
    pdf.add_page()
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, user_data["full_name"].upper(), 0, 1, "C")
    
    pdf.set_font("Arial", "", 10)
    contact_info = f"Email: {user_data['email']} | Phone: {user_data['phone']}"
    if user_data.get('location'):
        contact_info += f" | Location: {user_data['location']}"
    pdf.cell(0, 6, contact_info, 0, 1, "C")
    
    links = []
    if user_data.get('linkedin'):
        links.append(f"LinkedIn: {user_data['linkedin']}")
    if user_data.get('github'):
        links.append(f"GitHub: {user_data['github']}")
    if links:
        pdf.cell(0, 6, " | ".join(links), 0, 1, "C")
    
    pdf.ln(8)
    pdf.set_draw_color(150, 150, 150)
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(5)
    
    pdf.add_section("EDUCATION", user_data["education"])
    pdf.add_skills(user_data["skills"])
    
    if user_data["experience"] and user_data["experience"] != "No experience listed":
        pdf.add_section("EXPERIENCE", user_data["experience"])
    
    if user_data["projects"] and user_data["projects"] != "No projects listed":
        pdf.add_section("PROJECTS", user_data["projects"])
    
    if user_data["certifications"] and user_data["certifications"] != "No certifications listed":
        pdf.add_section("CERTIFICATIONS", user_data["certifications"])
    
    pdf.set_y(-25)
    pdf.set_font("Arial", "I", 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 10, f"Generated on {datetime.now().strftime('%B %d, %Y')}", 0, 0, "C")
    
    pdf.output(pdf_path)
    return pdf_path