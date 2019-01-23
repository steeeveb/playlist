from core.models import Video


class VideosUsecases:
    def __init__(self, video_repository, playlist_video_repository):
        self.video_repository = video_repository
        self.playlist_video_repository = playlist_video_repository

    def get(self):
        videos = self.video_repository.get_all()
        return {'data': [{'id': video.id, 'title': video.title, 'thumbnail': video.thumbnail} for video in videos]}

    def add(self, data):
        video = Video(None, data['title'], data['thumbnail'])
        self.video_repository.insert(video)

    def delete(self, video_id):
        self.video_repository.delete(video_id)
        self.playlist_video_repository.delete_all(video_id)


