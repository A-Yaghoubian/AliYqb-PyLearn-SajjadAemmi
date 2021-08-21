from moviepy import editor
video = editor.VideoFileClip('khande dar.mp4') # Your MP4 Address
video.audio.write_audiofile('khande dar.mp3') # Your MP3 Address
