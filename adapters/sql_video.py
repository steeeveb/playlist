from core.models import Video, MissingVideo


class SqlVideoRepository:

    def __init__(self, connection, placeholder='%s'):
        self.lazy_connection = connection
        self.ph = {'ph': placeholder}

    def insert(self, video):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO VIDEO(TITLE, THUMBNAIL) VALUES(%(ph)s,%(ph)s)" % self.ph, (video.title, video.thumbnail))
        self.connection.commit()

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT ID, TITLE, THUMBNAIL FROM VIDEO")
        return [Video(*row) for row in cursor.fetchall()]

    def get_some(self, *video_ids):
        if not video_ids:
            return []
        sql = "SELECT ID, TITLE, THUMBNAIL FROM VIDEO WHERE ID in (%s)" % ','.join(self.ph['ph'] for _ in video_ids)
        cursor = self.connection.cursor()
        cursor.execute(sql, video_ids)
        return [Video(*row) for row in cursor.fetchall()]

    def get(self, video_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT ID, TITLE, THUMBNAIL FROM VIDEO WHERE ID=%(ph)s" % self.ph, (video_id,))
        row = cursor.fetchone()
        if not row:
            raise MissingVideo()
        return Video(*row)

    def delete(self, video_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM VIDEO WHERE ID=%(ph)s" % self.ph, (video_id,))
        self.connection.commit()

    @property
    def connection(self):
        return self.lazy_connection.get()
