class LoggerMixin:
    def log(self, message):
        print(f"[LOG]: {message}")


class TimestampMixin:
    def current_timestamp(self):
        import datetime

        return datetime.datetime.now().isoformat()


class DatabaseConnection(LoggerMixin, TimestampMixin):
    def connect(self):
        self.log(f"Connecting at {self.current_timestamp()}")

    def disconnect(self):
        self.log(f"Disconnecting at {self.current_timestamp()}")


db = DatabaseConnection()
db.connect()
db.disconnect()
