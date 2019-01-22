from unittest import TestCase

from core.adapters import InMemoryVideoRepository, InMemoryPlaylistVideoRepository
from core.usecases.video import AddVideoUsecase, DeleteVideoUsecase, GetVideosUsecase
from core.models import Video


class AddVideoUsecaseTest(TestCase):
    def test_create_video(self):
        a_video = {
            'title': 'the title of the video',
            'thumbnail': 'The url of the video',
        }
        video_repository = InMemoryVideoRepository({})
        AddVideoUsecase(video_repository).execute(a_video)

        self.assertEqual({1: Video(1, 'the title of the video', 'The url of the video')},
                         video_repository.storage)


class DeleteVideoUsecaseTest(TestCase):
    def test_delete_video(self):
        video_repository = InMemoryVideoRepository({
            1: Video(1, 'the title of the video', 'The url of the video'),
        })
        playlist_video_repository = InMemoryPlaylistVideoRepository({})

        DeleteVideoUsecase(video_repository, playlist_video_repository).execute(1)

        self.assertEqual({}, video_repository.storage)

    def test_delete_video_used_in_a_playlist(self):
        video_repository = InMemoryVideoRepository({
            1: Video(1, 'the title of the video', 'The url of the video'),
        })
        playlist_video_repository = InMemoryPlaylistVideoRepository({10: [1], 50: [1,2]})

        DeleteVideoUsecase(video_repository, playlist_video_repository).execute(1)

        self.assertEqual({}, video_repository.storage)
        self.assertEqual({10: [], 50: [2]}, playlist_video_repository.storage)


class GetVideosUsecaseTest(TestCase):

    def test_create_video(self):
        expected_result = {
            'data': [{
                'id': 1,
                'title': 'the title of the video',
                'thumbnail': 'The url of the video',
            },{
                'id': 2,
                'title': 'another title',
                'thumbnail': 'another url',
            }]
        }

        video_repository = InMemoryVideoRepository({
            1: Video(1, 'the title of the video', 'The url of the video'),
            2: Video(2, 'another title', 'another url')
        })

        self.assertEqual(expected_result, GetVideosUsecase(video_repository).get())
