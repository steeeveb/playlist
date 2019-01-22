from core.models import Playlist


class AddPlaylistUsecase:
    def __init__(self, playlist_repository):
        self.playlist_repository = playlist_repository

    def execute(self, data):
        playlist = Playlist(None, data['name'])
        self.playlist_repository.insert(playlist)


class GetPlaylistsUsecase:
    def __init__(self, playlist_repository):
        self.playlist_repository = playlist_repository

    def get_all(self):
        playlists = self.playlist_repository.get_all()
        return {'data': [{'id': playlist.id, 'name': playlist.name} for playlist in playlists]}

    def get(self, playlist_id):
        playlist = self.playlist_repository.get(playlist_id)
        return {'data': {'id': playlist.id, 'name': playlist.name}}


class DeletePlaylistUsecase:
    def __init__(self, playlist_repository):
        self.playlist_repository = playlist_repository
    def execute(self, playlist_id):
        self.playlist_repository.delete(playlist_id)


class UpdatePlaylistUsecase:
    def __init__(self, playlist_repository):
        self.playlist_repository = playlist_repository
    def update(self, playlist_id, data):
        playlist = Playlist(playlist_id, data['name'])
        self.playlist_repository.update(playlist)

