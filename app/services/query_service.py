from app.services.clarification import check_clarity
from app.services.gemini_service import generate_sql
from app.services.sql_executor import execute_sql


def process_question(question: str) -> dict:

    print("A. Checking clarification...")

    clarification = check_clarity(question)

    print("B. Clarification result:", clarification)

    if not clarification["clear"]:
        return {
            "status": "clarification_required",
            "message": clarification["message"]
        }

    print("C. Sending question to Gemini...")

    try:
        sql = generate_sql(question)

    except RuntimeError as error:
        print("Gemini error:", error)

        return {
            "status": "error",
            "message": str(error)
        }

    print("D. Gemini returned SQL:", sql)

    print("E. Executing SQL...")

    try:
        result = execute_sql(sql)

    except Exception as error:
        print("SQL execution error:", error)

        return {
            "status": "error",
            "message": f"Database error: {error}"
        }

    print("F. SQL execution completed.")

    return {
        "status": "success",
        "question": question,
        "sql": sql,
        "result": result
    }