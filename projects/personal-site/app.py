from flask import Flask, render_template, jsonify, send_from_directory
import datetime
import os

app = Flask(__name__)

# ── Perfil Profesional ──────────────────────────────────────────────
USER_PROFILE = {
    "name": "Miguel Angel Carvajal R",
    "title": "Senior Cloud & AI Platform Engineer",
    "bio": "10+ años diseñando y operando infraestructura cloud-native a escala. "
           "Especializado en plataformas AI/LLM en producción (AWS Bedrock, EKS), "
           "SRE, CI/CD y automatización de infraestructura.",
    "location": "Ciudad de México",
    "email": "miguel@coatl.tech",
    "social": {
        "linkedin": "https://www.linkedin.com/in/miguel-carvajal",
        "github": "https://github.com/krvax",
        "twitter": "https://twitter.com/krvax",
    }
}

# ── Proyectos Destacados ────────────────────────────────────────────
PROJECTS = [
    {
        "id": 1,
        "title": "AI Platform on EKS",
        "category": "AI & Cloud",
        "description": "Plataforma generativa en producción sobre EKS integrando AWS Bedrock "
                       "(Claude, Titan), MCP Gateway como Helm chart, y Redis/PostgreSQL "
                       "para persistencia — sirviendo 500+ usuarios internos.",
        "link": "https://github.com/krvax/epam-aws-devops-prep",
        "icon": "🤖"
    },
    {
        "id": 2,
        "title": "Agente Cóatl Finanzas",
        "category": "AI Agents",
        "description": "Agente de razonamiento avanzado desplegado en Vertex AI para "
                       "análisis de mercados financieros con Gemini Enterprise.",
        "link": "https://vertexaisearch.cloud.google.com/home/cid/947f744a-0690-499b-82a5-22d91d67b103/r/agent/8544371628222189320",
        "icon": "🐍"
    },
    {
        "id": 3,
        "title": "Cloud Native Labs",
        "category": "DevOps & SRE",
        "description": "12 laboratorios hands-on cubriendo VPC, IAM, EKS, Terraform, "
                       "GitLab CI/CD con OIDC, ArgoCD, Prometheus/Grafana y Chaos Engineering.",
        "link": "https://github.com/krvax/epam-aws-devops-prep",
        "icon": "☁️"
    },
    {
        "id": 4,
        "title": "Conference Site Generator",
        "category": "Cloud & Web",
        "description": "Motor de sitios para conferencias técnicas con Flask, optimizado "
                       "para Google Cloud Run con deploy desde source.",
        "link": "https://conference-site-383578626035.us-central1.run.app",
        "icon": "🎤"
    },
]

# ── Stack Tecnológico ────────────────────────────────────────────────
SKILLS = {
    "AI & LLM": ["AWS Bedrock", "Vertex AI", "LangGraph", "LangChain", "RAG", "MCP"],
    "Cloud & Infra": ["AWS", "GCP", "Kubernetes/EKS", "Terraform", "Docker", "Helm"],
    "SRE & DevOps": ["CI/CD", "ArgoCD", "Datadog", "Prometheus", "PagerDuty", "SLO/SLI"],
    "Dev": ["Python", "FastAPI", "Flask", "JavaScript", "React", "Bash"],
}

# ── Rutas ────────────────────────────────────────────────────────────
@app.route('/')
def home():
    return render_template(
        'index.html',
        profile=USER_PROFILE,
        projects=PROJECTS,
        skills=SKILLS,
        datetime=datetime
    )

@app.route('/download-cv')
def download_cv():
    """Forzar descarga del CV en PDF."""
    return send_from_directory(
        os.path.join(app.static_folder, 'assets'),
        'CV-Miguel-Carvajal.pdf',
        as_attachment=True,
        download_name='CV-Miguel-Carvajal-2026.pdf'
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
