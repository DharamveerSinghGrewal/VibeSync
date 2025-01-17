from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/results', methods=['POST'])
def results():
    # Placeholder: Process image and generate results
    detected_emotion = "Happy"  # Temporary hardcoded value
    recommended_songs = ["Song 1", "Song 2", "Song 3"]  # Temporary hardcoded list
    return render_template('results.html', emotion=detected_emotion, songs=recommended_songs)