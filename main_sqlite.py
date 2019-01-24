import sqlite3
from http.server import HTTPServer
from socketserver import ForkingMixIn

from adapters.http_handler import ServerRequestHandler
from adapters.lazy_connection import LazyConnection
from adapters.sql_playlist import SqlPlaylistRepository
from adapters.sql_playlist_video import SqlPlaylistVideoRepository
from adapters.sql_video import SqlVideoRepository
from core.application import Application


class ForkingHTTPServer(ForkingMixIn, HTTPServer):
    pass


if __name__ == '__main__':
    def connect():
        return sqlite3.connect('playlist.db')
    print('Starting...')
    server = ForkingHTTPServer(('0.0.0.0', 8000), ServerRequestHandler)
    connection = LazyConnection(connect)
    playlist_repository = SqlPlaylistRepository(connection, '?')
    playlist_video_repository = SqlPlaylistVideoRepository(connection, '?')
    video_repository = SqlVideoRepository(connection, '?')

    playlist_repository.build_schema()
    playlist_video_repository.build_schema()
    video_repository.build_schema()

    server.app = Application(playlist_repository, playlist_video_repository, video_repository)
    server.serve_forever()
