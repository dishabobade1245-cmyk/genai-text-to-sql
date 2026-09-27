from app.services.query_service import process_question

print("1. Starting test...")

question = "Show me all completed orders"

print("2. Calling process_question...")

result = process_question(question)

print("3. Process completed!")

print("Final result:")
print(result)