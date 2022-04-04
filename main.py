#Installer Pytube depuis github
from pytube import YouTube

#url="https://www.youtube.com/watch?v=KxdmigBTh74"
#url="https://www.youtube.com/watch?v=9l9Wa-5ph6o"
while True:
    url=input("Donner l'url de la vidéo Youtube à télécharger :")
    #vERIFIER que l'Url commence par https://www.youtube.com
    BASE_YOUTUBE_URL="https://www.youtube.com"
    if url.lower().startswith(BASE_YOUTUBE_URL):
        break
    print("Vous devez entrez une Url de vidéo Youtube!!!")



def on_downald_progress(stream,chunk,byte_remaining):
    bytes_downalded=stream.filezsize-byte_remaining
    percent=bytes_downalded*100 /stream.filezsize
    print(f"Progression de téléchargement {int(percent)} %")

youtube_video=YouTube(url)
youtube_video.register_on_progress_callback(on_downald_progress)
print("Titre : "+youtube_video.title)
print("NB VUES: ",youtube_video.views)
print("AUTHOR :",youtube_video.author)

#Pour une video choisir un flux (selon la resolution, audio ou vidéo)
print("-- CHOIX DES RESOLUTIONS "
      "")
streams=youtube_video.streams.filter(progressive=True,file_extension='mp4')
for i in range(len(streams)):
    print(f"{i+1}-{streams[i].resolution}")
print("Choissisez votre Resolution")



stream = youtube_video.streams.get_lowest_resolution()
print("Téléchargement ...")
#Pourcentage de programmation
stream.download()
print("ok")









