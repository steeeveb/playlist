import os
import sqlite3
from unittest import TestCase

from adapters.sql_playlist import SqlPlaylistRepository
from adapters.sql_playlist_video import SqlPlaylistVideoRepository
from adapters.sql_video import SqlVideoRepository
from tests.core.adapters.playlist import PlaylistRepositoryContractTest
from tests.core.adapters.playlist_video import PlaylistVideoRepositoryContractTest
from tests.core.adapters.video import VideoRepositoryContractTest


class SqlPlaylistRepositoryContractTest(TestCase, PlaylistRepositoryContractTest):

    def setUp(self):
        connection = sqlite3.connect('test.db')
        self.repo = SqlPlaylistRepository(connection)
        self.repo.build_schema()

    def tearDown(self):
        os.remove('test.db')


class SqlVideoRepositoryContractTest(TestCase, VideoRepositoryContractTest):

    def setUp(self):
        connection = sqlite3.connect('test.db')
        self.repo = SqlVideoRepository(connection)
        self.repo.build_schema()

    def tearDown(self):
        os.remove('test.db')


class SqlPlaylistVideoRepositoryContractTest(TestCase, PlaylistVideoRepositoryContractTest):
    def setUp(self):
        connection = sqlite3.connect('test.db')
        self.repo = SqlPlaylistVideoRepository(connection)
        self.repo.build_schema()

    def tearDown(self):
        os.remove('test.db')
