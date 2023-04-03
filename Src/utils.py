import sqlite3


def connect_to_db(path_to_db):
    connection = sqlite3.connect(path_to_db, check_same_thread=False)
    return connection, connection.cursor()


def get_random_row(cursor):
    """Returns random message from db"""
    sql_request = """
    SELECT * FROM
        message_text
    ORDER BY RANDOM()
    LIMIT 1;
    """

    cursor.execute(sql_request)
    return cursor.fetchone()
