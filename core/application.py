from core.usecases.playlist import PlaylistsUsecases
from core.usecases.playlist_video import PlaylistsVideosUsecases
from core.usecases.video import VideosUsecases


class Application:
    def __init__(self, playlist_repository, playlist_video_repository, video_repository):
        self.playlists_usecases = PlaylistsUsecases(playlist_repository, playlist_video_repository)
        self.playlists_videos_usecases = PlaylistsVideosUsecases(playlist_repository, playlist_video_repository, video_repository)
        self.videos_usecases = VideosUsecases(video_repository, playlist_video_repository)

    def add_video(self, data):
        self.videos_usecases.add(data)

    def get_videos(self):
        return self.videos_usecases.get()

    def delete_video(self, video_id):
        self.videos_usecases.delete(video_id)

    def add_playlist(self, data):
        self.playlists_usecases.add(data)

    def change_playlist(self, playlist_id, data):
        self.playlists_usecases.update(playlist_id, data)

    def get_playlist(self, playlist_id):
        return self.playlists_usecases.get(playlist_id)

    def get_playlists(self):
        return self.playlists_usecases.get_all()

    def delete_playlist(self, playlist_id):
        self.playlists_usecases.delete(playlist_id)

    def add_playlist_video(self, playlist_id, video_id):
        self.playlists_videos_usecases.add(playlist_id, video_id)

    def get_playlist_videos(self, playlist_id):
        return self.playlists_videos_usecases.get_all(playlist_id)

    def delete_playlist_video(self, playlist_id, video_id):
        self.playlists_videos_usecases.delete(playlist_id, video_id)