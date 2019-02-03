import os
from unittest import TestCase, skipUnless

from adapters.lazy_connection import LazyConnection
from adapters.sql_playlist import SqlPlaylistRepository
from adapters.sql_playlist_video import SqlPlaylistVideoRepository
from adapters.sql_video import SqlVideoRepository
from tests.core.adapters.playlist import PlaylistRepositoryContractTest
from tests.core.adapters.playlist_video import PlaylistVideoRepositoryContractTest
from tests.core.adapters.video import VideoRepositoryContractTest

import mysql.connector


MYSQL = int(os.getenv('MYSQLTESTS', 0))


@skipUnless(MYSQL, 'mysql')
class SqlPlaylistRepositoryContractTest(TestCase, PlaylistRepositoryContractTest):

    def setUp(self):
        connection = setupConnection()
        self.repo = SqlPlaylistRepository(connection)
        cursor = connection.get().cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS PLAYLIST(ID INTEGER PRIMARY KEY AUTO_INCREMENT, NAME TEXT);")
        cursor.execute("TRUNCATE PLAYLIST;")


@skipUnless(MYSQL, 'mysql')
class SqlVideoRepositoryContractTest(TestCase, VideoRepositoryContractTest):

    def setUp(self):
        connection = setupConnection()
        self.repo = SqlVideoRepository(connection)
        cursor = connection.get().cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS VIDEO(ID INTEGER PRIMARY KEY AUTO_INCREMENT, TITLE TEXT, THUMBNAIL TEXT);")
        cursor.execute("TRUNCATE VIDEO;")


@skipUnless(MYSQL, 'mysql')
class SqlPlaylistVideoRepositoryContractTest(TestCase, PlaylistVideoRepositoryContractTest):
    def setUp(self):
        connection = setupConnection()
        self.repo = SqlPlaylistVideoRepository(connection)
        cursor = connection.get().cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS PLAYLIST_VIDEO (ID INTEGER PRIMARY KEY AUTO_INCREMENT, PLAYLIST_ID INTEGER, VIDEO_ID INTEGER);")
        cursor.execute("TRUNCATE PLAYLIST_VIDEO;")


def setupConnection():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'port': '32000',
        'database': 'playlist'
    }

    def connect():
        return mysql.connector.connect(**config)

    return LazyConnection(connect)
