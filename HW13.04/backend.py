"""
Creator: Aleksandra Krylova
"""

import sqlite3

conn = sqlite3.connect('KRYLOVASASHA.db')
cur = conn.cursor()


def create_table(text, area):
    """This function create table"""
    cur.execute("CREATE TABLE IF NOT EXISTS " + text.replace(" ", "") + area.replace(" ", "")
                + "(speciality text, company text, skills text,"
                "  compensation text, publicationdate text, href text)")
    conn.commit()


def delete_table(text, area):
    """This function delete data base"""
    cur.execute('DELETE FROM ' + text.replace(" ", "") + area.replace(" ", ""))
    conn.commit()
    cur.close()
    conn.close()


def add_line(text, speciality, company, skills, compensation, publicationdate, href, area):
    """Function to add a single row to the database"""
    cur.execute("INSERT INTO "+ text.replace(" ", "") + area.replace(" ", "")
                + " VALUES(?,?,?,?,?,?)", (speciality, company, skills, compensation, publicationdate, href))
    conn.commit()


def selector(text, area):
    """The function to read all the data in the database"""
    cur.execute("SELECT * FROM " + text.replace(" ", "") + area.replace(" ", ""))
    for i in cur.fetchall():
        print(i)


def names_table(text, area):
    """The function that keeps name of tables in database"""
    cur.execute("CREATE TABLE IF NOT EXISTS  nametable(text text, area text)")
    cur.execute("INSERT INTO nametable VALUES(?, ?)", (text, area))


def selector_nt():
    """The function that returns list of table`s name"""
    n_t = []
    cur.execute("SELECT * FROM nametable")
    for i in cur.fetchall():
        n_t.append(i)
    return n_t


def num(text, area, num):
    """The function that keeps id last vacancy"""
    try:
        cur.execute("SELECT numberlast FROM numberlast" + text.replace(" ", "") + area.replace(" ", ""))
        for i in cur.fetchall():
            lastnum = i[0]
        cur.execute("UPDATE numberlast" + text.replace(" ", "")
                    + area.replace(" ", "") + f" SET numberlast = {num + lastnum}")
        conn.commit()
    except:
        cur.execute("CREATE TABLE IF NOT EXISTS numberlast" + text.replace(" ", "")
                    + area.replace(" ", "") + "(numberlast int)")
        cur.execute("INSERT INTO numberlast"  + text.replace(" ", "") + area.replace(" ", "") + f" VALUES({num})")
        conn.commit()


def selector_href(text, area):
    """The function that returns  href of last vacancy in data base"""
    cur.execute("SELECT numberlast FROM numberlast" + text.replace(" ", "") + area.replace(" ", ""))
    for i in cur.fetchall():
        lastnum = i[0]
    cur.execute("SELECT href FROM " + text.replace(" ", "") + area.replace(" ", "") + f" WHERE id = {lastnum}")
    for i in cur.fetchall():
        return i[0]
