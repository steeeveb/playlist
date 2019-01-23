class SqlPlaylistVideoRepository:

    def __init__(self, connection):
        self.connection = connection

    def insert_video(self, playlist_id, video_id):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO PLAYLIST_VIDEO(PLAYLIST_ID, VIDEO_ID) VALUES(?,?)", (playlist_id, video_id))
        self.connection.commit()

    def get(self, playlist_id):
        cursor = self.connection.cursor()
        result = []
        for row in cursor.execute("SELECT VIDEO_ID FROM PLAYLIST_VIDEO WHERE PLAYLIST_ID=?", (playlist_id,)):
            result.append(*row)
        return result

    def delete(self, playlist_id, video_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM PLAYLIST_VIDEO WHERE PLAYLIST_ID=? AND VIDEO_ID=?", (playlist_id, video_id))
        self.connection.commit()

    def delete_playlist(self, playlist_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM PLAYLIST_VIDEO WHERE PLAYLIST_ID=?", (playlist_id,))
        self.connection.commit()

    def delete_video(self, video_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM PLAYLIST_VIDEO WHERE VIDEO_ID=?", (video_id,))
        self.connection.commit()
