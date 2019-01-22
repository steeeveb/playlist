class AddPlaylistVideoUsecase:
    def __init__(self, video_repository, playlist_repository, video_playlist_repository):
        self.video_repository = video_repository
        self.playlist_repository = playlist_repository
        self.video_playlist_repository = video_playlist_repository

    def execute(self, playlist_id, video_id):
        self.playlist_repository.get(playlist_id)
        self.video_repository.get(video_id)
        self.video_playlist_repository.insert_video(playlist_id, video_id)


class DeletePlaylistVideoUsecase:
    def __init__(self, playlist_repository, video_playlist_repository):
        self.video_playlist_repository = video_playlist_repository
        self.playlist_repository = playlist_repository

    def execute(self, playlist_id, video_id):
        self.playlist_repository.get(playlist_id)
        self.video_playlist_repository.delete_video(playlist_id, video_id)


class GetPlaylistVideosUsecase:
    def __init__(self, playlist_repository, video_playlist_repository, video_repository):
        self.video_playlist_repository = video_playlist_repository
        self.video_repository = video_repository
        self.playlist_repository = playlist_repository

    def get_all(self, playlist_id):
        self.playlist_repository.get(playlist_id)
        video_ids = self.video_playlist_repository.get(playlist_id)
        videos = self.video_repository.get_all(*video_ids)
        return {'data': [{'id': video.id, 'title': video.title, 'thumbnail': video.thumbnail} for video in videos]}
