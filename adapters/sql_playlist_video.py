class SqlPlaylistVideoRepository:

    def __init__(self, connection, placeholder='%s'):
        self.lazy_connection = connection
        self.ph = {'ph': placeholder}

    def insert_video(self, playlist_id, video_id):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO PLAYLIST_VIDEO(PLAYLIST_ID, VIDEO_ID) VALUES(%(ph)s,%(ph)s)" % self.ph, (playlist_id, video_id))
        self.connection.commit()

    def get(self, playlist_id):
        cursor = self.connection.cursor()
        result = []
        cursor.execute("SELECT VIDEO_ID FROM PLAYLIST_VIDEO WHERE PLAYLIST_ID=%(ph)s" % self.ph, (playlist_id,))
        for row in cursor.fetchall():
            result.append(*row)
        return result

    def delete(self, playlist_id, video_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM PLAYLIST_VIDEO WHERE PLAYLIST_ID=%(ph)s AND VIDEO_ID=%(ph)s" % self.ph, (playlist_id, video_id))
        self.connection.commit()

    def delete_playlist(self, playlist_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM PLAYLIST_VIDEO WHERE PLAYLIST_ID=%(ph)s" % self.ph, (playlist_id,))
        self.connection.commit()

    def delete_video(self, video_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM PLAYLIST_VIDEO WHERE VIDEO_ID=%(ph)s" % self.ph, (video_id,))
        self.connection.commit()

    @property
    def connection(self):
        return self.lazy_connection.get()