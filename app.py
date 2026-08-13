import streamlit as st
import os
from resume_generator import generate_pdf_resume
from resume_scorer import score_resume, get_keyword_suggestions
from utils import validate_email, validate_phone, format_skills

st.set_page_config(page_title="AI Resume Builder", page_icon="📄", layout="wide")

st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">📄 AI Resume Builder</p>', unsafe_allow_html=True)
st.markdown("Choose a template and fill in your details to generate a professional resume!")

with st.form("resume_form"):
    st.header("🎨 Choose Resume Template")
    
    template_choice = st.radio(
        "Select Template Style:",
        [
            "1 - Classic Blue (Two-Column)",
            "2 - Modern Green (Accent Bar)",
            "3 - Minimal Dark (Clean)",
            "4 - Elegant Gold (Premium)",
            "5 - Professional Grid (Boxed)"
        ],
        index=0,
        horizontal=True
    )
    
    # Descriptions for each template
    if template_choice.startswith("1"):
        st.info("📘 **Classic Blue** – Two‑column layout with a professional sidebar.")
    elif template_choice.startswith("2"):
        st.info("💚 **Modern Green** – Clean design with a left accent color bar.")
    elif template_choice.startswith("3"):
        st.info("⬛ **Minimal Dark** – Bold minimalist typography with a dark header.")
    elif template_choice.startswith("4"):
        st.info("🌟 **Elegant Gold** – Premium gold accents and serif fonts for a luxury feel.")
    elif template_choice.startswith("5"):
        st.info("📦 **Professional Grid** – Boxed sections with a clean, structured layout.")
    
    st.markdown("---")
    
    st.header("📝 Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("Full Name *")
        email = st.text_input("Email *")
        phone = st.text_input("Phone *")
    with col2:
        linkedin = st.text_input("LinkedIn URL")
        github = st.text_input("GitHub URL")
        location = st.text_input("Location")
    
    st.header("🎓 Education *")
    education = st.text_area("Education Details", height=100)
    
    st.header("💼 Work Experience")
    experience = st.text_area("Experience Details", height=150)
    
    st.header("🛠️ Skills *")
    skills = st.text_input("Skills (comma separated)")
    
    st.header("📂 Projects")
    projects = st.text_area("Projects", height=100)
    
    st.header("📜 Certifications")
    certifications = st.text_area("Certifications", height=80)
    
    submitted = st.form_submit_button("✨ Generate Resume")

if submitted:
    if not full_name or not email or not phone or not education or not skills:
        st.error("⚠️ Please fill all required fields (*)")
    else:
        with st.spinner("Generating your resume..."):
            try:
                template_num = template_choice.split(" - ")[0]
                
                user_data = {
                    "full_name": full_name,
                    "email": email,
                    "phone": phone,
                    "location": location,
                    "linkedin": linkedin,
                    "github": github,
                    "education": education,
                    "experience": experience if experience else "No experience listed",
                    "skills": format_skills(skills),
                    "projects": projects if projects else "No projects listed",
                    "certifications": certifications if certifications else "No certifications listed"
                }
                
                pdf_filename = f"{full_name.replace(' ', '_')}_Resume.pdf"
                pdf_path = generate_pdf_resume(user_data, pdf_filename, template_num)
                score, feedback = score_resume(user_data)
                suggestions = get_keyword_suggestions(user_data["skills"])
                
                st.success("✅ Resume generated successfully!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("📊 Resume Score", f"{score}/100")
                with col2:
                    st.info(f"💡 {feedback}")
                
                if suggestions:
                    st.write("💡 **Suggested skills to add:**", ", ".join(suggestions))
                
                with open(pdf_path, "rb") as f:
                    st.download_button("📥 Download PDF", f, file_name=pdf_filename, mime="application/pdf")
                
                os.remove(pdf_path)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

st.sidebar.markdown("""
    ### 💡 Tips
    - Choose a template that fits your style
    - Use action words (Developed, Created, Led)
    - Quantify achievements with numbers
    - List 5-10 relevant skills
""")
