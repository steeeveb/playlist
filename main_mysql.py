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
    import mysql.connector
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'playlist'
    }

    def connect():
        return mysql.connector.connect(**config)

    print('Starting...')
    connection = LazyConnection(connect)
    server = ForkingHTTPServer(('0.0.0.0', 8000), ServerRequestHandler)
    playlist_repository = SqlPlaylistRepository(connection)
    playlist_video_repository = SqlPlaylistVideoRepository(connection)
    video_repository = SqlVideoRepository(connection)
    server.app = Application(playlist_repository, playlist_video_repository, video_repository)
    server.serve_forever()
