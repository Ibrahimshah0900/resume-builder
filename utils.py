import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    return bool(re.search(r'\d', phone))

def format_skills(skills_string):
    if not skills_string:
        return []
    return [skill.strip() for skill in skills_string.split(',') if skill.strip()]