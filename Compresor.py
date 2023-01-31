from PIL import Image

import os

Descargas= "/home/seba/Descargas/" 

if __name__ == "__main__" :
    for filename in os.listdir(Descargas):
        name,extension = os.path.splitext(Descargas+ filename)
        if extension  in [".jpg",".png",".jpeg"]:
            foto= Image.open(Descargas+filename)
            foto.save(Descargas+ "compressed_"+filename,optimize=True,quality=10)

