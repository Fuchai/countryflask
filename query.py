import psycopg2
import os
import sqlite3

if __name__=="asdfasd":
    conn=psycopg2.connect("postgresql://huya01:@localhost:2345/world")
    curs=conn.cursor()
    curs.execute("select continent from country limit 10")
    res=curs.fetchall()
    print(res)

if __name__=="__main2__":
    conn = psycopg2.connect("postgresql://huya01:@localhost:2345/world")
    curs = conn.cursor()
    curs.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS --WHERE TABLE_NAME = N'country'")
    res = curs.fetchall()
    print(res)

def get_continents_old():
    conn=psycopg2.connect("postgresql://huya01:@localhost:2345/world")
    curs=conn.cursor()
    curs.execute("select DISTINCT continent from country")
    res=curs.fetchall()
    print(res)
    country_list=[(i[0],i[0]) for i in res]
    return country_list

def get_continents():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    dbpath=os.path.join(BASE_DIR,"localdb/country.db")
    conn=sqlite3.connect(dbpath)
    curs=conn.cursor()
    curs.execute("select DISTINCT continent from country")
    res=curs.fetchall()
    print(res)
    country_list=[(i[0],i[0]) for i in res]
    return country_list

if __name__=="__main__":
    get_continents()