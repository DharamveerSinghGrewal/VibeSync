from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
import os
from app.services.vision_service import detect_emotion
from app.services.spotify_service import get_songs_by_emotion
main = Blueprint('main', __name__)

UPLOAD_FOLDER = "app/static/uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@main.route('/')
def home():
    
    return render_template('index.html')

@main.route('/results', methods=['POST'])
def results():
    if 'image' not in request.files:
        return "No file part in the request", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    # Save the uploaded image
    filename = secure_filename(file.filename)
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(image_path)

    try:
        # Detect emotions using Google Vision API
        emotions = detect_emotion(image_path)
        # Map the most prominent emotion
        detected_emotion = max(emotions, key=emotions.get).capitalize()
        # Get songs from Spotify based on the detected emotion
        recommended_songs = get_songs_by_emotion(detected_emotion)
    except Exception as e:
        return f"Error detecting emotion: {e}", 500

    return render_template('results.html', emotion=detected_emotion, songs=recommended_songs)