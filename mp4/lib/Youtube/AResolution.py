
class Resolution:
    def __init__(self, Youtube):
        self.youtube = Youtube
        
    def get_resolutions(self):
        resolutions = []
        for stream in self.youtube.streams:
            if stream.resolution is not None:
                resolutions.append(int(stream.resolution[:-1]) if isinstance(int(stream.resolution[:-1]), int) else 0)
        resolutions.sort()
        return sorted(list(set(resolutions)))
    
    def get_second_high_res(self):
        resolutions = []
        for stream in self.youtube.streams:
            if stream.resolution is not None:
                resolutions.append(int(stream.resolution[:-1]) if isinstance(int(stream.resolution[:-1]), int) else 0)
        resolutions.sort()
        resolutions = list(set(resolutions))
        return f"{resolutions[-2]}p"
          
    def get_highest_res(self):
        resolutions = []
        for stream in self.youtube.streams:
            if stream.resolution is not None:
                resolutions.append(int(stream.resolution[:-1]) if isinstance(int(stream.resolution[:-1]), int) else 0)
        resolutions.sort()
        resolutions = list(set(resolutions))
        return f"{resolutions[-1]}p"
    
    def get_lowest_res(self):
        resolutions = []
        for stream in self.youtube.streams:
            if stream.resolution is not None:
                resolutions.append(int(stream.resolution[:-1]) if isinstance(int(stream.resolution[:-1]), int) else 0)
        resolutions.sort()
        resolutions = list(set(resolutions))
        return f"{resolutions[0]}p"
    
    def get_default_res(self, resolution: str):
        if len(resolution) >= 4: # Needs 4 or more characters
            if int(resolution[:-1]) in self.get_resolutions(): # When value of resolution is valid
                index = self.get_resolutions().index(int(resolution[:-1]))
                if index > 1:
                    index -= 1
                    return f"{self.get_resolutions()[index]}p"
        return f"{self.get_resolutions()[-1]}p"
            
        