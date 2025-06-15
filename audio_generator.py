

# The following is a simple example of how to use the telethon library to send a message to a Telegram channel.
import moviepy.editor as mp
from timings import Timings
from voice_timings import voice_timings
def save_audio_from_video(source_path, destination_path, filename):
    clip = mp.AudioFileClip(source_path + filename+".mp4")
    clip.write_audiofile(destination_path+filename+".mp3")


def save_subclips(source_path, destination_path, filename, audiolist: list[Timings]):
    for index,obj in enumerate(audiolist):
        finalclip=mp.AudioFileClip(source_path+filename+".mp3").subclip(0,0)
        starttime=(obj.start_minute * 60)+(obj.start_second)-1
        endtime = (obj.end_minute * 60) + (obj.end_second) + 1
        clip = mp.AudioFileClip(source_path+filename+".mp3").subclip(starttime,endtime)
        finalclip=mp.concatenate_audioclips([finalclip,clip])
        finalclip.write_audiofile(destination_path+filename+f"subclip-{index}.mp3")

audio_path = '/Users/lokeshmanideep/Downloads/KrishnasVoice/Audios/'
video_path = '/Users/lokeshmanideep/Downloads/KrishnasVoice/Videos/'
subclips_path = '/Users/lokeshmanideep/Downloads/KrishnasVoice/Subclips/'
for key,value in voice_timings.items():
    if int(key) == 14:
        print(key)
        filename = key
        audio_list = voice_timings[filename]
        #finalclip = mp.VideoFileClip(video_path+filename + ".mp4").audio
        #finalclip.write_audiofile(audio_path+filename.split(".")[0]+".mp3")
        save_subclips(audio_path,subclips_path,filename,audio_list)