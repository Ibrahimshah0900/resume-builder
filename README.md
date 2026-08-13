# 📄 AI Resume Builder

An intelligent, free resume builder powered by Python and Machine Learning. Create professional resumes, get AI-powered scoring, and receive smart skill recommendations.

## 🌟 Features

- ✅ **Professional PDF Generation** - Create clean, ATS-friendly resumes instantly
- 🤖 **AI Resume Scoring** - Get a score from 0-100 based on resume quality
- 💡 **Smart Skill Suggestions** - Receive personalized skill recommendations
- 📊 **Resume Analysis** - Get actionable feedback to improve your resume
- 🎯 **Complete Resume Sections** - Education, Experience, Skills, Projects, Certifications
- 📱 **Mobile-Friendly** - Works on all devices

## 🚀 Demo

[Live Demo](https://your-app-name.streamlit.app) *(After deployment)*

## 📋 How It Works

1. **Fill in your details** - Name, education, experience, skills, projects
2. **Click Generate** - AI analyzes your resume and creates a PDF
3. **Get Feedback** - Receive a score and improvement suggestions
4. **Download PDF** - Get your professional resume instantly

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **PDF Generation**: FPDF
- **AI/ML**: Scikit-learn, Pandas
- **Deployment**: Streamlit Cloud

## 📁 Project Structure

```
resume-builder/
├── app.py                 # Main application
├── resume_generator.py    # PDF generation
├── resume_scorer.py       # AI scoring engine
├── utils.py              # Helper functions
└── requirements.txt      # Python dependencies
```

## 🏃‍♂️ Run Locally

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/resume-builder.git
cd resume-builder

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📦 Dependencies

```
streamlit
fpdf
pandas
scikit-learn
```

## 🤖 AI Scoring Logic

The resume scorer evaluates:
- **Completeness** - All sections filled
- **Skills** - Quantity and quality of skills
- **Experience** - Action words and quantifiable achievements
- **Education** - Details and relevance

## 🎯 Keywords Suggested

Based on your current skills, the AI suggests:
- Industry-relevant technical skills
- In-demand programming languages
- Tools and technologies
- Soft skills

## 🚀 Deployment

This app is designed for easy deployment on Streamlit Cloud:

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://share.streamlit.io)
3. Connect your GitHub repository
4. Click Deploy

## 📊 Sample Resume Score

| Score Range | Rating | Feedback |
|-------------|--------|----------|
| 80-100 | 🌟 Excellent | Ready for top positions |
| 60-79 | 👍 Good | Add more detail |
| 40-59 | 📝 Decent | Fill missing sections |
| 0-39 | 📋 Needs Work | Complete all sections |

## 💡 Tips for a High Score

- ✅ **Quantify achievements** (e.g., "Improved by 30%")
- ✅ **Use action words** (Developed, Created, Implemented)
- ✅ **Add 5-10 relevant skills**
- ✅ **Include project details with results**
- ✅ **Add certifications and awards**

## 🔧 Troubleshooting

**Port already in use:**
```bash
kill $(lsof -t -i:8501)  # macOS/Linux
netstat -ano | findstr :8501  # Windows
```

**Missing packages:**
```bash
pip install -r requirements.txt --upgrade
```

## 🤝 Contributing

Contributions welcome! Feel free to:
- ⭐ Star this repository
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests

## 📄 License

MIT License - Free for personal and commercial use.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io)
- PDF generation by [FPDF](https://pyfpdf.readthedocs.io)
- ML powered by [Scikit-learn](https://scikit-learn.org)

## 📧 Contact

Created by [Your Name] - Feel free to reach out!

---

**Made with ❤️ using Python & Streamlit**
