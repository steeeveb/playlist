import os
import sqlite3
from unittest import skip, TestCase

from adapters.sql_playlist_video import SqlPlaylistVideoRepository
from tests.core.adapters.playlist_video import PlaylistVideoRepositoryContractTest


class SqlPlaylistVideoRepositoryContractTest(TestCase, PlaylistVideoRepositoryContractTest):
    def setUp(self):
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE PLAYLIST_VIDEO(ID INTEGER PRIMARY KEY AUTOINCREMENT, PLAYLIST_ID, VIDEO_ID)")
        connection.commit()

        self.repo = SqlPlaylistVideoRepository(connection)

    def tearDown(self):
        os.remove('test.db')
