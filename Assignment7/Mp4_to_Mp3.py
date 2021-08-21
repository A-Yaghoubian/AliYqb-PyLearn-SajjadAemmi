from moviepy import editor
video = editor.VideoFileClip('test.mp4') # Your MP4 Address
video.audio.write_audiofile('test.mp3') # Your MP3 Address