import psycopg2, csv

# Connect to the database
conn = psycopg2.connect(
    host='localhost',
    dbname='Suppliers',
    user='postgres',
    password='910!!vv$88',
)
cur = conn.cursor()


def datausers(data):
    incorrect = []
    for d in data:
        name, phone = d
        if len(phone) != 4 or not phone.isdigit():
            incorrect.append(d)
            continue
        cur.execute("INSERT INTO phone_book (name, phone) VALUES (%s, %s)", (name, phone))
    print(incorrect)
    conn.commit()
    cur.close()


def update(name, number):
    cur.execute("SELECT COUNT(*) FROM phone_book WHERE name = %s", (name,))
    count = cur.fetchone()[0]
    if count == 0:
        cur.execute("INSERT INTO phone_book (name, number) VALUES (%s, %s)", (name, number,))
    else:
        cur.execute("UPDATE phone_book SET number = %s WHERE name = %s", (phone, name,))
    conn.commit()
    cur.close()


while True:
    print(
        "1 - insert csv, 2 - insert console, 3 - update, 4 - search, 5 - delete, 8 - exit")
    n = input("Enter number : ")
    if n == '1':
        filename = 'csvdata.csv'
        with open(filename, 'r') as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                cur.execute("""INSERT INTO phone_book VALUES(%s,%s) returning *;""", row)
            conn.commit()
    elif n == '2':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        cur.execute("INSERT INTO phone_book (name, number) VALUES (%s, %s)", (name, phone))
        conn.commit()
    elif n == '3':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        update(name, phone)
    elif n == '4':
        name = input("Enter name to search: ")
        cur.execute("SELECT * FROM phone_book WHERE name ILIKE %s", (name,))
        rows = cur.fetchall()
        for r in rows:
            print(r)
        conn.commit()
    elif n == '6':
        name = input("delete name:")
        cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
        conn.commit()
    elif n == '8':
        break
    else:
        print("Please try again")

conn.close()