# Voice Notes Extraction & Automation

This project is my personal solution to a challenge I set for myself: I wanted to create a YouTube playlist of all of Lord Krishna's teachings from the Mahabharat TV series. Instead of doing everything by hand, I used a bit of code to automate the most repetitive parts.

While some steps still need a human touch, this workflow saved me a ton of time. Here's how it works.

## My Workflow

1. **Download Videos from Telegram**

   - I wrote a script to grab all the episodes from a Telegram channel. No more downloading each video one by one! The videos go straight into my `Videos` folder, and the audio is automatically pulled out and saved in `Audios`.

2. **Mark Krishna's Voice Timings**

   - This is the only part I couldn't automate. I watch each episode and note down the exact times when Lord Krishna speaks.

3. **Cut Out Krishna's Voice Clips**

   - Using the timings I collected, another script slices the audio files so I get just the parts where Krishna is speaking. These clips are saved for the next steps.

4. **Transcribe the Audio**

   - Each Krishna voice clip is sent to a speech-to-text API. The script gets back the transcription in the original language.

5. **Translate to English**

   - The transcription is then sent to a translation API, and I get the English version of Krishna's words.

6. **Create a Video**

   - Using the extracted voice notes, I use a video editing software to create a new video that highlights Krishna's messages. This part is still manual, but it's much faster now that I have all the clips and transcriptions ready.

7. **Generate Title & Description**

   - I use the transcript in step 5 to generate the video title and description using Gemini. I wrote the API call for this, but I prefer to do it manually so I can brainstorm the most suitable title and tweak the description as needed.

8. **Upload to YouTube**
   - Finally, I wrote a script (`video_uploader.py`) that uploads the finished video to YouTube. It even sets the title, description, tags, thumbnail, and adds the video to a playlist automatically. No more clicking through YouTube's upload page every time!

## Why This Was Fun

I didn't use any fancy tools—just Python scripts and some patience for the manual work. The scripts saved me a bunch of time in creating this playlist in my native language, Telugu. You can listen to the playlist here: [link](https://www.youtube.com/playlist?list=PLPgC7mD72GJ_rUG0khmdx-7CNDjRmxu-X)
