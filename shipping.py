import sqlite3
conn = sqlite3.connect('shipping.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS shipments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    destination TEXT NOT NULL,
                    weight REAL NOT NULL,
                    shipping_cost REAL NOT NULL
                  )''')

conn.commit()
conn.close()


def calculate_shipping_cost(destination, weight):
    rate_per_kg = 5.0
    return weight * rate_per_kg


def save_shipping_details(destination, weight, shipping_cost):
    # Save the shipping details in the database
    conn = sqlite3.connect('shipping.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO shipments (destination, weight, shipping_cost) VALUES (?, ?, ?)',
                   (destination, weight, shipping_cost))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    destination = 'New York'
    weight = 2.5

    shipping_cost = calculate_shipping_cost(destination, weight)
    print(f'Shipping cost to {destination} for {weight} kg package: {shipping_cost}')

    save_shipping_details(destination, weight, shipping_cost)
    print('Shipping details saved to the database.')
OUTPUT:
Shipping cost to New York for 2.5 kg package: 12.5
Shipping details saved to the database.
