from mp3 import MusicDownloader

def run():
    from os import getcwd
    this = getcwd() + '\download\ '[:-1]
    mp3 = MusicDownloader()
    mp3.from_file("list.txt", this)

if __name__=='__main__':
    run()