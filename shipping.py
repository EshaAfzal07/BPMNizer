import json
import random
import sqlite3

def create_database():
    db = sqlite3.connect("shipping_details.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS shipping_records (id INTEGER PRIMARY KEY, destination TEXT, weight REAL, shipping_cost REAL)")
    db.commit()
    return db

def calculate_shipping_cost(destination, weight):
    rate_per_kg = 5.0
    return weight * rate_per_kg

def save_shipping_details(destination, weight, shipping_cost, shipping_data):
    shipping_id = random.randint(1, 1000)
    shipping_data["id"] = shipping_id

    conn = sqlite3.connect('shipping_details.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO shipping_records (id, destination, weight, shipping_cost) VALUES (?, ?, ?, ?)',
                   (shipping_id, shipping_data["destination"], shipping_data["weight"], shipping_cost))
    conn.commit()
    conn.close()
    return shipping_id

def main(destination, weight):
    shipping_cost = calculate_shipping_cost(destination, weight)
    shipping_data = {"destination": destination, "weight": weight}
    shipping_id = save_shipping_details(destination, weight, shipping_cost, shipping_data)
    print(f"Shipping details saved. ID: {shipping_id}")

if __name__ == '__main__':
    destination = "New York"
    weight = 2.5
    main(destination, weight)



