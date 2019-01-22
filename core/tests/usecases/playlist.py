from unittest import TestCase

from core.models import Playlist
from core.adapters import InMemoryPlaylistRepository
from core.usecases.playlist import AddPlaylistUsecase, DeletePlaylistUsecase, GetPlaylistsUsecase, UpdatePlaylistUsecase


class AddPlaylistUsecaseTest(TestCase):
    def test_create_playlist(self):
        a_playlist = {
            'name': 'the name of the playlist'
        }
        playlist_repository = InMemoryPlaylistRepository({})

        AddPlaylistUsecase(playlist_repository).execute(a_playlist)

        self.assertEqual({1: Playlist(1, 'the name of the playlist')}, playlist_repository.storage)


class UpdatePlaylistUsecaseTest(TestCase):
    def test_update_playlist(self):
        a_playlist = {
            'name': 'the new name of the playlist'
        }

        playlist_repository = InMemoryPlaylistRepository({1: Playlist(1, 'the name of the playlist')})

        UpdatePlaylistUsecase(playlist_repository).update(1, a_playlist)

        self.assertEqual(playlist_repository.storage, {1: Playlist(1, 'the new name of the playlist')})


class DeletePlaylistUsecaseTest(TestCase):
    def test_delete_playlist(self):
        ID_TO_DELETE = 1
        playlist_repository = InMemoryPlaylistRepository({
            ID_TO_DELETE: Playlist(ID_TO_DELETE, 'the name of the playlist')
        })

        DeletePlaylistUsecase(playlist_repository).execute(ID_TO_DELETE)

        self.assertEqual({}, playlist_repository.storage)


class GetPlaylistsUsecaseTest(TestCase):
    def test_get_playlists(self):
        expected_result = {
            'data': [{
                'id': 1,
                'name': 'the name of the playlist'
            },{
                'id': 2,
                'name': 'another name'
            }]
        }

        playlist_repository = InMemoryPlaylistRepository({
            1: Playlist(1, 'the name of the playlist'),
            2: Playlist(2, 'another name'),
        })

        self.assertEqual(expected_result, GetPlaylistsUsecase(playlist_repository).get_all())

    def test_get_playlist(self):
        PLAYLIST_ID = 1
        expected_result = {
            'data': {
                'id': PLAYLIST_ID,
                'name': 'the name of the playlist'
            }
        }

        playlist_repository = InMemoryPlaylistRepository({PLAYLIST_ID: Playlist(PLAYLIST_ID, 'the name of the playlist')})

        result = GetPlaylistsUsecase(playlist_repository).get(PLAYLIST_ID)

        self.assertEqual(expected_result, result)
