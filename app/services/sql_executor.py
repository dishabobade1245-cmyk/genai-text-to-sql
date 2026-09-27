from app.database.connection import get_connection
from app.utils.sql_validator import validate_sql


def execute_sql(query: str):
    if not validate_sql(query):
        raise ValueError("Unsafe SQL query rejected.")

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)

            if cursor.description is None:
                return []

            columns = [column.name for column in cursor.description]
            rows = cursor.fetchall()

            return [
                dict(zip(columns, row))
                for row in rows
            ]

    finally:
        connection.close()