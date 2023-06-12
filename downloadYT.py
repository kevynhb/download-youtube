from pytube import YouTube
import os
import time

inicio = time.time()
# Obtém informações do vídeo em um objeto do tipo Youtube
yt = YouTube("https://youtu.be/72fneIUHXyY")

# Define a pasta onde os vídeos serão baixados
pasta_videos = os.getcwd() + os.sep + "videos"

# Recupera a maior resolução disponível para o video
video = yt.streams.get_highest_resolution()

# Realiza o download do vídeo na pasta definida
video.download(output_path=pasta_videos)

fim = time.time()
tempo_total = fim - inicio
print("O video levou ", tempo_total, " segundos para baixar!")