from unittest import skip, TestCase

from adapters.playlist_video import MysqlPlaylistVideoRepository
from tests.core.adapters.playlist_video import PlaylistVideoRepositoryContractTest


@skip('Not implemented')
class MysqlPlaylistVideoRepositoryContractTest(TestCase, PlaylistVideoRepositoryContractTest):
    def setUp(self):
        self.repo = MysqlPlaylistVideoRepository()