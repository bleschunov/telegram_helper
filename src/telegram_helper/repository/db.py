from pathlib import Path

import peewee as pw

db = pw.SqliteDatabase(Path.cwd() / "data" / "db.sqlite3")
