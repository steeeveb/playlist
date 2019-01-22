from unittest import TestCase

from core.adapters import InMemoryPlaylistRepository
from core.models import Playlist


class PlaylistRepositoryContractTest:
    repo = None

    def test_get_a_playlist(self):
        self.repo.insert(Playlist(1, 'the name of the playlist'))
        self.assertEqual(Playlist(1, 'the name of the playlist'), self.repo.get(1))

    def test_get_all_the_playlists(self):
        self.repo.insert(Playlist(1, 'the name of the playlist'))
        self.repo.insert(Playlist(2, 'the name of another playlist'))
        self.assertEqual([Playlist(1, 'the name of the playlist'), Playlist(2, 'the name of another playlist')],
                         self.repo.get_all())

    def test_delete(self):
        self.repo.insert(Playlist(1, 'the name of the playlist'))
        self.repo.delete(1)
        self.assertEqual([], self.repo.get_all())

    def test_create(self):
        self.repo.insert(Playlist(None, 'the name of the playlist'))
        self.assertEqual([Playlist(1, 'the name of the playlist')], self.repo.get_all())

    def test_update(self):
        self.repo.insert(Playlist(1, 'the name of the playlist'))
        self.repo.update(Playlist(1, 'the new name of the playlist'))
        self.assertEqual([Playlist(1, 'the new name of the playlist')], self.repo.get_all())


class InMemoryPlaylistRepositoryContractTest(TestCase, PlaylistRepositoryContractTest):

    def setUp(self):
        self.storage = {}
        self.repo = InMemoryPlaylistRepository(self.storage)
