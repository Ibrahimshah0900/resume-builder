from fpdf import FPDF
import os
from datetime import datetime

# Base class with common methods
class BaseResume(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
    
    def add_section(self, title, content):
        self.set_font("Arial", "B", 12)
        self.set_text_color(30, 30, 30)
        self.cell(0, 8, title, 0, 1, "L")
        self.set_draw_color(200, 200, 200)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(2)
        self.set_font("Arial", "", 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 5, content)
        self.ln(4)
    
    def add_skills(self, skills):
        self.set_font("Arial", "B", 12)
        self.set_text_color(30, 30, 30)
        self.cell(0, 8, "SKILLS", 0, 1, "L")
        self.set_draw_color(200, 200, 200)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(2)
        self.set_font("Arial", "", 10)
        self.set_text_color(50, 50, 50)
        skills_text = ", ".join(skills)
        self.multi_cell(0, 5, skills_text)
        self.ln(4)


# Template 1: Classic Blue (single-column)
class TemplateClassic(BaseResume):
    def header(self):
        self.set_fill_color(25, 50, 100)
        self.rect(0, 0, 210, 35, "F")
        self.set_y(8)
        self.set_font("Arial", "B", 18)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, self.name, 0, 1, "C")
        self.set_font("Arial", "", 10)
        self.set_text_color(200, 210, 230)
        self.cell(0, 6, self.contact, 0, 1, "C")
        self.ln(10)
    
    def add_sections(self, user_data):
        self.add_section("EDUCATION", user_data["education"])
        self.add_skills(user_data["skills"])
        if user_data["experience"] and user_data["experience"] != "No experience listed":
            self.add_section("EXPERIENCE", user_data["experience"])
        if user_data["projects"] and user_data["projects"] != "No projects listed":
            self.add_section("PROJECTS", user_data["projects"])
        if user_data["certifications"] and user_data["certifications"] != "No certifications listed":
            self.add_section("CERTIFICATIONS", user_data["certifications"])


# Template 2: Modern Green (single-column, green accents)
class TemplateModern(BaseResume):
    def header(self):
        self.set_fill_color(0, 150, 100)
        self.rect(0, 0, 8, 297, "F")
        self.set_y(20)
        self.set_x(15)
        self.set_font("Arial", "B", 22)
        self.set_text_color(0, 0, 0)
        self.cell(0, 12, self.name, 0, 1, "L")
        self.set_x(15)
        self.set_font("Arial", "", 10)
        self.set_text_color(80, 80, 80)
        self.cell(0, 6, self.contact, 0, 1, "L")
        self.set_draw_color(0, 150, 100)
        self.line(15, 50, 195, 50)
        self.ln(10)
    
    def add_section(self, title, content):
        self.set_font("Arial", "B", 11)
        self.set_text_color(0, 150, 100)
        self.cell(0, 8, title, 0, 1, "L")
        self.set_draw_color(200, 200, 200)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(2)
        self.set_font("Arial", "", 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 5, content)
        self.ln(4)
    
    def add_sections(self, user_data):
        self.add_section("EDUCATION", user_data["education"])
        self.add_skills(user_data["skills"])
        if user_data["experience"] and user_data["experience"] != "No experience listed":
            self.add_section("EXPERIENCE", user_data["experience"])
        if user_data["projects"] and user_data["projects"] != "No projects listed":
            self.add_section("PROJECTS", user_data["projects"])
        if user_data["certifications"] and user_data["certifications"] != "No certifications listed":
            self.add_section("CERTIFICATIONS", user_data["certifications"])


# Template 3: Minimal Dark (single-column, dark header)
class TemplateMinimal(BaseResume):
    def header(self):
        self.set_y(20)
        self.set_font("Arial", "B", 24)
        self.set_text_color(30, 30, 30)
        self.cell(0, 12, self.name, 0, 1, "C")
        self.set_font("Arial", "", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, self.contact, 0, 1, "C")
        self.set_draw_color(200, 200, 200)
        self.line(40, 50, 170, 50)
        self.ln(10)
    
    def add_section(self, title, content):
        self.set_font("Arial", "B", 11)
        self.set_text_color(40, 40, 60)
        self.cell(0, 8, title, 0, 1, "L")
        self.set_draw_color(200, 200, 200)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(2)
        self.set_font("Arial", "", 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 5, content)
        self.ln(4)
    
    def add_sections(self, user_data):
        self.add_section("EDUCATION", user_data["education"])
        self.add_skills(user_data["skills"])
        if user_data["experience"] and user_data["experience"] != "No experience listed":
            self.add_section("EXPERIENCE", user_data["experience"])
        if user_data["projects"] and user_data["projects"] != "No projects listed":
            self.add_section("PROJECTS", user_data["projects"])
        if user_data["certifications"] and user_data["certifications"] != "No certifications listed":
            self.add_section("CERTIFICATIONS", user_data["certifications"])


