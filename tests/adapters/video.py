import os
import sqlite3
from unittest import TestCase

from adapters.sql_video import SqlVideoRepository
from tests.core.adapters.video import VideoRepositoryContractTest


class SqlVideoRepositoryContractTest(TestCase, VideoRepositoryContractTest):

    def setUp(self):
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE VIDEO(ID INTEGER PRIMARY KEY AUTOINCREMENT, TITLE TEXT, THUMBNAIL TEXT)")
        connection.commit()

        self.repo = SqlVideoRepository(connection)

    def tearDown(self):
        os.remove('test.db')

