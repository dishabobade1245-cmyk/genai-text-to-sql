DATABASE_SCHEMA = """
Database: text_to_sql_db

Tables:

customers
- customer_id: integer, primary key
- customer_name: varchar
- email: varchar
- city: varchar
- state: varchar

products
- product_id: integer, primary key
- product_name: varchar
- category: varchar
- price: decimal

orders
- order_id: integer, primary key
- customer_id: integer, foreign key referencing customers.customer_id
- order_date: date
- status: varchar

order_items
- order_item_id: integer, primary key
- order_id: integer, foreign key referencing orders.order_id
- product_id: integer, foreign key referencing products.product_id
- quantity: integer
- unit_price: decimal
"""