# Template 4: Elegant Gold (single-column, gold accents, Times font)
class TemplateGold(BaseResume):
    def header(self):
        self.set_draw_color(200, 170, 110)
        self.set_line_width(1.5)
        self.rect(10, 10, 190, 277)
        self.set_line_width(0.5)
        self.set_fill_color(200, 170, 110)
        self.rect(10, 10, 190, 12, "F")
        self.set_y(16)
        self.set_font("Times", "B", 14)
        self.set_text_color(255, 255, 255)
        self.cell(0, 6, self.name, 0, 1, "C")
        self.set_font("Times", "", 9)
        self.set_text_color(255, 255, 255)
        self.cell(0, 5, self.contact, 0, 1, "C")
        self.set_y(35)
    
    def add_section(self, title, content):
        self.set_font("Times", "B", 11)
        self.set_text_color(200, 170, 110)
        self.cell(0, 8, title, 0, 1, "L")
        self.set_draw_color(200, 200, 200)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(2)
        self.set_font("Times", "", 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 5, content)
        self.ln(4)
    
    def add_skills(self, skills):
        self.set_font("Times", "B", 11)
        self.set_text_color(200, 170, 110)
        self.cell(0, 8, "SKILLS", 0, 1, "L")
        self.set_draw_color(200, 200, 200)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(2)
        self.set_font("Times", "", 10)
        self.set_text_color(50, 50, 50)
        skills_text = ", ".join(skills)
        self.multi_cell(0, 5, skills_text)
        self.ln(4)
    
    def add_sections(self, user_data):
        self.add_section("EDUCATION", user_data["education"])
        self.add_skills(user_data["skills"])
        if user_data["experience"] and user_data["experience"] != "No experience listed":
            self.add_section("EXPERIENCE", user_data["experience"])
        if user_data["projects"] and user_data["projects"] != "No projects listed":
            self.add_section("PROJECTS", user_data["projects"])
        if user_data["certifications"] and user_data["certifications"] != "No certifications listed":
            self.add_section("CERTIFICATIONS", user_data["certifications"])


# Template 5: Professional Grid (single-column, boxed sections)
class TemplateGrid(BaseResume):
    def header(self):
        self.set_fill_color(240, 240, 240)
        self.rect(0, 0, 210, 30, "F")
        self.set_y(8)
        self.set_font("Arial", "B", 16)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, self.name, 0, 1, "C")
        self.set_font("Arial", "", 9)
        self.set_text_color(80, 80, 80)
        self.cell(0, 6, self.contact, 0, 1, "C")
        self.set_draw_color(200, 200, 200)
        self.line(15, 30, 195, 30)
        self.ln(8)
    
    def add_section(self, title, content):
        self.set_fill_color(245, 245, 245)
        self.set_draw_color(200, 200, 200)
        self.rect(15, self.get_y(), 180, 10 + len(content.split("\n"))*5, "DF")
        self.set_y(self.get_y()+3)
        self.set_x(20)
        self.set_font("Arial", "B", 10)
        self.set_text_color(0, 0, 0)
        self.cell(0, 6, title, 0, 1, "L")
        self.set_font("Arial", "", 9)
        self.set_text_color(60, 60, 60)
        self.set_x(20)
        self.multi_cell(170, 5, content)
        self.set_y(self.get_y()+5)
    
    def add_skills(self, skills):
        self.set_fill_color(245, 245, 245)
        self.set_draw_color(200, 200, 200)
        content = ", ".join(skills)
        self.rect(15, self.get_y(), 180, 10 + len(content.split("\n"))*5, "DF")
        self.set_y(self.get_y()+3)
        self.set_x(20)
        self.set_font("Arial", "B", 10)
        self.set_text_color(0, 0, 0)
        self.cell(0, 6, "SKILLS", 0, 1, "L")
        self.set_font("Arial", "", 9)
        self.set_text_color(60, 60, 60)
        self.set_x(20)
        self.multi_cell(170, 5, content)
        self.set_y(self.get_y()+5)
    
    def add_sections(self, user_data):
        self.add_section("EDUCATION", user_data["education"])
        self.add_skills(user_data["skills"])
        if user_data["experience"] and user_data["experience"] != "No experience listed":
            self.add_section("EXPERIENCE", user_data["experience"])
        if user_data["projects"] and user_data["projects"] != "No projects listed":
            self.add_section("PROJECTS", user_data["projects"])
        if user_data["certifications"] and user_data["certifications"] != "No certifications listed":
            self.add_section("CERTIFICATIONS", user_data["certifications"])


# ============================================
# MAIN GENERATION FUNCTION
# ============================================
def generate_pdf_resume(user_data, filename, template="1"):
    os.makedirs("outputs", exist_ok=True)
    pdf_path = os.path.join("outputs", filename)
    
    # Select template
    if template == "2":
        pdf = TemplateModern()
    elif template == "3":
        pdf = TemplateMinimal()
    elif template == "4":
        pdf = TemplateGold()
    elif template == "5":
        pdf = TemplateGrid()
    else:
        pdf = TemplateClassic()
    
    # Store name and contact
    pdf.name = user_data["full_name"].upper()
    contact = f"{user_data['email']} | {user_data['phone']}"
    if user_data.get('location'):
        contact += f" | {user_data['location']}"
    pdf.contact = contact
    
    pdf.add_page()
    pdf.add_sections(user_data)
    
    # Footer
    pdf.set_y(-20)
    pdf.set_font("Arial", "I", 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 10, f"Generated on {datetime.now().strftime('%B %d, %Y')}", 0, 0, "C")
    
    pdf.output(pdf_path)
    return pdf_path
