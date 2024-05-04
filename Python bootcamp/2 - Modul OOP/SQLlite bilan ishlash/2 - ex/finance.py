import sqlite3
import sys

def main():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS finance
                 (type text, amount integer)''')

    if sys.argv[1] == "earn":
        amount = int(sys.argv[2])
        c.execute("INSERT INTO finance VALUES (?,?)", ('earn', amount))

    elif sys.argv[1] == "spend":
        amount = int(sys.argv[2])
        c.execute("INSERT INTO finance VALUES (?,?)", ('spend', amount))

    elif sys.argv[1] == "balance":
        c.execute("SELECT * FROM finance")
        rows = c.fetchall()
        balance = 0
        for row in rows:
            if row[0] == 'earn':
                balance += row[1]
            elif row[0] == 'spend':
                balance -= row[1]
        print(balance)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
