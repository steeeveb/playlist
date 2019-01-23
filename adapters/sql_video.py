from core.models import Video, MissingVideo


class SqlVideoRepository:

    def __init__(self, connection):
        self.connection = connection

    def insert(self, video):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO VIDEO(TITLE, THUMBNAIL) VALUES(?,?)", (video.title, video.thumbnail))
        self.connection.commit()

    def get_all(self, *video_ids):
        result = []
        cursor = self.connection.cursor()
        if video_ids:
            sql = "SELECT ID, TITLE, THUMBNAIL FROM VIDEO WHERE ID in (%s)" % ','.join('?' for _ in video_ids)
            for row in cursor.execute(sql, video_ids):
                result.append(Video(*row))
        else:
            for row in cursor.execute("SELECT ID, TITLE, THUMBNAIL FROM VIDEO"):
                result.append(Video(*row))
        return result

    def get(self, video_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT ID, TITLE, THUMBNAIL FROM VIDEO WHERE ID=?", (video_id,))
        row = cursor.fetchone()
        if not row:
            raise MissingVideo()
        return Video(*row)

    def delete(self, video_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM VIDEO WHERE ID=?", (video_id,))
        self.connection.commit()

    def build_schema(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS VIDEO(ID INTEGER PRIMARY KEY AUTOINCREMENT, TITLE TEXT, THUMBNAIL TEXT)")
        self.connection.commit()
