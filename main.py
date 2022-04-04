#Installer Pytube depuis github
from pytube import YouTube


url="https://www.youtube.com/watch?v=9l9Wa-5ph6o"

youtube_video=YouTube(url)

print("Titre : "+youtube_video.title)
print("NB VUES: ",youtube_video.views)
print("AUTHOR :",youtube_video.author)

#Pour une video choisir un flux (selon la resolution, audio ou vidéo)
print("STREAMS")
for stream in youtube_video.streams:
    print(" ",stream)