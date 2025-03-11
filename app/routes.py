import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from .transcriber import transcribe_audio
from .summarizer import summarize_text

main = Blueprint("main", __name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"mp3", "wav", "m4a"}

# Ensure uploads directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if uploaded file has an allowed extension"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Meeting Transcriber API is running!"})

@main.route("/transcribe", methods=["GET"])
def transcribe_info():
    return jsonify({"message": "Use POST to send an audio file."}), 405

@main.route("/transcribe", methods=["POST"])
def transcribe():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]  # FIXED SYNTAX ERROR

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type. Allowed: mp3, wav, m4a"}), 400

    # Secure and save the file
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    try:
        # Transcribe audio
        transcript = transcribe_audio(filepath)

        # Summarize text
        summary = summarize_text(transcript)

        return jsonify({
            "filename": filename,
            "transcript": transcript,
            "summary": summary
        })
    
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500
