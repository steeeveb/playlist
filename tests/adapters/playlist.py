import os
from unittest import TestCase, skip
import sqlite3

from adapters.playlist import SqlPlaylistRepository
from tests.core.adapters.playlist import PlaylistRepositoryContractTest


@skip('NOT IMPLEMENTED')
class SqlPlaylistRepositoryContractTest(TestCase, PlaylistRepositoryContractTest):

    def setUp(self):
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE PLAYLIST(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT)")
        connection.commit()

        self.repo = SqlPlaylistRepository(connection)

    def tearDown(self):
        os.remove('test.db')
