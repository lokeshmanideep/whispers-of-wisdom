import logging
from pathlib import Path
from dotenv import load_dotenv
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import translate_v2 as translate

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants (Customize as needed)
BASE_DIR = Path("/Users/lokeshmanideep/Downloads/KrishnasVoice")
TRANSCRIPTS_DIR = BASE_DIR / "Transcripts"
TRANSLATIONS_DIR = BASE_DIR / "Translations"
SUBCLIPS_DIR = BASE_DIR / "Subclips"

# Ensure output directories exist
TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
TRANSLATIONS_DIR.mkdir(parents=True, exist_ok=True)

def transcribe_audio(file_path: Path) -> str:
    """
    Transcribes speech from an audio file using Google Cloud Speech-to-Text.

    Args:
        file_path (Path): Path to the MP3 file.

    Returns:
        str: The full transcribed text.
    """
    logging.info(f"Transcribing audio: {file_path.name}")
    client = speech.SpeechClient()

    with file_path.open("rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        language_code="te-IN",
        sample_rate_hertz=44100,
        model="latest_long"
    )

    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=600)

    transcript_text = "\n".join(
        result.alternatives[0].transcript for result in response.results
    )

    transcript_path = TRANSCRIPTS_DIR / f"{file_path.stem}.txt"
    transcript_path.write_text(transcript_text, encoding="utf-8")
    logging.info(f"Transcript saved: {transcript_path}")
    
    return transcript_text


def translate_text(text: str, file_stem: str, target_language: str = "en", source_language: str = "te") -> None:
    """
    Translates text using Google Cloud Translate API.

    Args:
        text (str): Text to translate.
        file_stem (str): Output file name without extension.
        target_language (str): Language to translate to. Defaults to English.
        source_language (str): Original language. Defaults to Telugu.
    """
    logging.info(f"Translating text for: {file_stem}")
    translate_client = translate.Client()
    result = translate_client.translate(
        text,
        target_language=target_language,
        source_language=source_language
    )

    output_path = TRANSLATIONS_DIR / f"{file_stem}.txt"
    output_path.write_text(result["translatedText"], encoding="utf-8")
    logging.info(f"Translation saved: {output_path}")


if __name__ == "__main__":
    clip_name = "14subclip-1"
    audio_file = SUBCLIPS_DIR / f"{clip_name}.mp3"

    if not audio_file.exists():
        logging.error(f"Audio file not found: {audio_file}")
        exit(1)

    try:
        transcript = transcribe_audio(audio_file)
        translate_text(transcript, clip_name)
    except Exception as e:
        logging.exception(f"Error during processing: {e}")
