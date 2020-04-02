import os
import eyed3
#import songdetails
from tinytag import TinyTag
#import eyeD3
# "Safaera - Bad Bunny x Jowell & Randy x Ñengo Flow _ YHLQMDLG (320  kbps) (ytmp3s.me).mp3"
path = "../songs/"
nombre = "el desorden"  # metallica-the-unforgiven-video"
extencion = ".mp3"


# tinytag
#tag = TinyTag.get(path+nombre+extencion)
#print("type: "+str(type(tag)))
#print("tamaño: "+str(tag.filesize))

# ----------

# buscar las canciones de una carpeta recibe la direccion de la carpeta


def importCancion_eyed3(path, nombre, extencion):
    songfield = eyed3.load(path+nombre+extencion)

    meta = {
        "title": songfield.tag.title,
        "album": songfield.tag.album,
        "artist": songfield.tag.artist
    }
    # print(songfield.function.filename)
    print(meta)
    # return meta


#importCancion_eyed3(path, nombre, extencion)
