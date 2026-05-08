# Google Cloud Innovate: Condesa 2026 — Conference Site

A **1-day technical conference informational website** focused on Google Cloud Technologies.
Built with **Python/Flask** on the backend and **Vanilla HTML/CSS/JS** on the frontend.

---

## 📁 Project Structure

```
workshop2/
├── app.py                  # Flask backend (data, routes)
├── requirements.txt        # Python dependencies
├── Dockerfile              # For Cloud Run deployment
├── README.md               # This file
├── static/
│   ├── css/
│   │   └── style.css       # Premium styles (glassmorphism, animations)
│   └── js/
│       └── main.js         # Client-side search logic
└── templates/
    └── index.html          # Main page (Jinja2 template)
```

---

## 🚀 Setup & Run Locally

### Prerequisites

- Python 3.9+ installed
- pip

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Development Server

```bash
python app.py
```

The app runs on **http://localhost:8080**.

---

## 🔍 Functionality

| Feature | Details |
|---|---|
| **Schedule** | 8 GCP talks in a single-track timetable with a lunch break |
| **Search** | Real-time filter by talk title, speaker name, or category |
| **Speaker Links** | Each speaker links to their LinkedIn profile |
| **Categories** | Each talk is tagged with 1–2 technology categories |

---

## 📝 Modifying Data

All conference data lives at the top of `app.py`:

### Change Conference Info

```python
CONFERENCE_INFO = {
    "title": "Your Conference Name",
    "date": "May 1, 2026",
    "location": "Your City",
    "description": "Your description..."
}
```

### Add/Edit a Speaker

```python
SPEAKERS = [
    {"id": 7, "first_name": "Jane", "last_name": "Doe", "linkedin": "https://linkedin.com/in/janedoe"},
    ...
]
```

### Add/Edit a Talk

```python
TALKS = [
    {
        "id": "T9",
        "title": "New Talk Title",
        "speaker_ids": [7],             # References SPEAKERS IDs
        "categories": ["AI", "Data"],
        "description": "Talk description...",
        "time": "06:00 PM"
    },
    ...
]
```

> **Note:** The lunch break automatically appears after the **3rd talk**. To change its position, update the `loop.index` check in `templates/index.html` (line: `{% if loop.index == 4 %}`).

---

## ☁️ Deploy to Google Cloud Run

> Step-by-step guide including all gcloud commands required to set up and deploy from scratch.

### Prerequisites

- [gcloud CLI](https://cloud.google.com/sdk/docs/install) installed and logged in.
- A Google account with access to Google Cloud.

### Step 1 — Authenticate (if not done already)

```bash
gcloud auth login
```

### Step 2 — Create a new GCP project

```bash
gcloud projects create YOUR_PROJECT_ID --name="Your Project Name"
```

Example:

```bash
gcloud projects create mx-coatl-aicondesa-workshop02 --name="AI Condesa Workshop 02"
```

### Step 3 — Set the new project as active

```bash
gcloud config set project YOUR_PROJECT_ID
```

Verify it:

```bash
gcloud config get-value project
```

### Step 4 — List your billing accounts

```bash
gcloud billing accounts list
```

Look for accounts with `OPEN: True`.

### Step 5 — Link a billing account to your project

```bash
gcloud billing projects link YOUR_PROJECT_ID --billing-account=YOUR_BILLING_ACCOUNT_ID
```

Example:

```bash
gcloud billing projects link mx-coatl-aicondesa-workshop02 --billing-account=01308E-141324-F98114
```

You should see `billingEnabled: true` in the output.

### Step 6 — Enable required APIs

```bash
gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com
```

This enables:
- **Cloud Run** — to run the application
- **Cloud Build** — to build the Docker image from source
- **Artifact Registry** — to store the container image

### Step 7 — Deploy from source

Navigate to the project folder and run:

```bash
gcloud run deploy conference-site \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8080
```

When prompted to create an Artifact Registry repository, type **`Y`** to confirm.

Cloud Run will:
1. Build the Docker image using the `Dockerfile`
2. Push the image to Artifact Registry
3. Deploy the service to Cloud Run
4. Return a public HTTPS URL

### Step 8 — Access the live site

After a successful deploy, you'll see output like:

```
Service URL: https://conference-site-383578626035.us-central1.run.app
```

Open that URL in your browser to see the live site.

---

## 🧪 API Endpoint

The app also exposes a JSON API for programmatic access:

- **`GET /api/talks`** — Returns all 8 talks with full speaker data as JSON.

---

## 🎨 Customizing the Design

Styles are in `static/css/style.css`. The theme uses CSS custom properties at the top:

```css
:root {
    --primary: #4285F4;       /* Google Blue */
    --bg-dark: #0f172a;       /* Dark background */
    --text-muted: #94a3b8;    /* Muted text */
}
```

Change these to instantly retheme the entire site.
