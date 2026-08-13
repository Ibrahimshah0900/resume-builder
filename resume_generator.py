from fpdf import FPDF
import os
from datetime import datetime

class ResumeTemplate1(FPDF):
    """Template 1: Classic Professional - Blue theme"""
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
    
    def header(self):
        self.set_font("Arial", "B", 11)
        self.set_text_color(30, 80, 150)
        self.cell(0, 5, "PROFESSIONAL RESUME", align="C")
        self.ln(3)
        self.set_draw_color(30, 80, 150)
        self.line(15, 20, 195, 20)
        self.ln(10)
    
    def add_section(self, title, content):
        self.set_font("Arial", "B", 11)
        self.set_fill_color(210, 225, 245)
        self.set_text_color(30, 80, 150)
        self.cell(0, 8, f" {title}", 0, 1, "L", 1)
        self.set_font("Arial", "", 10)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 5, content)
        self.ln(2)
    
    def add_skills(self, skills_list):
        self.set_font("Arial", "B", 11)
        self.set_fill_color(210, 225, 245)
        self.set_text_color(30, 80, 150)
        self.cell(0, 8, " SKILLS", 0, 1, "L", 1)
        self.set_font("Arial", "", 10)
        self.set_text_color(0, 0, 0)
        skills_text = "\n".join([f"- {skill}" for skill in skills_list])
        self.multi_cell(0, 5, skills_text)
        self.ln(2)


class ResumeTemplate2(FPDF):
    """Template 2: Modern - Green theme with clean style"""
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
    
    def header(self):
        self.set_font("Arial", "B", 11)
        self.set_text_color(0, 120, 80)
        self.cell(0, 5, "RESUME", align="C")
        self.ln(3)
        self.set_draw_color(0, 120, 80)
        self.line(15, 20, 195, 20)
        self.ln(10)
    
    def add_section(self, title, content):
        self.set_font("Arial", "B", 11)
        self.set_text_color(0, 120, 80)
        self.cell(0, 8, f"▸ {title}", 0, 1, "L")
        self.set_draw_color(200, 200, 200)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(2)
        self.set_font("Arial", "", 10)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 5, content)
        self.ln(2)
    
    def add_skills(self, skills_list):
        self.set_font("Arial", "B", 11)
        self.set_text_color(0, 120, 80)
        self.cell(0, 8, f"▸ SKILLS", 0, 1, "L")
        self.set_draw_color(200, 200, 200)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(2)
        self.set_font("Arial", "", 10)
        self.set_text_color(0, 0, 0)
        skills_text = "\n".join([f"• {skill}" for skill in skills_list])
        self.multi_cell(0, 5, skills_text)
        self.ln(2)


class ResumeTemplate3(FPDF):
    """Template 3: Minimal - Dark header with clean design"""
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
    
    def header(self):
        self.set_font("Arial", "B", 12)
        self.set_text_color(255, 255, 255)
        self.set_fill_color(40, 40, 60)
        self.cell(0, 12, "  RESUME", 0, 1, "L", 1)
        self.ln(5)
    
    def add_section(self, title, content):
        self.set_font("Arial", "B", 11)
        self.set_text_color(40, 40, 60)
        self.cell(0, 8, f"   {title}", 0, 1, "L")
        self.set_draw_color(40, 40, 60)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(2)
        self.set_font("Arial", "", 10)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 5, content)
        self.ln(2)
    
    def add_skills(self, skills_list):
        self.set_font("Arial", "B", 11)
        self.set_text_color(40, 40, 60)
        self.cell(0, 8, f"   SKILLS", 0, 1, "L")
        self.set_draw_color(40, 40, 60)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(2)
        self.set_font("Arial", "", 10)
        self.set_text_color(0, 0, 0)
        skills_text = "\n".join([f"• {skill}" for skill in skills_list])
        self.multi_cell(0, 5, skills_text)
        self.ln(2)


def generate_pdf_resume(user_data, filename, template="1"):
    """
    Generate a professional resume PDF with chosen template
    
    Args:
        user_data (dict): All resume data
        filename (str): Output filename
        template (str): Template choice - "1", "2", or "3"
    """
    os.makedirs("outputs", exist_ok=True)
    pdf_path = os.path.join("outputs", filename)
    
    # Select template
    if template == "2":
        pdf = ResumeTemplate2()
    elif template == "3":
        pdf = ResumeTemplate3()
    else:
        pdf = ResumeTemplate1()  # Default
    
    pdf.add_page()
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    
    # Personal Information
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(0, 0, 0)
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
    
    pdf.ln(6)
    
    # Sections
    pdf.add_section("EDUCATION", user_data["education"])
    pdf.add_skills(user_data["skills"])
    
    if user_data["experience"] and user_data["experience"] != "No experience listed":
        pdf.add_section("EXPERIENCE", user_data["experience"])
    
    if user_data["projects"] and user_data["projects"] != "No projects listed":
        pdf.add_section("PROJECTS", user_data["projects"])
    
    if user_data["certifications"] and user_data["certifications"] != "No certifications listed":
        pdf.add_section("CERTIFICATIONS", user_data["certifications"])
    
    # Footer
    pdf.set_y(-25)
    pdf.set_font("Arial", "I", 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 10, f"Generated on {datetime.now().strftime('%B %d, %Y')}", 0, 0, "C")
    
    pdf.output(pdf_path)
    return pdf_path
