import json

from app.database.database import Base, engine, SessionLocal
from app.models.admin import Admin
from app.models.content import PortfolioContent
from app.core.security import hash_password
from app.config.settings import settings

DEFAULT_CONTENT = {
    "name": "Reyan De La Cruz",
    "title": "Senior Software Developer",
    "tagline": (
        "Full-stack developer with 7+ years of experience building enterprise "
        "applications, RPA solutions, and modern web platforms using Python, "
        "JavaScript, and cloud technologies."
    ),
    "location": "Rosario, Pasig City, Philippines",
    "photo": "/images/reyan-profile.jpg",
    "socials": [
        {"label": "GitHub", "url": "https://github.com/reyandelacruz09"},
        {"label": "LinkedIn", "url": "https://www.linkedin.com/in/reyan-dela-cruz-26a447163/"},
        {"label": "Email", "url": "mailto:reyandelacruz09@gmail.com"},
    ],
    "contact": {
        "email": "reyandelacruz09@gmail.com",
        "phone": "09763092862",
    },
    "about": [
        (
            "I'm a senior software developer with 7+ years of experience "
            "engineering enterprise-grade applications across fintech, HR, "
            "procurement, and automotive industries. I specialize in building "
            "full-stack web applications, automating business processes with "
            "RPA, and delivering scalable solutions using Python, JavaScript, "
            "and modern cloud platforms."
        ),
        (
            "From building applicant tracking systems for Uniqlo to developing "
            "RPA tools that automate financial reconciliation for SB Finance, "
            "I thrive on solving complex problems with clean, maintainable "
            "code. I'm passionate about leveraging modern tools like React, "
            "Django, FastAPI, Docker, and AWS to deliver real business value."
        ),
    ],
    "skills": [
        {"category": "Frontend", "items": ["React", "React Native", "JavaScript", "TypeScript", "Redux", "HTML", "CSS", "Bootstrap", "Tailwind CSS"]},
        {"category": "Backend", "items": ["Python", "Django", "Django REST", "FastAPI", "Flask", "PHP", "Java", "SQL", "PostgreSQL"]},
        {"category": "Data & Analytics", "items": ["NumPy", "Pandas", "Matplotlib", "Data Modeling", "Database Design"]},
        {"category": "DevOps & Tools", "items": ["Docker", "AWS", "Digital Ocean", "Git", "Linux", "Nginx", "CI/CD"]},
        {"category": "Other", "items": ["Zoho Creator", "Adobe Photoshop CS6", "Microsoft Office", "Agile Frameworks", "Manual & Automated Testing"]},
    ],
    "projects": [
        {
            "title": "RPA Financial Reconciliation Tool",
            "description": "Built an RPA solution from scratch for SB Finance that automates financial reconciliation by extracting, validating, and matching transaction data across banking systems and internal records.",
            "tech": ["Python", "Pandas", "NumPy", "Flask", "PostgreSQL", "Docker", "AWS Lambda", "Boto3"],
            "github": "",
            "live": "",
        },
        {
            "title": "Applicant Tracker System (Uniqlo)",
            "description": "Led development of a comprehensive applicant tracking system for Uniqlo, streamlining the recruitment workflow from application to onboarding.",
            "tech": ["Python", "Django", "Django REST", "React", "JavaScript", "SQL"],
            "github": "",
            "live": "",
        },
        {
            "title": "Employee Portal (OODC)",
            "description": "Led development of a full employee management web application with dashboards, attendance tracking, assessments, and reporting features.",
            "tech": ["React", "Redux", "Django", "Django REST", "PostgreSQL", "Tailwind CSS"],
            "github": "",
            "live": "",
        },
        {
            "title": "Monde Procurement System",
            "description": "Led the development of an integrated procurement system managing vendor workflows, purchase orders, and inventory tracking.",
            "tech": ["Python", "Django", "React", "JavaScript", "SQL", "Bootstrap"],
            "github": "",
            "live": "",
        },
        {
            "title": "Burger Machine Integrated System",
            "description": "Led development of an integrated business system covering operations, inventory, and reporting for Burger Machine.",
            "tech": ["Python", "Django", "React", "JavaScript", "SQL"],
            "github": "",
            "live": "",
        },
        {
            "title": "SRS V2 (Service Request System)",
            "description": "Developed a web-based service request management system used across multiple departments to submit and track requests for the Support Team.",
            "tech": ["FastAPI", "React", "TanStack Query", "PostgreSQL"],
            "github": "",
            "live": "",
        },
        {
            "title": "Wiring Comparison Tools (Yazaki)",
            "description": "Developed RJ90 Wiring Comparison Tool & BOM Wiring Comparison Tool for the Yazaki Wiring Department to automate and streamline wiring data validation.",
            "tech": ["FastAPI", "React", "TanStack Query"],
            "github": "",
            "live": "",
        },
    ],
    "experience": [
        {
            "role": "Sr. Technical Support Analyst",
            "company": "Yazaki",
            "period": "Apr 2026 – Aug 2026",
            "description": "Developed internal tools for the Wiring Department including RJ90 Wiring Comparison Tool and BOM Wiring Comparison Tool using FastAPI and React. Built SRS V2, a web-based service request management system used across multiple departments.",
        },
        {
            "role": "Software Developer",
            "company": "Vertere Global Solution, Inc.",
            "period": "Apr 2025 – Feb 2026",
            "description": "Built an RPA solution from scratch for SB Finance that automates financial reconciliation. Engineered and maintained RPA solution using Python, Pandas, NumPy, Flask, PostgreSQL, Docker, and AWS services (Lambda, Boto3).",
        },
        {
            "role": "Sr. Software Developer",
            "company": "One Out Source",
            "period": "Mar 2023 – Mar 2025",
            "description": "Lead developer for multiple projects including Applicant Tracker System (Uniqlo), Employee Portal (OODC), Monde Procurement System, and Burger Machine Integrated System. Engineered modern applications with Python, Django, React, TypeScript, and deployed on Digital Ocean and AWS.",
        },
        {
            "role": "Software Engineer I",
            "company": "Think DWM",
            "period": "May 2019 – Mar 2023",
            "description": "Implemented Psymetrics (requirements gathering, analysis, implementation, and testing). Engineered applications with Python, JavaScript, SQL, and React. Handled data modeling, database design, QA testing, and automated tests with Python.",
        },
        {
            "role": "Associate Software Engineer",
            "company": "Gotech Solutions, Inc.",
            "period": "Jul 2018 – Jan 2019",
            "description": "Provided day-to-day support and bug fixing using Java and JavaScript. Engineered modern applications with Java, JavaScript, and SQL.",
        },
    ],
}


def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(Admin).count() == 0:
            db.add(
                Admin(
                    username=settings.DEFAULT_ADMIN_USERNAME,
                    password_hash=hash_password(settings.DEFAULT_ADMIN_PASSWORD),
                )
            )
            db.commit()

        if db.query(PortfolioContent).count() == 0:
            for key, value in DEFAULT_CONTENT.items():
                db.add(PortfolioContent(key=key, value=json.dumps(value)))
            db.commit()
        else:
            for key, value in DEFAULT_CONTENT.items():
                row = (
                    db.query(PortfolioContent)
                    .filter(PortfolioContent.key == key)
                    .first()
                )
                if row:
                    row.value = json.dumps(value)
                else:
                    db.add(PortfolioContent(key=key, value=json.dumps(value)))
            db.commit()
    finally:
        db.close()