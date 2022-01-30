from youtube_dl import YoutubeDL
from pytube import Playlist

class MusicDownloader:
    
    def __init__(self):
        pass
    
    def is_from_yt_playlist(self, url: str):
        return True if "&list=" in url else False
    
    def transform_url(self, url: str):
        return url[:url.find("&list=")]
    
    def from_file(self, textFile: str, outputFile: str):
        with open(textFile, "r") as file:
            for url in file:
                if self.is_from_yt_playlist(url):
                    url = self.transform_url(url)
                    self.download(url.strip(), outputFile)
                
    def from_playlist(self, playlistURL: str, outputFile: str):
        playlist = Playlist(playlistURL)
        for url in playlist.video_urls:
            self.download(url, outputFile)
            
        
            
    def download(self, youtubeURL: str, downloadBin: str):
        video_info = YoutubeDL().extract_info(
            url = youtubeURL, download = False
        )
        kbps = "320"
        filename = f"{downloadBin}{video_info['title']} ({kbps}kbps).mp3"
        options = {
        'format': 'bestaudio/best',
        'keepvideo':False,
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': kbps,
        }],
        }

        with YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        print("Download complete... {}".format(filename))