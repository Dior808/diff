import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
        )"""

        self.cur.execute(sql)
        self.con.commit()

    # Вставить функцию
    def insert(self, name, age, doj, email, gender, contact, address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)", # вставить в значения сотрудников
                         (name, age, doj, email, gender, contact, address))
        self.con.commit()

    # Получить все данные из БД
    def fetch(self):
        self.cur.execute("SELECT * from employees") # от сотрудников
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Удалить запись в БД
    def remove(self, id):
        self.cur.execute("delete from employees where id=?", (id,)) # удалить из сотрудников, где id
        self.con.commit()

    # Обновить запись в БД
    def update(self, id, name, age, doj, email, gender, contact, address):
        self.cur.execute(
            "update employees set name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? where id=?", # обновить сотрудников
            (name, age, doj, email, gender, contact, address, id))
        self.con.commit()