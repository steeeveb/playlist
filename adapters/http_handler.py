import json
import re
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler

from core.models import MissingPlaylist, MissingVideo


class ServerRequestHandler(BaseHTTPRequestHandler):
    VIDEOS = re.compile(r'^/videos$')
    VIDEO = re.compile(r'^/videos/(\d+)$')
    PLAYLISTS = re.compile(r'^/playlists$')
    PLAYLIST = re.compile(r'^/playlists/(\d+)$')
    PLAYLIST_VIDEOS = re.compile(r'^/playlists/(\d+)/videos$')
    PLAYLIST_VIDEO = re.compile(r'^/playlists/(\d+)/videos/(\d+)$')

    def do_GET(self):
        self._handle(self._get)
    def do_POST(self):
        self._handle(self._post)
    def do_PUT(self):
        self._handle(self._put)
    def do_DELETE(self):
        self._handle(self._delete)

    def _get(self):
        if re.search(self.VIDEOS, self.path):
            self._success(self.app.get_videos())
        elif re.search(self.PLAYLISTS, self.path):
            self._success(self.app.get_playlists())
        elif re.search(self.PLAYLIST, self.path):
            m = re.match(self.PLAYLIST, self.path)
            playlist_id = int(m.groups()[0])
            self._success(self.app.get_playlist(playlist_id))
        elif re.search(self.PLAYLIST_VIDEOS, self.path):
            m = re.match(self.PLAYLIST_VIDEOS, self.path)
            playlist_id = int(m.groups()[0])
            self._success(self.app.get_playlist_videos(playlist_id))
        else:
            self._error('Resource not found', HTTPStatus.NOT_FOUND)

    def _post(self):
        data = self._get_data()
        if re.search(self.VIDEOS, self.path):
            self._success(self.app.add_video(data))
        elif re.search(self.PLAYLISTS, self.path):
            self._success(self.app.add_playlist(data))
        elif re.search(self.PLAYLIST_VIDEOS, self.path):
            m = re.match(self.PLAYLIST_VIDEOS, self.path)
            playlist_id = int(m.groups()[0])
            self._success(self.app.add_playlist_video(playlist_id, data))
        else:
            self._error('Resource not found', HTTPStatus.NOT_FOUND)


    def _put(self):
        if re.search(self.PLAYLIST, self.path):
            m = re.match(self.PLAYLIST, self.path)
            playlist_id = int(m.groups()[0])
            self._success(self.app.change_playlist(playlist_id, self._get_data()))
        else:
            self._error('Resource not found', HTTPStatus.NOT_FOUND)


    def _delete(self):
        if re.search(self.VIDEO, self.path):
            m = re.match(self.VIDEO, self.path)
            video_id = int(m.groups()[0])
            self._success(self.app.delete_video(video_id))
        elif re.search(self.PLAYLIST, self.path):
            m = re.match(self.PLAYLIST, self.path)
            playlist_id = int(m.groups()[0])
            self._success(self.app.delete_playlist(playlist_id))
        elif re.search(self.PLAYLIST_VIDEO, self.path):
            m = re.match(self.PLAYLIST_VIDEO, self.path)
            playlist_id = int(m.groups()[0])
            video_id = int(m.groups()[1])
            self._success(self.app.delete_playlist_video(playlist_id, video_id))
        else:
            self._error('Resource not found', HTTPStatus.NOT_FOUND)


    def _handle(self, action):
        try:
            action()
        except MissingVideo:
            self._error('Missing video', HTTPStatus.NOT_FOUND)
        except MissingPlaylist:
            self._error('Missing playlist', HTTPStatus.NOT_FOUND)
        except Exception:
            self._error('Server Error', HTTPStatus.INTERNAL_SERVER_ERROR)

    def _error(self, msg, status):
        self.send_response(status)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        response_content = '<html><body><h1>' + msg + '</h1></body></html>'
        self.wfile.write(response_content.encode('utf-8'))


    def _get_data(self):
        content_length = int(self.headers['Content-Length'])
        raw_data = self.rfile.read(content_length)
        data = None
        if raw_data:
            data = json.loads(raw_data)
        return data

    def _success(self, response_data=None):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        if response_data != None:
            response_content = json.dumps(response_data)
            self.wfile.write(response_content.encode('utf-8'))

    @property
    def app(self):
        return self.server.app