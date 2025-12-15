import csv
import sqlite3

DB_PATH = "instance/restaurants.db"
CSV_PATH = "data/광주광역시_광주맛집.csv"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

with open(CSV_PATH, newline='', encoding='cp949') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        name = row[1]
        address = row[2]
        phone = row[3]
        category = row[4]

        cur.execute("""
            INSERT INTO restaurants (name, address, phone, category)
            VALUES (?, ?, ?, ?)
        """, (name, address, phone, category))

conn.commit()
conn.close()

print("✅ CP949 CSV → DB 저장 완료")
