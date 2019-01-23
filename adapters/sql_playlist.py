from core.adapters import MissingPlaylist
from core.models import Playlist


class SqlPlaylistRepository:

    def __init__(self, connection):
        self.connection = connection

    def insert(self, playlist):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO PLAYLIST(NAME) VALUES(?)", (playlist.name,))
        self.connection.commit()

    def get_all(self):
        result = []
        cursor = self.connection.cursor()
        for row in cursor.execute("SELECT ID, NAME FROM PLAYLIST"):
            result.append(Playlist(*row))
        return result

    def get(self, playlist_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT ID, NAME FROM PLAYLIST WHERE ID=?", (playlist_id,))
        row = cursor.fetchone()
        if not row:
            raise MissingPlaylist()
        return Playlist(*row)

    def delete(self, playlist_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM PLAYLIST WHERE ID=?", (playlist_id,))
        self.connection.commit()

    def update(self, playlist):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE PLAYLIST set name=? WHERE ID=?", (playlist.name, playlist.id))
        self.connection.commit()
