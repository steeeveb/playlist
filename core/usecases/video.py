from core.models import Video


class AddVideoUsecase:
    def __init__(self, video_repository):
        self.video_repository = video_repository

    def execute(self, data):
        video = Video(None, data['title'], data['thumbnail'])
        self.video_repository.insert(video)


class GetVideosUsecase:
    def __init__(self, video_repository):
        self.video_repository = video_repository

    def get(self):
        videos = self.video_repository.get_all()
        return {'data': [{'id': video.id, 'title': video.title, 'thumbnail': video.thumbnail} for video in videos]}


class DeleteVideoUsecase:
    def __init__(self, video_repository, playlist_video_repository):
        self.video_repository = video_repository
        self.playlist_video_repository = playlist_video_repository

    def execute(self, video_id):
        self.video_repository.delete(video_id)
        self.playlist_video_repository.delete_all(video_id)


