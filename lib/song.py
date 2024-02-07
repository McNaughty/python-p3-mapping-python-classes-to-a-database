from config import CONN, CURSOR
# from music import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY,
            name TEXT,
            album TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()  # Add commit after executing DDL statements

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()  # Commit the transaction after insertion
        self.id = CURSOR.lastrowid if CURSOR.lastrowid is not None else -1  # Set id to -1 if lastrowid is None

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song