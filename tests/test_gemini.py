from app.services.gemini_service import generate_sql

print("1. Starting Gemini test...", flush=True)

question = "Show me all completed orders"

print("2. Calling generate_sql...", flush=True)

sql = generate_sql(question)

print("3. Gemini returned:", sql, flush=True)