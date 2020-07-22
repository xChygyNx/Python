# import banking
import random
import sqlite3


def luhn_generate():
    sum_ = 0
    sequence = [4, 0, 0, 0, 0, 0]
    card_num = ""
    for _ in range(9):
        sequence.append(random.randint(0, 9))
    for digit in sequence:
        card_num += str(digit)
    for i in range(0, len(sequence)):
        if i % 2 == 0:
            sequence[i] *= 2
            if sequence[i] >= 10:
                sequence[i] -= 9
        sum_ += sequence[i]
    card_num += str((10 - sum_ % 10) % 10)
    return card_num


def create_db():
    conn = sqlite3.connect('card.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS card')
    conn.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS card
                    (
                        id INT PRIMARY_KEY,
                        number VARCHAR(16),
                        pin VARCHAR(4),
                        balance INT DEFAULT 0
                    );""")
    conn.commit()
    conn.close()


def create_card():
    pin = ""
    for _ in range(4):
            pin += str(random.randint(0, 9))
    card_num = luhn_generate()
    request = 'INSERT INTO card(number, pin) VALUES(' + card_num + ', ' + pin + ')'
    conn = sqlite3.connect('card.s3db')
    cursor = conn.cursor()
    cursor.execute(request)
    conn.commit()
    conn.close()
    print("Your card has been created")
    print("Your card number:")
    print(card_num)
    print("Your card PIN:")
    print(pin)

