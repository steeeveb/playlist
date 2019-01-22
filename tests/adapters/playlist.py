from unittest import skip, TestCase

from adapters.playlist import MysqlPlaylistRepository
from tests.core.adapters.playlist import PlaylistRepositoryContractTest


@skip('NOT IMPLEMENTED')
class MysqlPlaylistRepositoryContractTest(TestCase, PlaylistRepositoryContractTest):

    def setUp(self):
        self.repo = MysqlPlaylistRepository()