import psycopg2

if __name__=="asdfasd":
    conn=psycopg2.connect("postgresql://huya01:@localhost:2345/world")
    curs=conn.cursor()
    curs.execute("select continent from country limit 10")
    res=curs.fetchall()
    print(res)

if __name__=="__main__":
    conn = psycopg2.connect("postgresql://huya01:@localhost:2345/world")
    curs = conn.cursor()
    curs.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS --WHERE TABLE_NAME = N'country'")
    res = curs.fetchall()
    print(res)

def get_continents():
    conn=psycopg2.connect("postgresql://huya01:@localhost:2345/world")
    curs=conn.cursor()
    curs.execute("select DISTINCT continent from country")
    res=curs.fetchall()
    print(res)
    country_list=[(i[0],i[0]) for i in res]
    return country_list

if __name__=="__main1__":
    get_continents()