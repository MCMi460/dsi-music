from dataclasses import dataclass, field
from typing import List

@dataclass
class Track:
    name:str
    artist:str
    album:str = ''

@dataclass
class Playlist:
    name:str
    creator:str = ''
    tracks:List[Track] = field(
        default_factory = lambda: []
    )
