from app.services.clarification import check_clarity


questions = [
    "sales",
    "Show me all completed orders",
    "customers",
    ""
]

for question in questions:
    result = check_clarity(question)

    print(f"\nQuestion: {question}")
    print(f"Result: {result}")