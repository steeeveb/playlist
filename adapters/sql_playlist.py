from core.models import Playlist, MissingPlaylist


class SqlPlaylistRepository:

    def __init__(self, connection, placeholder='%s'):
        self.lazy_connection = connection
        self.ph = {'ph': placeholder}

    def insert(self, playlist):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO PLAYLIST(NAME) VALUES(%(ph)s)" % self.ph, (playlist.name,))
        self.connection.commit()

    def get_all(self):
        result = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT ID, NAME FROM PLAYLIST")
        for row in cursor.fetchall():
            result.append(Playlist(*row))
        return result

    def get(self, playlist_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT ID, NAME FROM PLAYLIST WHERE ID=%(ph)s" % self.ph, (playlist_id,))
        row = cursor.fetchone()
        if not row:
            raise MissingPlaylist()
        return Playlist(*row)

    def delete(self, playlist_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM PLAYLIST WHERE ID=%(ph)s" % self.ph, (playlist_id,))
        self.connection.commit()

    def update(self, playlist):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE PLAYLIST set name=%(ph)s WHERE ID=%(ph)s" % self.ph, (playlist.name, playlist.id))
        self.connection.commit()

    def build_schema(self):
        cursor = self.connection.cursor()
        self.connection.commit()

    @property
    def connection(self):
        return self.lazy_connection.get()