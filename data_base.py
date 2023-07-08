import sqlite3

class Database:
    def _init_(self, db):
        con=sqlite3.connect(db)
        cur=self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees
             (EId integer primary key,
             name text,
             contact text,
             email text,
             doj text,
             )"""
        self.cur.execute()
        self.con.commit()

    def insert( name, age, doj, email, gender, contact, address):
        self.cur.execute("insert into employees values(NULL,?,?,?,?,?,?)", (eid,name, contact, email,doj))
        self.con.commit()

    def fetch(self):
        self.cur.execute("Select * from employees")
        rows = self.cur.fetchall()
        return rows

    def update(name, contact, email,doj):
        self.cur.execute("update employees set eid=?, name=?,contact=?,email=?,,doj=?,email=?where eid = ?",(name, contact, email,doj))
        self.con.commit()


    def delete(self, id):
        selfcur.execute("delete from employees where eid = ?", (id,))
        self.con.commit()

