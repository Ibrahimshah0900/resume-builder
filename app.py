import streamlit as st
import os
from resume_generator import generate_pdf_resume
from resume_scorer import score_resume, get_keyword_suggestions
from utils import validate_email, validate_phone, format_skills

st.set_page_config(page_title="AI Resume Builder", page_icon="📄", layout="wide")

st.title("📄 AI Resume Builder")
st.markdown("Create a professional resume in minutes!")

with st.form("resume_form"):
    st.header("Personal Information")
    col1, col2 = st.columns(2)
    
    with col1:
        full_name = st.text_input("Full Name *")
        email = st.text_input("Email *")
        phone = st.text_input("Phone *")
    
    with col2:
        linkedin = st.text_input("LinkedIn URL")
        github = st.text_input("GitHub URL")
        location = st.text_input("Location")
    
    st.header("Education *")
    education = st.text_area("Education Details", height=100)
    
    st.header("Work Experience")
    experience = st.text_area("Experience Details", height=150)
    
    st.header("Skills *")
    skills = st.text_input("Skills (comma separated)")
    
    st.header("Projects")
    projects = st.text_area("Projects", height=100)
    
    st.header("Certifications")
    certifications = st.text_area("Certifications", height=80)
    
    submitted = st.form_submit_button("✨ Generate Resume")

if submitted:
    if not full_name or not email or not phone or not education or not skills:
        st.error("⚠️ Please fill all required fields (*)")
    else:
        with st.spinner("Generating your resume..."):
            try:
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
                pdf_path = generate_pdf_resume(user_data, pdf_filename)
                score, feedback = score_resume(user_data)
                suggestions = get_keyword_suggestions(user_data["skills"])
                
                st.success("✅ Resume generated!")
                st.metric("Resume Score", f"{score}/100")
                st.info(f"💡 {feedback}")
                
                if suggestions:
                    st.write("Suggested skills to add:", ", ".join(suggestions))
                
                with open(pdf_path, "rb") as f:
                    st.download_button("📥 Download PDF", f, file_name=pdf_filename, mime="application/pdf")
                
                os.remove(pdf_path)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")