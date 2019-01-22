from typing import NamedTuple, Optional


class Video(NamedTuple):
    id: Optional[int]
    title: str
    thumbnail: str


class Playlist(NamedTuple):
    id: Optional[int]
    name: str
