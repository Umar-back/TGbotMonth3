CREATE_USER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS telegram_users
        (
        ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        USERNAME CHAR(20),
        FIRST_NAME CHAR(20),
        LAST_NAME CHAR(20),
        UNIQUE (TELEGRAM_ID)
        )
"""

INSERT_USER_NAME = """
INSERT OR IGNORE INTO telegram_users VALUES(?,?,?,?,?)
"""