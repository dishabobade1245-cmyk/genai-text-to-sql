from fastapi import FastAPI
from app.services.clarification import check_clarity
from app.services.query_service import process_question
from app.database.connection import get_connection

app = FastAPI(title="GenAI Text-to-SQL API")


@app.get("/")
def root():
    return {"message": "GenAI Text-to-SQL API is running"}


@app.get("/customers")
def get_customers():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT customer_id, customer_name, email, city, state FROM customers"
            )
            rows = cursor.fetchall()

        return [
            {
                "customer_id": row[0],
                "customer_name": row[1],
                "email": row[2],
                "city": row[3],
                "state": row[4],
            }
            for row in rows
        ]

    finally:
        connection.close()


@app.get("/clarify")
def clarify_question(question: str):
    return check_clarity(question)


@app.get("/query")
def query_database(question: str):
    return process_question(question)