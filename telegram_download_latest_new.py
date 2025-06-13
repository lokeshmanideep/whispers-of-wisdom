import os
import time
import logging
from pathlib import Path
from moviepy.editor import VideoFileClip
from telethon import TelegramClient
from dotenv import load_dotenv
load_dotenv()


API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")
PHONE_NUMBER = os.getenv("TELEGRAM_PHONE_NUMBER")
CHANNEL_USERNAME = os.getenv("TELEGRAM_CHANNEL_USERNAME")  # Update with correct key
SESSION_NAME = "mahabharat"

AUDIO_DIR = Path("/Users/lokeshmanideep/Downloads/KrishnasVoice/Audios/")
VIDEO_DIR = Path("/Users/lokeshmanideep/Downloads/KrishnasVoice/Videos/")

# Ensure output directories exist
AUDIO_DIR.mkdir(parents=True, exist_ok=True)
VIDEO_DIR.mkdir(parents=True, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)


async def main():
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    await client.start(phone=PHONE_NUMBER)

    if not await client.is_user_authorized():
        await client.send_code_request(PHONE_NUMBER)
        code = input("Enter the verification code: ")
        await client.sign_in(PHONE_NUMBER, code)

    logger.info("Fetching messages...")
    messages = await client.get_messages(CHANNEL_USERNAME, limit=198)
    messages = list(reversed(messages))
    print(messages)
    for msg in messages:
        if not msg.media or not msg.media.document:
            continue

        try:
            filename = msg.media.document.attributes[0].file_name
            video_path = VIDEO_DIR / filename
            audio_filename = f"{video_path.stem}.mp3"
            audio_path = AUDIO_DIR / audio_filename

            start = time.time()
            await client.download_media(message=msg, file=video_path)
            logger.info(f"Downloaded: {filename} in {time.time() - start:.2f}s")

            # Extract audio
            audio = VideoFileClip(str(video_path)).audio
            audio.write_audiofile(str(audio_path))
            logger.info(f"Saved audio: {audio_filename}")

        except Exception as e:
            logger.error(f"Error processing message: {e}")

    await client.disconnect()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
