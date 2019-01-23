from core.models import Playlist


class SqlPlaylistRepository:

    def __init__(self, connection):
        self.connection = connection

    def insert(self, playlist):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO PLAYLIST(NAME) VALUES(?)", (playlist.name,))

    def get_all(self):
        cursor = self.connection.cursor()
        result = []
        for row in cursor.execute("SELECT ID, NAME FROM PLAYLIST"):
            result.append(Playlist(*row))
        return result

    def delete(self, playlist_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM PLAYLIST WHERE ID=?", (playlist_id,))
