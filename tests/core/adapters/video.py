from unittest import TestCase

from core.adapters import InMemoryVideoRepository, MissingVideo
from core.models import Video


class VideoRepositoryContractTest:
    repo = None

    def test_get_all(self):
        self.repo.insert(Video(1, 'the name of the playlist', 'thumbnail'))
        self.repo.insert(Video(2, 'the name of another playlist', 'another thumbnail'))
        self.assertEqual([Video(1, 'the name of the playlist', 'thumbnail'),
                          Video(2, 'the name of another playlist', 'another thumbnail')],
                         self.repo.get_all())

    def test_get_some_ids(self):
        self.repo.insert(Video(1, 'name1', 'thumbnail1'))
        self.repo.insert(Video(2, 'name2', 'thumbnail2'))
        self.repo.insert(Video(3, 'name3', 'thumbnail3'))
        self.assertEqual([Video(1, 'name1', 'thumbnail1'),
                          Video(2, 'name2', 'thumbnail2')],
                         self.repo.get_all(1, 2))

    def test_get_a_video(self):
        self.repo.insert(Video(1, 'name1', 'thumbnail1'))
        self.assertEqual(Video(1, 'name1', 'thumbnail1'), self.repo.get(1))

    def test_get_a_missing_video(self):
        with self.assertRaises(MissingVideo):
            self.repo.get(1)

    def test_delete(self):
        self.repo.insert(Video(1, 'the name of the playlist', 'thumbnail'))
        self.repo.delete(1)
        self.assertEqual([], self.repo.get_all())

    def test_create(self):
        self.repo.insert(Video(None, 'the name of the playlist', 'thumbnail'))
        self.assertEqual([Video(1, 'the name of the playlist', 'thumbnail')], self.repo.get_all())


class InMemoryVideoRepositoryContractTest(TestCase, VideoRepositoryContractTest):

    def setUp(self):
        self.storage = {}
        self.repo = InMemoryVideoRepository(self.storage)
