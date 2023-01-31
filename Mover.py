from PIL import Image

import os

Descargas= "/home/seba/Descargas/" 

fotos="/home/seba/Imágenes/"
videos= "/home/seba/Vídeos/"
musica="/home/seba/Música/"

if __name__ == "__main__" :
    for filename in os.listdir(Descargas):
        name,extension = os.path.splitext(Descargas+ filename)
        if extension  in [".jpg",".png",".jpeg"]:
            foto= Image.open(Descargas+filename)
            foto.save(fotos+ "compressed_"+filename,optimize=True,quality=60)
        if extension in [".mp3"]:
            os.rename(Descargas + filename,musica+filename)
        if extension in [".mp4"]:
            os.rename(Descargas + filename,videos+filename)
            

