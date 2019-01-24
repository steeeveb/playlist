from http import HTTPStatus
from http.client import HTTPConnection
from http.server import HTTPServer
from unittest import TestCase
from threading import Thread
import json
import socket

from adapters.http_handler import ServerRequestHandler
from core.models import MissingPlaylist, MissingVideo, ValidationError


class ServerResourcesTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_port = get_free_port()
        start_server(cls.server_port, EchoFakeApplication())

    def test_get_requests(self):
        get_requests = [
            ("/videos", ['get_videos']),
            ("/playlists", ['get_playlists']),
            ("/playlists/10", ['get_playlist', 10]),
            ("/playlists/10/videos", ['get_playlist_videos', 10]),
        ]

        for case in get_requests:
            response = self.request('GET', case[0])
            self.check_response(case[1], response)

    def test_post_requests(self):
        post_requests = [
            ("/videos", 'data', ['add_video', 'data']),
            ("/playlists", 'data', ['add_playlist', 'data']),
            ("/playlists/10/videos", 100, ['add_playlist_video', 10, 100]),
        ]

        for case in post_requests:
            response = self.request('POST', case[0], case[1])
            self.check_response(case[2], response)

    def test_delete_requests(self):
        delete_requests = [
            ("/videos/10", ['delete_video', 10]),
            ("/playlists/20", ['delete_playlist', 20]),
            ("/playlists/10/videos/100", ['delete_playlist_video', 10, 100]),
        ]

        for case in delete_requests:
            response = self.request('DELETE', case[0])
            self.check_response(case[1], response)

    def test_put_requests(self):
        put_requests = [
            ("/playlists/10", 'data', ['change_playlist', 10, 'data']),
        ]

        for case in put_requests:
            response = self.request('PUT', case[0], case[1])
            self.check_response(case[2], response)

    def check_response(self, expected, response, status=HTTPStatus.OK):
        self.assertEqual('application/json; charset=utf-8', response.headers['Content-Type'])
        self.assertEqual(status, response.status)
        self.assertEqual(expected, json.load(response))

    def request(self, method, url, data=None):
        connection = HTTPConnection("localhost", port=self.server_port)
        if data:
            connection.request(method, url, json.dumps(data))
        else:
            connection.request(method, url)
        return connection.getresponse()


class HttpErrorsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_port = get_free_port()
        start_server(cls.server_port, ErrorFakeApplication())

    def test_missing_playlist(self):
        connection = HTTPConnection("localhost", port=self.server_port)
        connection.request('DELETE', '/playlists/10')
        response = connection.getresponse()
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status)
        self.assertEqual(b'<html><body><h1>Missing playlist</h1></body></html>', response.read())

    def test_missing_video(self):
        connection = HTTPConnection("localhost", port=self.server_port)
        connection.request('DELETE', '/videos/10')
        response = connection.getresponse()
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status)
        self.assertEqual(b'<html><body><h1>Missing video</h1></body></html>', response.read())

    def test_validation_error(self):
        connection = HTTPConnection("localhost", port=self.server_port)
        connection.request('POST', '/videos')
        response = connection.getresponse()
        self.assertEqual(HTTPStatus.BAD_REQUEST, response.status)
        self.assertEqual(b'<html><body><h1>Validation error</h1></body></html>', response.read())

    def test_wrong_url(self):
        connection = HTTPConnection("localhost", port=self.server_port)
        connection.request('GET', '/wrongurl')
        response = connection.getresponse()
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status)
        self.assertEqual(b'<html><body><h1>Resource not found</h1></body></html>', response.read())


class EchoFakeApplication:
    def __getattr__(self, item):
        return lambda *args: (item,) + args


class ErrorFakeApplication:
    def delete_playlist(self, playlist_id):
        raise MissingPlaylist()
    def delete_video(self, video_id):
        raise MissingVideo()
    def add_video(self, video_id):
        raise ValidationError()


def get_free_port():
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    address, port = s.getsockname()
    s.close()
    return port


def start_server(port, app):
    server = HTTPServer(('localhost', port), ServerRequestHandler)
    server.app = app
    server_thread = Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
