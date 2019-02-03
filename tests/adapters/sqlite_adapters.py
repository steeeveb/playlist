import os
import sqlite3
from unittest import TestCase

from adapters.lazy_connection import LazyConnection
from adapters.sql_playlist import SqlPlaylistRepository
from adapters.sql_playlist_video import SqlPlaylistVideoRepository
from adapters.sql_video import SqlVideoRepository
from tests.core.adapters.playlist import PlaylistRepositoryContractTest
from tests.core.adapters.playlist_video import PlaylistVideoRepositoryContractTest
from tests.core.adapters.video import VideoRepositoryContractTest


class SqlPlaylistRepositoryContractTest(TestCase, PlaylistRepositoryContractTest):

    def setUp(self):
        connection = LazyConnection(lambda: sqlite3.connect('test.db'))
        self.repo = SqlPlaylistRepository(connection, '?')
        cursor = connection.get().cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS PLAYLIST(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT)")

    def tearDown(self):
        os.remove('test.db')


class SqlVideoRepositoryContractTest(TestCase, VideoRepositoryContractTest):

    def setUp(self):
        connection = LazyConnection(lambda: sqlite3.connect('test.db'))
        self.repo = SqlVideoRepository(connection, '?')
        cursor = connection.get().cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS VIDEO(ID INTEGER PRIMARY KEY AUTOINCREMENT, TITLE TEXT, THUMBNAIL TEXT)")

    def tearDown(self):
        os.remove('test.db')


class SqlPlaylistVideoRepositoryContractTest(TestCase, PlaylistVideoRepositoryContractTest):
    def setUp(self):
        connection = LazyConnection(lambda: sqlite3.connect('test.db'))
        self.repo = SqlPlaylistVideoRepository(connection, '?')
        cursor = connection.get().cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS PLAYLIST_VIDEO(ID INTEGER PRIMARY KEY AUTOINCREMENT, PLAYLIST_ID, VIDEO_ID)")

    def tearDown(self):
        os.remove('test.db')
