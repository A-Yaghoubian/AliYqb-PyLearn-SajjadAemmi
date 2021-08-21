from moviepy import editor
video = editor.VideoFileClip('E:\programming\PyLearn-SajjadAemmi\Assignment7\khande dar.mp4') # Your MP4 Address
video.audio.write_audiofile('E:\programming\PyLearn-SajjadAemmi\Assignment7\khande dar.mp3') # Your MP3 Address
