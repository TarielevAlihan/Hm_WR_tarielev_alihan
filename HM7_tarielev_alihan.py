import sqlite3


def create_db():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT NOT NULL CHECK(length(product_title) <= 200),
            price REAL DEFAULT 0.0 CHECK(price >= 0),
            quantity INTEGER DEFAULT 0 CHECK(quantity >= 0)
        )
    ''')
    conn.commit()
    conn.close()


def add_products():
    products = [
        ('Шариковая ручка', 10.50, 100),
        ('Ноутбук', 15000.75, 5),
        ('Мыло', 25.99, 50),

    ]
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)
    conn.commit()
    conn.close()


def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))
    conn.commit()
    conn.close()


def update_price(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    conn.commit()
    conn.close()


def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()


def select_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)


def select_filtered_products(limit_price=100, limit_quantity=5):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE price < ? AND quantity > ?', (limit_price, limit_quantity))
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)


def search_products_by_title(title):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%'+title+'%',))
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)


if __name__ == '__main__':
    create_db()
    add_products()
    update_quantity(1, 200)
    update_price(2, 15500.99)
    delete_product(3)
    select_all_products()
    select_filtered_products()
    search_products_by_title('мыло')


