from core.models import Playlist, Video


class MissingPlaylist(Exception):
    pass


class InMemoryPlaylistRepository:
    def __init__(self, storage):
        self.storage = storage
        self.counter = 0

    def get(self, playlist_id):
        try:
            return self.storage[playlist_id]
        except KeyError:
            raise MissingPlaylist()

    def get_all(self):
        return list(self.storage.values())

    def delete(self, playlist_id):
        del self.storage[playlist_id]

    def insert(self, playlist):
        # da rivedere
        self.counter = max(self.counter + 1, playlist.id or 0)
        self.storage[self.counter] = Playlist(self.counter, playlist.name)

    def update(self, playlist):
        self.storage[playlist.id] = playlist


class MysqlPlaylistRepository:
    pass


class InMemoryVideoRepository:
    def __init__(self, storage):
        self.storage = storage
        self.counter = 0

    def get_all(self, *video_ids):
        if video_ids:
            return list(v for v in self.storage.values() if v.id in video_ids)
        return list(self.storage.values())

    def get(self, video_id):
        try:
            return self.storage[video_id]
        except KeyError:
            raise MissingVideo()

    def delete(self, video_id):
        del self.storage[video_id]

    def insert(self, video):
        # da rivedere
        self.counter = max(self.counter + 1, video.id or 0)
        self.storage[self.counter] = Video(self.counter, video.title, video.thumbnail)


class MysqlVideoRepository:
    pass


class InMemoryPlaylistVideoRepository:
    def __init__(self, storage):
        self.storage = storage
    def get(self, playlist_id):
        return self.storage[playlist_id]
    def delete_video(self, playlist_id, video_id):
        self.storage.setdefault(playlist_id, []).remove(video_id)
    def insert_video(self, playlist_id, video_id):
        self.storage.setdefault(playlist_id, []).append(video_id)


class MissingVideo(Exception):
    pass