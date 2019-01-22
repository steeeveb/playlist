from unittest import TestCase, skip

from core.adapters import InMemoryPlaylistVideoRepository


class PlaylistVideoRepositoryContractTest:
    repo = None

    def test_get(self):
        self.add_video(1, 10)
        self.add_video(1, 11)
        self.add_video(2, 5)

        result = self.repo.get(1)

        self.assertEqual([10, 11], result)

    def test_delete_video(self):
        self.add_video(1, 10)
        self.add_video(1, 11)

        self.repo.delete_video(1, 10)

        self.assertEqual([11], self.repo.get(1))

    def test_add_video(self):
        self.repo.insert_video(1, 10)

        self.assertEqual([10], self.repo.get(1))

    def add_video(self, playlist_id, video_id):
        raise NotImplementedError


class InMemoryPlaylistVideoRepositoryContractTest(TestCase, PlaylistVideoRepositoryContractTest):
    def setUp(self):
        self.storage = {}
        self.repo = InMemoryPlaylistVideoRepository(self.storage)

    def add_video(self, playlist_id, video_id):
        self.storage.setdefault(playlist_id, []).append(video_id)


@skip('Not implemented')
class MysqlPlaylistVideoRepositoryContractTest(TestCase, PlaylistVideoRepositoryContractTest):
    pass