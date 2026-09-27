from app.utils.sql_validator import validate_sql


print("SELECT test:", validate_sql("SELECT * FROM customers;"))
print("DELETE test:", validate_sql("DELETE FROM customers;"))
print("DROP test:", validate_sql("DROP TABLE customers;"))
print("UPDATE test:", validate_sql("UPDATE customers SET city = 'Pune';"))