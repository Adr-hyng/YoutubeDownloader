import pytube
from lib.Youtube import AYoutube

class Playlist:
    
    def __init__(self, playlistURL: str):
        self.playlist_url = playlistURL
        self.playlist = pytube.Playlist(playlistURL)
    
    def get_number_videos(self):
        print('Number of videos in playlist: %s' % len(self.playlist.video_urls))
        
    def get_videos(self):
        for i, video in enumerate(self.playlist.videos):
            print(f"{i+1}. {video.title}")
    
    def download(self, outputPath: str, resolution: str = "2160p"):
        for url in self.playlist.video_urls:
            yt = AYoutube.Youtube(url)
            resolution = resolution if int(resolution[:-1]) in yt.resolution.get_resolutions() else yt.resolution.get_default_res(resolution)
            yt.download(outputPath, resolution)