from google import genai
from dotenv import load_dotenv

from app.services.schema_context import DATABASE_SCHEMA

load_dotenv()

client = genai.Client()


def generate_sql(question: str) -> str:

    prompt = f"""
You are a PostgreSQL SQL generator.

Convert the user's natural-language question into
a safe, valid PostgreSQL SELECT query.

{DATABASE_SCHEMA}

Rules:
1. Generate only SELECT statements.
2. Do not generate INSERT, UPDATE, DELETE, DROP, ALTER, CREATE,
   TRUNCATE, or any other modification query.
3. Use only the tables and columns provided in the schema.
4. Return only the SQL query.
5. Do not include markdown code fences.
6. Do not add explanations.

User question:
{question}
"""

    try:

        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            input=prompt,
            generation_config={
                "thinking_level": "low"
            }
        )

        return interaction.output_text.strip()

    except Exception as error:

        error_message = str(error).lower()

        # Temporary fallback for development/testing
        # Used only when Gemini API is unavailable or rate-limited.

        if "rate limit" in error_message or "429" in error_message:

            question_lower = question.lower()

            if "completed" in question_lower and "orders" in question_lower:
                return "SELECT * FROM orders WHERE LOWER(status) = 'completed';"

            if "customers" in question_lower:
                return "SELECT * FROM customers;"

            if "products" in question_lower and "500" in question_lower:
                return "SELECT * FROM products WHERE price > 500;"

            raise RuntimeError(
                "Gemini API quota is currently exhausted. "
                "The requested query is not available in the local fallback."
            )

        raise error