import re

def score_resume(user_data):
    score = 0
    feedback = []
    
    # Personal info score
    if user_data.get("full_name") and len(user_data["full_name"]) > 2:
        score += 20
    if user_data.get("email") and "@" in user_data["email"]:
        score += 10
    if user_data.get("phone") and re.search(r'\d', user_data["phone"]):
        score += 10
    
    # Education score
    if user_data.get("education") and len(user_data["education"]) > 20:
        score += 15
        if re.search(r'(university|college|institute)', user_data["education"], re.I):
            score += 5
    
    # Skills score
    skills = user_data.get("skills", [])
    if skills:
        score += min(len(skills) * 5, 20)
    
    # Experience score
    if user_data.get("experience") and user_data["experience"] != "No experience listed":
        score += 10
        if any(word in user_data["experience"].lower() for word in ['developed', 'created', 'implemented']):
            score += 5
    
    # Projects score
    if user_data.get("projects") and user_data["projects"] != "No projects listed":
        score += 5
    
    final_score = min(score, 100)
    
    if final_score >= 80:
        feedback = "🌟 Excellent resume! You're ready to apply!"
    elif final_score >= 60:
        feedback = "👍 Good resume! Consider adding more details to weak sections"
    elif final_score >= 40:
        feedback = "📝 Decent start! Fill in missing sections"
    else:
        feedback = "📋 Please fill in all required sections"
    
    return final_score, feedback

def get_keyword_suggestions(skills):
    suggestions = []
    tech_skills = ['Python', 'SQL', 'Git', 'Machine Learning', 'Data Analysis']
    
    if not skills:
        return tech_skills
    
    for skill in tech_skills:
        if skill.lower() not in [s.lower() for s in skills]:
            suggestions.append(skill)
    
    return suggestions[:5]