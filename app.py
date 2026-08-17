import streamlit as st
import os
from resume_generator import generate_pdf_resume
from resume_scorer import score_resume, get_keyword_suggestions
from utils import validate_email, validate_phone, format_skills
from PIL import Image
import cv2
import numpy as np

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

def detect_face_and_crop(image_path, crop_percent=0):
    """Detect face with optional manual crop offset"""
    try:
        img = cv2.imread(image_path)
        if img is None:
            return None
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        if len(faces) == 0:
            return None
        
        (x, y, w, h) = max(faces, key=lambda f: f[2] * f[3])
        
        # Apply manual crop adjustment
        padding = max(w, h) // 2
        x1 = max(0, x - padding)
        y1 = max(0, y - padding - int(crop_percent * 0.5))
        x2 = min(img.shape[1], x + w + padding)
        y2 = min(img.shape[0], y + h + padding)
        
        cropped = img[y1:y2, x1:x2]
        cropped_pil = Image.fromarray(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))
        return cropped_pil
    except:
        return None

with st.form("resume_form"):
    st.header("🎨 Choose Resume Template")
    
    template_choice = st.radio(
        "Select Template Style:",
        [
            "1 - Classic Blue",
            "2 - Modern Green",
            "3 - Minimal Dark",
            "4 - Elegant Gold",
            "5 - Professional Grid"
        ],
        index=0,
        horizontal=True
    )
    
    if template_choice.startswith("1"):
        st.info("📘 **Classic Blue** – Professional two-column layout")
    elif template_choice.startswith("2"):
        st.info("💚 **Modern Green** – Clean design with accent bar")
    elif template_choice.startswith("3"):
        st.info("⬛ **Minimal Dark** – Bold minimalist design")
    elif template_choice.startswith("4"):
        st.info("🌟 **Elegant Gold** – Premium gold accents")
    elif template_choice.startswith("5"):
        st.info("📦 **Professional Grid** – Boxed sections layout")
    
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
    
    # ============================================
    # SIMPLE PHOTO UPLOAD WITH CROP SLIDER
    # ============================================
    st.header("📸 Profile Photo")
    st.markdown("Upload a photo. Use the slider to crop around your face.")
    
    uploaded_file = st.file_uploader(
        "Upload your photo (JPG/PNG)",
        type=["jpg", "jpeg", "png"]
    )
    
    photo_path = None
    crop_adjust = 0
    
    if uploaded_file is not None:
        os.makedirs("outputs", exist_ok=True)
        temp_path = os.path.join("outputs", "uploaded_photo.jpg")
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Preview original
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(temp_path, width=150, caption="Original")
        
        with col2:
            # Simple crop slider
            crop_adjust = st.slider(
                "Crop adjustment (move up/down to center face)",
                min_value=-50,
                max_value=50,
                value=0,
                step=5,
                help="Move slider to center your face in the frame"
            )
        
        # Auto crop with face detection
        with st.spinner("🔄 Processing photo..."):
            cropped_img = detect_face_and_crop(temp_path, crop_adjust)
            
            if cropped_img is not None:
                cropped_path = os.path.join("outputs", "cropped_photo.jpg")
                cropped_img.save(cropped_path, "JPEG", quality=90)
                photo_path = cropped_path
                st.image(cropped_path, width=150, caption="✅ Cropped (Face detected)")
                st.success("✅ Photo ready! Face detected and cropped.")
            else:
                # Fallback: center crop
                img = Image.open(temp_path)
                width, height = img.size
                min_side = min(width, height)
                left = (width - min_side) // 2
                top = (height - min_side) // 2 + crop_adjust
                top = max(0, top)
                bottom = top + min_side
                cropped = img.crop((left, top, left + min_side, bottom))
                cropped_path = os.path.join("outputs", "cropped_photo.jpg")
                cropped.save(cropped_path, "JPEG", quality=90)
                photo_path = cropped_path
                st.image(cropped_path, width=150, caption="⚠️ Center Cropped")
                st.warning("⚠️ No face detected. Cropped from center. Try a clearer photo or adjust slider.")
    
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
                pdf_path = generate_pdf_resume(user_data, pdf_filename, template_num, photo_path)
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
                
                # Clean up
                try:
                    if os.path.exists(pdf_path):
                        os.remove(pdf_path)
                    if photo_path and os.path.exists(photo_path):
                        os.remove(photo_path)
                    if os.path.exists(os.path.join("outputs", "uploaded_photo.jpg")):
                        os.remove(os.path.join("outputs", "uploaded_photo.jpg"))
                except:
                    pass
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

st.sidebar.markdown("""
    ### 💡 Tips
    - Choose a template that fits your style
    - Use action words (Developed, Created, Led)
    - Quantify achievements with numbers
    - List 5-10 relevant skills
    - Upload a photo and use slider to center your face
""")
