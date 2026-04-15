from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

# Dummy Data
CONFERENCE_INFO = {
    "title": "Google Cloud Innovate: Condesa 2026",
    "date": "April 14, 2026",
    "location": "Google Condesa Office, Mexico City",
    "description": "A high-impact technical conference exploring the latest in Cloud Infrastructure, Generative AI, and Data Analytics on GCP."
}

SPEAKERS = [
    {"id": 1, "first_name": "Elena", "last_name": "Rodriguez", "linkedin": "https://linkedin.com/in/elenarodriguez-gcp"},
    {"id": 2, "first_name": "Marcus", "last_name": "Chen", "linkedin": "https://linkedin.com/in/marcuschen-dev"},
    {"id": 3, "first_name": "Sonia", "last_name": "Gupta", "linkedin": "https://linkedin.com/in/soniaguptacloud"},
    {"id": 4, "first_name": "David", "last_name": "Miller", "linkedin": "https://linkedin.com/in/davidmillerarch"},
    {"id": 5, "first_name": "Ana", "last_name": "Silva", "linkedin": "https://linkedin.com/in/anasilvalab"},
    {"id": 6, "first_name": "Kofi", "last_name": "Mensah", "linkedin": "https://linkedin.com/in/kofimensah-ops"}
]

TALKS = [
    {
        "id": "T1",
        "title": "Vertex AI: From Model to Production",
        "speaker_ids": [1],
        "categories": ["AI", "Machine Learning"],
        "description": "Learn how to deploy and scale generative models using Vertex AI pipelines and endpoint management.",
        "time": "09:30 AM"
    },
    {
        "id": "T2",
        "title": "Cloud Run Deep Dive: Serverless for Gophers",
        "speaker_ids": [2],
        "categories": ["Serverless", "Application Development"],
        "description": "Unveiling the internal architecture of Cloud Run and best practices for high-concurrency Go applications.",
        "time": "10:30 AM"
    },
    {
        "id": "T3",
        "title": "Scaling Kubernetes with GKE Autopilot",
        "speaker_ids": [3, 4],
        "categories": ["Infrastructure", "Kubernetes"],
        "description": "A hands-on guide to automating cluster management and optimizing costs with GKE Autopilot.",
        "time": "11:30 AM"
    },
    {
        "id": "T4",
        "title": "BigQuery: Processing Peta-Bytes in Seconds",
        "speaker_ids": [5],
        "categories": ["Data", "Analytics"],
        "description": "Advanced SQL techniques and the new BI Engine optimization for sub-second reporting.",
        "time": "01:30 PM"
    },
    {
        "id": "T5",
        "title": "Modern Security with BeyondCorp Enterprise",
        "speaker_ids": [6],
        "categories": ["Security", "Networking"],
        "description": "Implementing zero-trust architecture for remote development teams.",
        "time": "02:30 PM"
    },
    {
        "id": "T6",
        "title": "Pub/Sub Messaging for Real-Time Pipelines",
        "speaker_ids": [4],
        "categories": ["Networking", "Data"],
        "description": "Building resilient event-driven systems using Pub/Sub and Cloud Functions.",
        "time": "03:30 PM"
    },
    {
        "id": "T7",
        "title": "AlloyDB: The Evolution of PostgreSQL",
        "speaker_ids": [1, 2],
        "categories": ["Databases", "Performance"],
        "description": "How AlloyDB achieves 4x faster performance than standard PostgreSQL for analytical workloads.",
        "time": "04:30 PM"
    },
    {
        "id": "T8",
        "title": "The Future of GCP: Multicloud with Anthos",
        "speaker_ids": [3],
        "categories": ["Infrastructure", "Multicloud"],
        "description": "Managing complex hybrid-cloud environments with a single pane of glass using Anthos.",
        "time": "05:30 PM"
    }
]

# Helper to enrich talks with speaker objects
def get_enriched_talks():
    enriched = []
    for talk in TALKS:
        talk_speakers = [s for s in SPEAKERS if s["id"] in talk["speaker_ids"]]
        new_talk = talk.copy()
        new_talk["speaker_objs"] = talk_speakers
        enriched.append(new_talk)
    return enriched

@app.route('/')
def home():
    return render_template('index.html', info=CONFERENCE_INFO, talks=get_enriched_talks())

@app.route('/api/talks')
def api_talks():
    return jsonify(get_enriched_talks())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
