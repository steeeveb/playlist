from http.server import HTTPServer

from adapters.http_handler import ServerRequestHandler
from core.adapters import InMemoryPlaylistRepository, InMemoryPlaylistVideoRepository, InMemoryVideoRepository
from core.application import Application

if __name__ == '__main__':

    server = HTTPServer(('0.0.0.0', 8000), ServerRequestHandler)
    server.app = Application(InMemoryPlaylistRepository({}),
                             InMemoryPlaylistVideoRepository({}),
                             InMemoryVideoRepository({}))
    server.serve_forever()
