import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS machine (id INTEGER PRIMARY KEY, "
                         "date TEXT, "
                         "machine_name TEXT,"
                         "tech_name TEXT,"
                         "mach_downtime INTEGER,"
                         "tech_downtime INTEGER,"
                         "machine_status TEXT,"
                         "fault TEXT,"
                         "repair TEXT,"
                         "j_type TEXT,"
                         "j_cat TEXT,"
                         "verification TEXT)")
        self.conn.commit()

    def insert_entry(self, date, machine_name, tech_name, mach_downtime, tech_downtime, machine_status, fault, repair,
                     j_type, j_cat, verification):
        self.cur.execute("INSERT INTO machine VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?)",
                         (date, machine_name, tech_name, mach_downtime, tech_downtime, machine_status, fault, repair,
                          j_type, j_cat, verification))
        self.conn.commit()

    def view_all(self):
        self.cur.execute("SELECT * FROM machine")
        rows = self.cur.fetchall()
        return rows

    def search_entry(self, date="", machine_name="", tech_name="", mach_downtime='', tech_downtime='',
                     machine_status="",
                     fault="", repair="",
                     j_type="", j_cat="", verification=""):
        self.cur.execute("SELECT * FROM machine WHERE date=? OR "
                         "machine_name=? OR "
                         "tech_name=? OR "
                         "mach_downtime = ? OR "
                         "tech_downtime=? OR "
                         "machine_status =? OR "
                         "fault=? OR "
                         "repair=? OR "
                         "j_type=? OR "
                         "j_cat=? OR "
                         "verification=? ", (date, machine_name, tech_name, mach_downtime, tech_downtime, machine_status,
                                             fault, repair,
                                             j_type, j_cat, verification))
        rows = self.cur.fetchall()
        return rows

    def delete_entry(self, id):
        self.cur.execute("DELETE FROM machine WHERE id=?", (id,))
        self.conn.commit()

    def update_entry(self, date,machine_name, tech_name, mach_downtime, tech_downtime, machine_status, fault, repair,
                     j_type, j_cat, verification):
        self.cur.execute("UPDATE machine SET date=?, machine_name=?,"
                         "tech_name=?,  mach_downtime=?, tech_downtime=?, "
                         "machine_status=?,fault=?, repair=?, j_type=?,"
                         " j_cat=?, verification=? WHERE id=?",
                         (date, machine_name, tech_name, mach_downtime, tech_downtime, machine_status, fault, repair,
                          j_type, j_cat, verification))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
