import sqlite3


def initialize_db():
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, pin TEXT,
                balance INTEGER DEFAULT 0);""")
    conn.commit()
    conn.close()


def get_count():
    try:
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()

        count = cur.rowcount
        cur.close()
        return count

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


def load_from_db(number, pin):
    try:
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()

        sql = "SELECT * FROM card WHERE number = ? AND pin = ?"
        cursor = cur.execute(sql, (str(number), str(pin),)).fetchone()
        if cursor:
            return cursor

        cur.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


def insert_card(data):
    try:
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()

        sql = """INSERT INTO card
                              (id, number, pin, balance) 
                               VALUES 
                              (?, ?, ?, ?)"""

        cur.execute(sql, data).fetchone()
        conn.commit()

        cur.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


def update_balance(balance, card_number):
    try:
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()

        sql = """UPDATE card 
                SET balance = balance + ? 
                WHERE number = ?"""
        data = (balance, card_number)
        cur.execute(sql, data).fetchone()
        conn.commit()

        cur.close()

    except sqlite3.Error as error:
        print("Failed to update record into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


def delete_card(card_number):
    try:
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()

        sql = """DELETE 
                FROM card 
                WHERE number = ?"""
        cur.execute(sql, (card_number,))
        conn.commit()

        cur.close()

    except sqlite3.Error as error:
        print("Failed to delete record from a sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")


def is_existing_card(number):
    try:
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()

        sql = """SELECT * 
                FROM card 
                WHERE number = ?"""
        cursor = cur.execute(sql, (number,)).fetchone()
        if cursor:
            return True

        cur.close()

    except sqlite3.Error as error:
        print("Failed to find record from a sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")



