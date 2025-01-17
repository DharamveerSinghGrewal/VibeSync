import os
from google.cloud import vision

def detect_emotion(image_path):
    """Detects emotions from the uploaded image using Google Vision API."""
    # Ensure credentials are set
    if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
        raise EnvironmentError("GOOGLE_APPLICATION_CREDENTIALS environment variable is not set.")

    # Initialize Vision API client
    client = vision.ImageAnnotatorClient()

    # Load image into memory
    with open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Perform label detection (you can adjust based on API capabilities)
    response = client.face_detection(image=image)

    if response.error.message:
        raise Exception(f"Google Vision API error: {response.error.message}")

    # Extract emotion annotations
    emotions = {
        "joy": response.face_annotations[0].joy_likelihood if response.face_annotations else "UNKNOWN",
        "sorrow": response.face_annotations[0].sorrow_likelihood if response.face_annotations else "UNKNOWN",
        "anger": response.face_annotations[0].anger_likelihood if response.face_annotations else "UNKNOWN",
        "surprise": response.face_annotations[0].surprise_likelihood if response.face_annotations else "UNKNOWN",
    }

    return emotions
