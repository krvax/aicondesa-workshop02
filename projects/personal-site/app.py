from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

# Configuración del Perfil Personal
USER_PROFILE = {
    "name": "Miguel Angel Carvajal R",
    "title": "Cloud Architect & AI Engineer",
    "bio": "Apasionado por la intersección entre la Inteligencia Artificial y la arquitectura de nube. Liderando la innovación en AI Club Condesa.",
    "location": "Ciudad de México",
    "email": "miguel@coatl.tech",
    "social": {
        "linkedin": "https://linkedin.com/in/krvax",
        "github": "https://github.com/krvax",
        "twitter": "https://twitter.com/krvax"
    }
}

PROJECTS = [
    {
        "id": 1,
        "title": "Agente Cóatl Finanzas",
        "category": "AI & Agents",
        "description": "Agente de razonamiento avanzado desplegado en Vertex AI para análisis de mercados financieros.",
        "link": "https://github.com/krvax/AI-Club-Condesa-Workshops/tree/main/workshops/w6/lab01-gemini-agents"
    },
    {
        "id": 2,
        "title": "Conference Site Generator",
        "category": "Cloud & Web",
        "description": "Motor de sitios para conferencias técnicas optimizado para Google Cloud Run.",
        "link": "https://github.com/krvax/AI-Club-Condesa-Workshops/tree/main/workshops/w2/lab01-conference-site"
    },
    {
        "id": 3,
        "title": "Pomodoro AI Timer",
        "category": "Productivity",
        "description": "Herramienta de productividad minimalista desplegada con Nginx y Docker.",
        "link": "https://github.com/krvax/AI-Club-Condesa-Workshops/tree/main/workshops/w2/lab02-pomodoro-timer"
    }
]

SKILLS = {
    "AI": ["Gemini 1.5", "Vertex AI", "Reasoning Engines", "LangChain"],
    "Cloud": ["GCP", "Cloud Run", "Docker", "Terraform"],
    "Dev": ["Python", "Flask", "JavaScript", "HTML/CSS"]
}

@app.route('/')
def home():
    return render_template('index.html', profile=USER_PROFILE, projects=PROJECTS, skills=SKILLS, datetime=datetime)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
