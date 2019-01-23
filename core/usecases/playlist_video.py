class PlaylistsVideosUsecases:
    def __init__(self, playlist_repository, playlist_video_repository, video_repository):
        self.playlist_repository = playlist_repository
        self.video_repository = video_repository
        self.playlist_video_repository = playlist_video_repository

    def get_all(self, playlist_id):
        self.playlist_repository.get(playlist_id)
        video_ids = self.playlist_video_repository.get(playlist_id)
        videos = self.video_repository.get_all(*video_ids)
        return {'data': [{'id': video.id, 'title': video.title, 'thumbnail': video.thumbnail} for video in videos]}

    def add(self, playlist_id, video_id):
        self.playlist_repository.get(playlist_id)
        self.video_repository.get(video_id)
        self.playlist_video_repository.insert_video(playlist_id, video_id)

    def delete(self, playlist_id, video_id):
        self.playlist_repository.get(playlist_id)
        self.playlist_video_repository.delete(playlist_id, video_id)
