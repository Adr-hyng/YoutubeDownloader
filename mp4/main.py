from lib import APlaylist
from lib.Youtube import AYoutube

"""
!Bugs:
- Can only select the available Resolution because of the library "Pytube".
"""

if __name__ == '__main__':
    from os import getcwd
    this = getcwd() + '\downloads\ '[:-1]
    pl = APlaylist.Playlist("https://www.youtube.com/playlist?list=PLHMbEPQsIZ9z7GHyPn4I1mFdI8FLzoJSX")
    pl.download(this)
    