# VibeSync: Emotion-Based Music Recommendation System 🎵

VibeSync is a full-stack web application that bridges technology and creativity by recommending songs based on emotions detected in user-uploaded images. This project leverages advanced APIs and modern web technologies to create a fun and engaging experience while demonstrating scalable and deployable solutions.

Live Demo: [VibeSync](https://vibe-sync-1037638874998.northamerica-northeast2.run.app)

---

## 🌟 Features
- **Emotion Detection:** Uses Google Vision AI to analyze uploaded images and determine the user's emotion (e.g., joy, sorrow, anger).
- **Music Recommendation:** Integrates Spotify API to recommend mood-appropriate songs tailored to the detected emotion.
- **Interactive User Interface:** A sleek, modern interface for uploading images and displaying music recommendations.
- **Cloud Deployment:** Dockerized and deployed on Google Cloud Run for scalability and seamless access.

---

## 🖯 Motivation
With the abundance of music available online, finding the right playlist for your mood can be overwhelming. VibeSync solves this by combining AI-powered emotion detection with curated music recommendations, offering a unique and personalized experience.

This project serves as a showcase of full-stack development skills, advanced API integrations, and modern deployment practices.

---

## 🔧️ Tech Stack

### Backend:
- **Flask**: Lightweight web framework for routing and API handling.
- **Google Vision AI**: Emotion analysis from images.
- **Spotify API**: Song recommendations based on detected emotions.

### Frontend:
- **HTML5, CSS3**: Responsive and professional user interface.

### Deployment:
- **Docker**: Containerization for consistent environments.
- **Google Cloud Run**: Managed serverless platform for scalable deployment.
- **Google Artifact Registry**: Secure image storage for container deployment.

---

## 🚀 Deployment
The application is live and accessible via [Google Cloud Run](https://vibe-sync-1037638874998.northamerica-northeast2.run.app). It uses Docker containers to ensure a consistent environment and leverages Google Cloud's serverless capabilities for scalability.

---

## 📂 Project Structure
```
vibe-sync/
├── app/
│   ├── __init__.py        # Flask app factory
│   ├── routes.py          # Backend routes for image upload and results
│   ├── services/
│   │   ├── vision_service.py  # Google Vision AI logic
│   │   ├── spotify_service.py # Spotify API integration
│   ├── static/            # Static files (CSS, uploads)
│   └── templates/         # HTML templates
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
├── run.py                 # App entry point
└── README.md              # Project documentation
```

---

## 🌐 Key APIs Used
1. **Google Vision AI:**
   - Detects emotions such as joy, sorrow, anger, and surprise from images.
   - Provides confidence scores for each detected emotion.

2. **Spotify API:**
   - Maps emotions to appropriate music genres (e.g., "joy" → "happy").
   - Retrieves song recommendations with embedded Spotify players.

---

## 🧠 Key Learnings and Challenges
1. **API Integration:**
   - Handling OAuth-based authentication for Spotify.
   - Parsing and processing responses from Google Vision and Spotify APIs.
2. **Containerization and Deployment:**
   - Building and deploying Docker images on Google Cloud Run.
   - Managing environment variables securely with Cloud Run.
3. **Frontend-Backend Interaction:**
   - Dynamic rendering of images and playlists in Flask.
   - Ensuring responsive design across devices.

---

## ⚙️ Running Locally

### Prerequisites
- Docker installed on your machine.
- Google Vision API credentials (`GOOGLE_APPLICATION_CREDENTIALS`).
- Spotify API credentials (`SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET`).

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/DharamveerSinghGrewal/vibe-sync.git
   cd vibe-sync
   ```
2. Build and run the Docker container:
   ```bash
   docker build -t vibe-sync .
   docker run -p 8080:8080 vibe-sync
   ```
3. Access the app locally at `http://127.0.0.1:8080`.

---

## 🔒 Security and Best Practices
- **Environment Variables:** API credentials are passed securely using environment variables during deployment.
- **Dockerization:** Ensures consistency across environments.
- **Cloud Run Deployment:** Provides serverless scalability and minimizes attack surface.

---

## 🎉 Future Enhancements
- **User Profiles:** Save favorite songs and emotions for personalized recommendations.
- **Enhanced Recommendations:** Improve emotion-to-music mapping using AI/ML models.
- **Multi-Language Support:** Add support for non-English music recommendations.

---

## 💼 Why This Project?
VibeSync showcases practical skills relevant to modern software development:
- **Full-Stack Proficiency:** Covers frontend, backend, and cloud deployment.
- **API Mastery:** Integrates multiple real-world APIs with robust error handling.
- **Scalability:** Deployed using Docker and Google Cloud for real-world use cases.
---


