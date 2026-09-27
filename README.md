# QueryMind AI — GenAI Text-to-SQL

QueryMind AI is a GenAI-powered Text-to-SQL application that allows users to query a PostgreSQL database using natural language.

Instead of writing SQL manually, users can ask questions such as:

> Show me all completed orders

The application uses Gemini to convert the natural-language question into a PostgreSQL SELECT query, validates the generated SQL for safety, executes it against PostgreSQL, and displays the results through a Streamlit dashboard.

---

## Features

- Natural-language database querying
- Gemini-powered SQL generation
- PostgreSQL database integration
- SQL safety validation
- Read-only SELECT query enforcement
- Query clarification for ambiguous questions
- FastAPI backend
- Streamlit interactive dashboard
- Structured query results
- Error handling for Gemini API failures and rate limits

---

## System Workflow

```text
User
  |
  v
Streamlit Dashboard
  |
  v
FastAPI Backend
  |
  v
Clarification Engine
  |
  v
Gemini
  |
  v
Generated SQL
  |
  v
SQL Validator
  |
  v
PostgreSQL
  |
  v
Query Results
  |
  v
Streamlit Dashboard