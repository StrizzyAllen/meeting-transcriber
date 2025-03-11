import whisper
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

def transcribe_audio(filepath):
    model = whisper.load_model("base")  # Ensuring correct model loading
    result = model.transcribe(filepath)
    return result["text"]
