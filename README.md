# Telegram Download Daemon - Krishna's Voice Extraction Workflow

This project helps you download videos from a Telegram channel, extract Lord Krishna's voice from each episode, transcribe the audio, and translate it to English.

## Workflow Overview

1. **Download Videos from Telegram**

   - The script downloads all videos from a specified Telegram channel using the Telethon library.
   - Videos are saved in the `Videos` folder.
   - Audio is extracted from each video and saved in the `Audios` folder.

2. **Mark Voice Timings**

   - For each episode, you manually note down the start and end times where Lord Krishna speaks.
   - These timings are saved in the `timings.py` file.

3. **Cut Audio Clips**

   - Using the timings from `timings.py`, the script cuts the audio files to extract only the parts where Krishna speaks.
   - The cut audio clips are saved for further processing.

4. **Transcribe Audio to Text**

   - Each voice audio clip is sent to a speech-to-text API.
   - The API returns the original language transcription.

5. **Translate to English**
   - The original transcription is sent to a translation API.
   - The API returns the English translation of Krishna's speech.

## Folder Structure

├── telegram_download_latest_new.py # Downloads videos and extracts audio  
├── timings.py # Contains Krishna's voice timings for each episode  
├── audio_generator.py # Cuts audio clips based on timings  
├── transcribe.py # Transcribes and translates audio clips  
├── Audios/ # Folder for extracted audio files  
├── Videos/ # Folder for downloaded videos

## How to Use

1. **Set Up Environment**

   - Install dependencies:  
     `pip install -r requirements.txt`
   - Set your Telegram API credentials and channel username in a `.env` file.

2. **Download Videos and Extract Audio**

   - Run:  
     `python telegram_download_latest_new.py`
   - This will download videos and extract audio files.

3. **Mark Timings**

   - Watch each episode and note down Krishna's voice timings.
   - Add these timings to `timings.py`.

4. **Cut Krishna's Voice Clips**

   - Run:  
     `python audio_generator.py`
   - This will create audio clips for Krishna's voice.

5. **Transcribe and Translate**
   - Run:  
     `python transcribe.py`
   - This will transcribe the audio clips and translate them to English.

## Notes

- Make sure you have the correct API keys and access to the required APIs.
- The process of marking timings is manual and requires you to listen to each episode.
- All scripts are written in Python and should work on most systems.

---

Feel free to improve or automate any step as needed!
