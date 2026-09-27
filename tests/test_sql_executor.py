from app.services.sql_executor import execute_sql


# Safe query
result = execute_sql(
    "SELECT customer_id, customer_name FROM customers ORDER BY customer_id;"
)

print("Safe query result:")
print(result)


# Unsafe query
try:
    execute_sql("DELETE FROM customers;")
except ValueError as error:
    print("Unsafe query result:")
    print(error)