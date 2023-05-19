import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        sql = """ 
        CREATE TABLE IF NOT EXISTS products(
            id Integer Primary Key,
            nam text,
            price text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, nam, price):
        self.cur.execute("insert into products values (NULL,?,?)", (nam, price))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM products")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute("delete from products where id=?", (id,))
        self.con.commit()

    def update(self, id, nam, price):
        self.cur.execute('update products set nam=?,price=? where id=?',
                         (nam, price, id))
        self.con.commit()
