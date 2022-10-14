from lib import APlaylist
from lib.Youtube import AYoutube

"""
!Bugs:

- When Span error occurs use this : python -m pip install git+https://github.com/pytube/pytube

- Can only select the available Resolution because of the library "Pytube
"""

if __name__ == '__main__':
    from os import getcwd
    this = getcwd() + '\downloads\ '[:-1]
    pl = APlaylist.Playlist("https://www.youtube.com/playlist?list=PLZm85UZQLd2SXQzsF-a0-pPF6IWDDdrXt")
    pl.download(this)
    # video = AYoutube.Youtube("https://www.youtube.com/watch?v=XCyuHSJS7XE")
    # video.bulk_download("download.txt", this)
    
    