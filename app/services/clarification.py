AMBIGUOUS_KEYWORDS = {
    "sales",
    "performance",
    "customers",
    "orders",
    "revenue",
    "products"
}


def check_clarity(question: str) -> dict:
    question = question.strip().lower()

    if not question:
        return {
            "clear": False,
            "message": "Please enter a question."
        }

    found_keywords = [
        keyword
        for keyword in AMBIGUOUS_KEYWORDS
        if keyword in question
    ]

    if len(found_keywords) == 1 and question in found_keywords:
        return {
            "clear": False,
            "message": f"What would you like to know about {found_keywords[0]}?"
        }

    return {
        "clear": True,
        "message": None
    }