
import moviepy.editor as mp
from timings import *
audio_path = '/Users/lokeshmanideep/Downloads/KrishnasVoice/Audios/'
video_path = '/Users/lokeshmanideep/Downloads/KrishnasVoice/Videos/'
subclips_path = '/Users/lokeshmanideep/Downloads/KrishnasVoice/Subclips copy/'
final_subclips_path = '/Users/lokeshmanideep/Downloads/KrishnasVoice/FinalSubclips/'
filename = "1subclip"
finalclip = mp.AudioFileClip(subclips_path+filename+ ".mp3")
audio_list = subclip_timings[filename]
for index,obj in enumerate(audio_list):
    starttime=(obj.start_minute * 60)+(obj.start_second)
    endtime = (obj.end_minute * 60) + (obj.end_second)
    clip = finalclip.subclip(starttime,endtime)
    clip.write_audiofile(final_subclips_path+filename+f"-{index}.mp3")


