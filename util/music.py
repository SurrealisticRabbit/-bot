class Song():
    def __init__(self):
        self.title: str = ""
        self.artist: str = ""
        self.album: str = ""
        self.duration: int = 0

class LocalSong(Song):
    def __init__(self):
        super().__init__()
        self.path: str = ""
        self.codec: str = ""
        self.bitrate: int = 0
        
    
        
    

