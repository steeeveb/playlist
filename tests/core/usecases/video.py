from unittest import TestCase

from core.adapters import InMemoryVideoRepository, InMemoryPlaylistVideoRepository
from core.usecases.video import VideosUsecases
from core.models import Video, ValidationError


class AddVideoUsecaseTest(TestCase):
    def test_create_video(self):
        a_video = {
            'title': 'the title of the video',
            'thumbnail': 'The url of the video',
        }
        video_repository = InMemoryVideoRepository({})
        VideosUsecases(video_repository, None).add(a_video)

        self.assertEqual({1: Video(1, 'the title of the video', 'The url of the video')},
                         video_repository.storage)

    def test_bad_data(self):
        with self.assertRaises(ValidationError):
            an_empty_video = {}
            VideosUsecases(None, None).add(an_empty_video)
        with self.assertRaises(ValidationError):
            a_null_video = None
            VideosUsecases(None, None).add(a_null_video)


class DeleteVideoUsecaseTest(TestCase):
    def test_delete_video(self):
        video_repository = InMemoryVideoRepository({
            1: Video(1, 'the title of the video', 'The url of the video'),
        })
        playlist_video_repository = InMemoryPlaylistVideoRepository({})

        VideosUsecases(video_repository, playlist_video_repository).delete(1)

        self.assertEqual({}, video_repository.storage)

    def test_delete_video_used_in_a_playlist(self):
        video_repository = InMemoryVideoRepository({
            1: Video(1, 'the title of the video', 'The url of the video'),
        })
        playlist_video_repository = InMemoryPlaylistVideoRepository({10: [1], 50: [1,2]})

        VideosUsecases(video_repository, playlist_video_repository).delete(1)

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

        self.assertEqual(expected_result, VideosUsecases(video_repository, None).get())
