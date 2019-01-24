from unittest import TestCase

from core.adapters import InMemoryPlaylistVideoRepository


class PlaylistVideoRepositoryContractTest:
    repo = None

    def test_get(self):
        self.repo.insert_video(1, 10)
        self.repo.insert_video(1, 11)
        self.repo.insert_video(2, 5)

        self.assertEqual([10, 11], self.repo.get(1))
        self.assertEqual([5], self.repo.get(2))
        self.assertEqual([], self.repo.get(-1))

    def test_delete(self):
        self.repo.insert_video(1, 10)
        self.repo.insert_video(1, 11)

        self.repo.delete(1, 10)

        self.assertEqual([11], self.repo.get(1))

    def test_delete_playlist(self):
        self.repo.insert_video(1, 10)
        self.repo.insert_video(1, 11)

        self.repo.delete_playlist(1)

        self.assertEqual([], self.repo.get(1))

    def test_delete_video(self):
        self.repo.insert_video(1, 10)
        self.repo.insert_video(2, 10)

        self.repo.delete_video(10)

        self.assertEqual([], self.repo.get(1))
        self.assertEqual([], self.repo.get(2))

    def test_add(self):
        self.repo.insert_video(1, 10)

        self.assertEqual([10], self.repo.get(1))


class InMemoryPlaylistVideoRepositoryContractTest(TestCase, PlaylistVideoRepositoryContractTest):
    def setUp(self):
        self.storage = {}
        self.repo = InMemoryPlaylistVideoRepository(self.storage)


