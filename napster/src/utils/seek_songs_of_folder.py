import os
import eyed3


def seek_songs_of_folder():
    for root,  dirs, files in os.walk(path):
        for file in files:
            try:
                if file.find(".mp3") < 0:
                    continue
                path = os.path.abspath(os.path.join(root, file))
                t = eyed3.load(path)
                print(t.tag.title, t.tag.artist)
                # print(t.getArtist())
            except Exception as e:
                print(e)
                continue
