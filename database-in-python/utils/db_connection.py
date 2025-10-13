import sqlite3
class DatabaseConnection:
    def __init__(self,host_storage):
        self.connection = None
        self.host_storage = host_storage
    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host_storage,timeout=10)
        return self.connection
    def __exit__(self,exc_type,exc_val,exc_tb) -> None:
        if exc_type or exc_val or exc_tb:
            self.connection.rollback()
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
