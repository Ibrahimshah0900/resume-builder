from fpdf import FPDF
import os
from datetime import datetime

# ============================================
# TEMPLATE 1: CLASSIC - Two Column Layout
# ============================================
class TemplateClassic(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
    
    def header(self):
        self.set_fill_color(25, 50, 100)
        self.rect(0, 0, 210, 35, "F")
        self.set_y(8)
        self.set_font("Arial", "B", 18)
        self.set_text_color(255,255,255)
        self.cell(0,10, self.name, 0,1,"C")
        self.set_font("Arial", "", 10)
        self.set_text_color(200,210,230)
        self.cell(0,6, self.contact, 0,1,"C")
        self.ln(5)
    
    def add_sidebar(self, skills, education):
        self.set_y(45)
        self.set_x(10)
        self.set_font("Arial","B",11)
        self.set_text_color(25,50,100)
        self.cell(55,8,"SKILLS",0,1,"L")
        self.set_font("Arial","",9)
        self.set_text_color(50,50,50)
        for s in skills:
            self.cell(55,5,f"  - {s}",0,1,"L")
        self.ln(3)
        self.set_font("Arial","B",11)
        self.set_text_color(25,50,100)
        self.cell(55,8,"EDUCATION",0,1,"L")
        self.set_font("Arial","",9)
        self.set_text_color(50,50,50)
        self.multi_cell(55,5, education)
    
    def add_main_content(self, exp, proj, cert):
        self.set_y(45)
        self.set_x(75)
        self.set_font("Arial","B",11)
        self.set_text_color(25,50,100)
        self.cell(120,8,"EXPERIENCE",0,1,"L")
        self.set_font("Arial","",9)
        self.set_text_color(50,50,50)
        self.multi_cell(120,5, exp)
        self.ln(3)
        self.set_font("Arial","B",11)
        self.set_text_color(25,50,100)
        self.cell(120,8,"PROJECTS",0,1,"L")
        self.set_font("Arial","",9)
        self.set_text_color(50,50,50)
        self.multi_cell(120,5, proj)
        self.ln(3)
        if cert and cert!="No certifications listed":
            self.set_font("Arial","B",11)
            self.set_text_color(25,50,100)
            self.cell(120,8,"CERTIFICATIONS",0,1,"L")
            self.set_font("Arial","",9)
            self.set_text_color(50,50,50)
            self.multi_cell(120,5, cert)

# ============================================
# TEMPLATE 2: MODERN - Accent Color Bar
# ============================================
class TemplateModern(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
    
    def header(self):
        self.set_fill_color(0,150,100)
        self.rect(0,0,8,297,"F")
        self.set_y(20)
        self.set_x(15)
        self.set_font("Arial","B",22)
        self.set_text_color(0,0,0)
        self.cell(0,12,self.name,0,1,"L")
        self.set_x(15)
        self.set_font("Arial","",10)
        self.set_text_color(80,80,80)
        self.cell(0,6,self.contact,0,1,"L")
        self.set_draw_color(0,150,100)
        self.line(15,50,195,50)
        self.ln(5)
    
    def add_sidebar(self, skills, education):
        self.set_y(58)
        self.set_x(15)
        self.set_font("Arial","B",11)
        self.set_text_color(0,150,100)
        self.cell(0,8,"SKILLS",0,1,"L")
        self.set_font("Arial","",9)
        self.set_text_color(50,50,50)
        self.multi_cell(0,5, "  |  ".join(skills))
        self.ln(5)
        self.set_font("Arial","B",11)
        self.set_text_color(0,150,100)
        self.cell(0,8,"EDUCATION",0,1,"L")
        self.set_font("Arial","",9)
        self.set_text_color(50,50,50)
        self.multi_cell(0,5, education)
    
    def add_main_content(self, exp, proj, cert):
        self.ln(5)
        self.set_font("Arial","B",11)
        self.set_text_color(0,150,100)
        self.cell(0,8,"EXPERIENCE",0,1,"L")
        self.set_font("Arial","",9)
        self.set_text_color(50,50,50)
        self.multi_cell(0,5, exp)
        self.ln(3)
        self.set_font("Arial","B",11)
        self.set_text_color(0,150,100)
        self.cell(0,8,"PROJECTS",0,1,"L")
        self.set_font("Arial","",9)
        self.set_text_color(50,50,50)
        self.multi_cell(0,5, proj)
        self.ln(3)
        if cert and cert!="No certifications listed":
            self.set_font("Arial","B",11)
            self.set_text_color(0,150,100)
            self.cell(0,8,"CERTIFICATIONS",0,1,"L")
            self.set_font("Arial","",9)
            self.set_text_color(50,50,50)
            self.multi_cell(0,5, cert)

# ============================================
# TEMPLATE 3: MINIMAL - Clean Typography
# ============================================
class TemplateMinimal(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)
    
    def header(self):
        self.set_y(20)
        self.set_font("Arial","B",24)
        self.set_text_color(30,30,30)
        self.cell(0,12,self.name,0,1,"C")
        self.set_font("Arial","",10)
        self.set_text_color(100,100,100)
        self.cell(0,6,self.contact,0,1,"C")
        self.set_draw_color(200,200,200)
        self.line(40,50,170,50)
        self.ln(8)
    
    def add_sidebar(self, skills, education):
        self.set_font("Arial","B",10)
        self.set_text_color(30,30,30)
        self.cell(0,6,"SKILLS",0,1,"L")
        self.set_font("Arial","",9)
        self.set_text_color(60,60,60)
        self.multi_cell(0,5, ", ".join(skills))
        self.ln(5)
        self.set_font("Arial","B",10)
        self.set_text_color(30,30,30)
        self.cell(0,6,"EDUCATION",0,1,"L")
        self.set_font("Arial","",9)
        self.set_text_color(60,60,60)
        self.multi_cell(0,5, education)
    
    def add_main_content(self, exp, proj, cert):
        self.ln(5)
        self.set_font("Arial","B",10)
        self.set_text_color(30,30,30)
        self.cell(0,6,"EXPERIENCE",0,1,"L")
        self.set_font("Arial","",9)
        self.set_text_color(60,60,60)
        self.multi_cell(0,5, exp)
        self.ln(3)
        self.set_font("Arial","B",10)
        self.set_text_color(30,30,30)
        self.cell(0,6,"PROJECTS",0,1,"L")
        self.set_font("Arial","",9)
        self.set_text_color(60,60,60)
        self.multi_cell(0,5, proj)
        self.ln(3)
        if cert and cert!="No certifications listed":
            self.set_font("Arial","B",10)
            self.set_text_color(30,30,30)
            self.cell(0,6,"CERTIFICATIONS",0,1,"L")
            self.set_font("Arial","",9)
            self.set_text_color(60,60,60)
            self.multi_cell(0,5, cert)

# ============================================
# TEMPLATE 4: ELEGANT GOLD - Premium Style
# ============================================
class TemplateGold(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
    
    def header(self):
        # Gold decorative border
        self.set_draw_color(200,170,110)
        self.set_line_width(1.5)
        self.rect(10,10,190,277)
        self.set_line_width(0.5)
        self.set_fill_color(200,170,110)
        self.rect(10,10,190,12,"F")
        self.set_y(16)
        self.set_font("Times","B",14)
        self.set_text_color(255,255,255)
        self.cell(0,6,self.name,0,1,"C")
        self.set_font("Times","",9)
        self.set_text_color(255,255,255)
        self.cell(0,5,self.contact,0,1,"C")
        self.set_y(35)
    
    def add_sidebar(self, skills, education):
        self.set_x(15)
        self.set_font("Times","B",11)
        self.set_text_color(200,170,110)
        self.cell(0,8,"SKILLS",0,1,"L")
        self.set_font("Times","",9)
        self.set_text_color(50,50,50)
        for s in skills:
            self.cell(0,5,f"  • {s}",0,1,"L")
        self.ln(3)
        self.set_font("Times","B",11)
        self.set_text_color(200,170,110)
        self.cell(0,8,"EDUCATION",0,1,"L")
        self.set_font("Times","",9)
        self.set_text_color(50,50,50)
        self.multi_cell(0,5, education)
    
    def add_main_content(self, exp, proj, cert):
        self.ln(5)
        self.set_font("Times","B",11)
        self.set_text_color(200,170,110)
        self.cell(0,8,"EXPERIENCE",0,1,"L")
        self.set_font("Times","",9)
        self.set_text_color(50,50,50)
        self.multi_cell(0,5, exp)
        self.ln(3)
        self.set_font("Times","B",11)
        self.set_text_color(200,170,110)
        self.cell(0,8,"PROJECTS",0,1,"L")
        self.set_font("Times","",9)
        self.set_text_color(50,50,50)
        self.multi_cell(0,5, proj)
        self.ln(3)
        if cert and cert!="No certifications listed":
            self.set_font("Times","B",11)
            self.set_text_color(200,170,110)
            self.cell(0,8,"CERTIFICATIONS",0,1,"L")
            self.set_font("Times","",9)
            self.set_text_color(50,50,50)
            self.multi_cell(0,5, cert)

# ============================================
# TEMPLATE 5: PROFESSIONAL GRID - Boxed Sections
# ============================================
class TemplateGrid(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
    
    def header(self):
        self.set_fill_color(240,240,240)
        self.rect(0,0,210,30,"F")
        self.set_y(8)
        self.set_font("Arial","B",16)
        self.set_text_color(0,0,0)
        self.cell(0,10,self.name,0,1,"C")
        self.set_font("Arial","",9)
        self.set_text_color(80,80,80)
        self.cell(0,6,self.contact,0,1,"C")
        self.set_draw_color(200,200,200)
        self.line(15,30,195,30)
        self.ln(6)
    
    def add_sidebar(self, skills, education):
        # Skills box
        self.set_fill_color(245,245,245)
        self.set_draw_color(200,200,200)
        self.rect(15,self.get_y(),180,30+len(skills)*5,"DF")
        self.set_y(self.get_y()+3)
        self.set_x(20)
        self.set_font("Arial","B",10)
        self.set_text_color(0,0,0)
        self.cell(0,6,"SKILLS",0,1,"L")
        self.set_font("Arial","",9)
        self.set_text_color(60,60,60)
        self.set_x(20)
        self.multi_cell(170,5, ", ".join(skills))
        self.set_y(self.get_y()+5)
        # Education box
        self.set_fill_color(245,245,245)
        self.rect(15,self.get_y(),180,30+len(education.split("\n"))*5,"DF")
        self.set_y(self.get_y()+3)
        self.set_x(20)
        self.set_font("Arial","B",10)
        self.set_text_color(0,0,0)
        self.cell(0,6,"EDUCATION",0,1,"L")
        self.set_font("Arial","",9)
        self.set_text_color(60,60,60)
        self.set_x(20)
        self.multi_cell(170,5, education)
        self.set_y(self.get_y()+5)
    
    def add_main_content(self, exp, proj, cert):
        # Experience box
        self.set_fill_color(245,245,245)
        self.rect(15,self.get_y(),180,30+len(exp.split("\n"))*5,"DF")
        self.set_y(self.get_y()+3)
        self.set_x(20)
        self.set_font("Arial","B",10)
        self.set_text_color(0,0,0)
        self.cell(0,6,"EXPERIENCE",0,1,"L")
        self.set_font("Arial","",9)
        self.set_text_color(60,60,60)
        self.set_x(20)
        self.multi_cell(170,5, exp)
        self.set_y(self.get_y()+5)
        # Projects box
        self.set_fill_color(245,245,245)
        self.rect(15,self.get_y(),180,30+len(proj.split("\n"))*5,"DF")
        self.set_y(self.get_y()+3)
        self.set_x(20)
        self.set_font("Arial","B",10)
        self.set_text_color(0,0,0)
        self.cell(0,6,"PROJECTS",0,1,"L")
        self.set_font("Arial","",9)
        self.set_text_color(60,60,60)
        self.set_x(20)
        self.multi_cell(170,5, proj)
        self.set_y(self.get_y()+5)
        if cert and cert!="No certifications listed":
            self.set_fill_color(245,245,245)
            self.rect(15,self.get_y(),180,30+len(cert.split("\n"))*5,"DF")
            self.set_y(self.get_y()+3)
            self.set_x(20)
            self.set_font("Arial","B",10)
            self.set_text_color(0,0,0)
            self.cell(0,6,"CERTIFICATIONS",0,1,"L")
            self.set_font("Arial","",9)
            self.set_text_color(60,60,60)
            self.set_x(20)
            self.multi_cell(170,5, cert)
            self.set_y(self.get_y()+5)

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
    
    # Store name and contact for header
    pdf.name = user_data["full_name"].upper()
    contact = f"{user_data['email']} | {user_data['phone']}"
    if user_data.get('location'):
        contact += f" | {user_data['location']}"
    pdf.contact = contact
    
    pdf.add_page()
    
    # Add sidebar (skills + education) - works for all templates
    pdf.add_sidebar(
        user_data["skills"],
        user_data["education"]
    )
    
    # Add main content
    pdf.add_main_content(
        user_data["experience"] if user_data["experience"] != "No experience listed" else "",
        user_data["projects"] if user_data["projects"] != "No projects listed" else "",
        user_data["certifications"] if user_data["certifications"] != "No certifications listed" else ""
    )
    
    # Footer
    pdf.set_y(-20)
    pdf.set_font("Arial", "I", 8)
    pdf.set_text_color(150,150,150)
    pdf.cell(0,10, f"Generated on {datetime.now().strftime('%B %d, %Y')}", 0, 0, "C")
    
    pdf.output(pdf_path)
    return pdf_path
