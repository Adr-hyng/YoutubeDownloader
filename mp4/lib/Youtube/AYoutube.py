from urllib.error import URLError
from lib.Youtube import AResolution

class Youtube:
    def __init__(self,  url: str = None):
        from pytube.cli import on_progress
        from pytube import YouTube
        from pytube import request
        request.default_range_size = 1048576
        self.yt = YouTube(url, on_progress_callback = on_progress, on_complete_callback=self.complete_callback) if url is not None else None
        
        self.resolution =  AResolution.Resolution(self.yt)
        self.res = None

    def previous_and_next(self, iterateList: list):
        from itertools import tee, chain, islice
        prevs, items, nexts = tee(iterateList, 3)
        prevs = chain([None], prevs)
        nexts = chain(islice(nexts, 1, None), [None])
        return zip(prevs, items, nexts)
    
    def complete_callback(self, stream, file_handle):
        print(f"\n{self.filename} {self.res} Download Completed!")
    
    def bulk_download(self, textFile: str, outputPath: str, resolution: str = "2160p"):
        with open(textFile, "r") as file:
            for link in file:
                yt = Youtube(link.strip())
                resolution = resolution if int(resolution[:-1]) in yt.resolution.get_resolutions() else yt.resolution.get_default_res(resolution)
                yt.download(outputPath, resolution) 
            
    def download(self, outputPath: str, resolution: str): 
        from urllib.error import URLError 
        from sys import stdout
        title = self.yt.title.translate ({ord(c): "-" for c in "\/:*?<>|"})
        extension = "mp4"
        try:
            if int(resolution[:-1]) in self.resolution.get_resolutions():
                video = self.yt.streams.filter(res = resolution, progressive = True, file_extension = extension).first()
                if video is not None:
                    text = f"\n{self.yt.title} ({resolution}).{extension}\n\r"
                    stdout.write(text)
                    stdout.flush()
                    self.res = resolution
                    self.filename = self.yt.title
                    video.download(output_path = outputPath, filename = f"{title} ({resolution}).{extension}")
                else:
                    resolution = self.resolution.get_default_res(resolution)
                    self.filename = self.yt.title
                    self.res = resolution
                    self.download(outputPath, resolution) 
            else:
                resolution = self.resolution.get_default_res(resolution)
                self.download(outputPath, resolution)    
            
        except URLError:
            print(f"Connection Lost")
        
        