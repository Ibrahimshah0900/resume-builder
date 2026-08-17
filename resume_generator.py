from fpdf import FPDF
import os
from datetime import datetime
from PIL import Image

# ============================================
# BASE CLASS with PHOTO SUPPORT
# ============================================
class BaseResume(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.photo_path = None
        self.photo_size = 30
    
    def set_photo(self, photo_path, size=30):
        self.photo_path = photo_path
        self.photo_size = size
    
    def add_photo_top_right(self):
        """Add photo at top right corner - clean placement"""
        if self.photo_path and os.path.exists(self.photo_path):
            try:
                img = Image.open(self.photo_path)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                temp_path = 'outputs/temp_photo.jpg'
                img.save(temp_path, 'JPEG', quality=85)
                self.image(temp_path, 165, 8, 32, 32)
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                return True
            except:
                return False
        return False
    
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


# ============================================
# TEMPLATE 1: CLASSIC BLUE - FIXED
# ============================================
class TemplateClassic(BaseResume):
    def header(self):
        # Dark blue header bar - increased height to 65
        self.set_fill_color(25, 50, 100)
        self.rect(0, 0, 210, 65, "F")
        self.set_y(12)
        self.add_photo_top_right()
        self.set_x(15)
        self.set_font("Arial", "B", 18)
        self.set_text_color(255, 255, 255)
        self.cell(0, 12, self.name, 0, 1, "L")
        self.set_x(15)
        self.set_font("Arial", "", 10)
        self.set_text_color(200, 210, 230)
        self.cell(0, 6, self.contact, 0, 1, "L")
        # Set Y position to 70 - well below the header
        self.set_y(70)
    
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
# TEMPLATE 2: MODERN GREEN - FIXED
# ============================================
class TemplateModern(BaseResume):
    def header(self):
        self.set_fill_color(0, 150, 100)
        self.rect(0, 0, 8, 297, "F")
        self.set_y(15)
        self.add_photo_top_right()
        self.set_x(20)
        self.set_font("Arial", "B", 22)
        self.set_text_color(0, 0, 0)
        self.cell(0, 12, self.name, 0, 1, "L")
        self.set_x(20)
        self.set_font("Arial", "", 10)
        self.set_text_color(80, 80, 80)
        self.cell(0, 6, self.contact, 0, 1, "L")
        self.set_draw_color(0, 150, 100)
        self.line(15, 55, 195, 55)
        # Set Y position to 65 - well below header
        self.set_y(65)
    
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


# ============================================
# TEMPLATE 3: MINIMAL DARK - FIXED
# ============================================
class TemplateMinimal(BaseResume):
    def header(self):
        self.set_y(15)
        self.add_photo_top_right()
        self.set_x(15)
        self.set_font("Arial", "B", 24)
        self.set_text_color(30, 30, 30)
        self.cell(0, 12, self.name, 0, 1, "L")
        self.set_x(15)
        self.set_font("Arial", "", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, self.contact, 0, 1, "L")
        self.set_draw_color(200, 200, 200)
        self.line(15, 55, 195, 55)
        # Set Y position to 65 - well below header
        self.set_y(65)
    
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


# ============================================
# TEMPLATE 4: ELEGANT GOLD - FIXED
# ============================================
class TemplateGold(BaseResume):
    def header(self):
        self.set_draw_color(200, 170, 110)
        self.set_line_width(1.5)
        self.rect(10, 10, 190, 277)
        self.set_line_width(0.5)
        self.set_fill_color(200, 170, 110)
        self.rect(10, 10, 190, 16, "F")
        self.set_y(14)
        self.add_photo_top_right()
        self.set_x(18)
        self.set_font("Times", "B", 14)
        self.set_text_color(255, 255, 255)
        self.cell(0, 8, self.name, 0, 1, "L")
        self.set_x(18)
        self.set_font("Times", "", 9)
        self.set_text_color(255, 255, 255)
        self.cell(0, 5, self.contact, 0, 1, "L")
        # Set Y position to 45 - well below the gold header
        self.set_y(45)
    
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
# TEMPLATE 5: PROFESSIONAL GRID - FIXED
# ============================================
class TemplateGrid(BaseResume):
    def header(self):
        self.set_fill_color(240, 240, 240)
        self.rect(0, 0, 210, 50, "F")
        self.set_y(10)
        self.add_photo_top_right()
        self.set_x(15)
        self.set_font("Arial", "B", 16)
        self.set_text_color(0, 0, 0)
        self.cell(0, 12, self.name, 0, 1, "L")
        self.set_x(15)
        self.set_font("Arial", "", 9)
        self.set_text_color(80, 80, 80)
        self.cell(0, 6, self.contact, 0, 1, "L")
        self.set_draw_color(200, 200, 200)
        self.line(15, 52, 195, 52)
        # Set Y position to 58 - well below header
        self.set_y(58)
    
    def add_section(self, title, content):
        self.set_fill_color(245, 245, 245)
        self.set_draw_color(200, 200, 200)
        line_count = len(content.split("\n")) + 2
        height = 10 + line_count * 5
        self.rect(15, self.get_y(), 180, height, "DF")
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
        content = ", ".join(skills)
        self.set_fill_color(245, 245, 245)
        self.set_draw_color(200, 200, 200)
        line_count = len(content.split("\n")) + 2
        height = 10 + line_count * 5
        self.rect(15, self.get_y(), 180, height, "DF")
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
def generate_pdf_resume(user_data, filename, template="1", photo_path=None):
    os.makedirs("outputs", exist_ok=True)
    pdf_path = os.path.join("outputs", filename)
    
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
    
    if photo_path and os.path.exists(photo_path):
        pdf.set_photo(photo_path, size=32)
    
    pdf.name = user_data["full_name"].upper()
    contact = f"{user_data['email']} | {user_data['phone']}"
    if user_data.get('location'):
        contact += f" | {user_data['location']}"
    pdf.contact = contact
    
    pdf.add_page()
    pdf.add_sections(user_data)
    
    pdf.set_y(-20)
    pdf.set_font("Arial", "I", 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 10, f"Generated on {datetime.now().strftime('%B %d, %Y')}", 0, 0, "C")
    
    pdf.output(pdf_path)
    return pdf_path
