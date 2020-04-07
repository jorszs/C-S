
# TO DO: exportar este schema copiarlo a=song_schema.copy() para editarlo y guardarlo en la base de datos
song_Schema = {
    "title": None,
    "artist": None,
    "album": None,
    "song": None,

    "user": {
        "ip": None,
        "port": None
    }
}


def cancion(ar_cancion):
    return {
        "titulo": "el desorden",
        "artista": "ozuna",
        "album": "el desorden",
        "cancion": str(ar_cancion)
    }
