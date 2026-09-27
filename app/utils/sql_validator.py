import re


FORBIDDEN_KEYWORDS = {
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "GRANT",
    "REVOKE",
}


def validate_sql(query: str) -> bool:
    query = query.strip()

    if not query:
        return False

    if not re.match(r"^SELECT\b", query, re.IGNORECASE):
        return False

    query_without_strings = re.sub(
        r"'(?:''|[^'])*'",
        "",
        query
    )

    words = re.findall(
        r"\b[A-Z]+\b",
        query_without_strings.upper()
    )

    for word in words:
        if word in FORBIDDEN_KEYWORDS:
            return False

    return True