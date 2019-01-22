from unittest import TestCase

from core.adapters import InMemoryPlaylistRepository, InMemoryVideoRepository, InMemoryPlaylistVideoRepository, \
    MissingPlaylist, MissingVideo
from core.models import Video, Playlist
from core.usecases.playlist_video import AddPlaylistVideoUsecase, DeletePlaylistVideoUsecase, GetPlaylistVideosUsecase


class AddPlaylistVideoUsecaseTest(TestCase):
    def test_add_video_to_playlist(self):
        video_repository = InMemoryVideoRepository({50: Video(50, None, None)})
        playlist_repository = InMemoryPlaylistRepository({100: [Playlist(100, None)]})
        playlist_video_repository = InMemoryPlaylistVideoRepository({})

        usecase = AddPlaylistVideoUsecase(video_repository, playlist_repository, playlist_video_repository)

        usecase.execute(100, 50)

        self.assertEqual({100: [50]}, playlist_video_repository.storage)

    def test_add_missing_video_to_playlist(self):
        video_repository = InMemoryVideoRepository({})
        playlist_repository = InMemoryPlaylistRepository({100: [Playlist(100, None)]})

        usecase = AddPlaylistVideoUsecase(video_repository, playlist_repository, None)

        self.assertRaises(MissingVideo, lambda : usecase.execute(100, 50))

    def test_add_video_to_missing_playlist(self):
        playlist_repository = InMemoryPlaylistRepository({})

        usecase = AddPlaylistVideoUsecase(None, playlist_repository, None)

        self.assertRaises(MissingPlaylist, lambda : usecase.execute(-1, 50))


class DeletePlaylistVideoUsecaseTest(TestCase):
    def test_delete_video_from_playlist(self):
        playlist_repository = InMemoryPlaylistRepository({10: Playlist(10, 'name')})
        playlist_video_repository = InMemoryPlaylistVideoRepository({10: [1, 50]})

        DeletePlaylistVideoUsecase(playlist_repository, playlist_video_repository).execute(10, 50)

        self.assertEqual({10: [1]}, playlist_video_repository.storage)

    def test_delete_video_from_missing_playlist(self):
        playlist_repository = InMemoryPlaylistRepository({})

        usecase = DeletePlaylistVideoUsecase(playlist_repository, None)

        self.assertRaises(MissingPlaylist, lambda : usecase.execute(-1, 50))


class GetPlaylistVideosUsecaseTest(TestCase):
    def test_get_playlists(self):
        expected_result = {
            'data': [{
                'id': 1,
                'title': 'the title of the video',
                'thumbnail': 'a thumbnail'
            },{
                'id': 2,
                'title': 'another title',
                'thumbnail': 'another thumbnail'
            }]
        }

        playlist_repository = InMemoryPlaylistRepository({10: Playlist(10, 'name')})
        video_repository = InMemoryVideoRepository({1: Video(1, 'the title of the video', 'a thumbnail'),
                                                    2: Video(2, 'another title', 'another thumbnail')})
        playlist_video_repository = InMemoryPlaylistVideoRepository({10: [1, 2]})

        usecase = GetPlaylistVideosUsecase(playlist_repository, playlist_video_repository, video_repository)

        self.assertEqual(expected_result, usecase.get_all(10))

    def test_missing_playlist(self):
        playlist_repository = InMemoryPlaylistRepository({10: Playlist(10, 'name')})

        usecase = GetPlaylistVideosUsecase(playlist_repository, None, None)

        self.assertRaises(MissingPlaylist, lambda : usecase.get_all(-1))
