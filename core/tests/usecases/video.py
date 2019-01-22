from unittest import TestCase

from core.adapters import InMemoryVideoRepository
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

        DeleteVideoUsecase(video_repository).execute(1)

        self.assertEqual({}, video_repository.storage)

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
