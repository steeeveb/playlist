class LazyConnection:
    def __init__(self, connect):
        self._connect = connect
        self._connection = None

    def get(self):
        if not self._connection:
            self._connection = self._connect()
        return self._connection
