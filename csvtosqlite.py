import sqlite3
import ast
import os
import traceback

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def gettype(string):
    try:
        tt=type(ast.literal_eval(string))
        if tt is int:
            return "int"
        if tt is float:
            return "float"
        if tt is bool:
            return "bool"
        raise NotImplementedError("Unhandled type")
    except (ValueError, SyntaxError):
        return "text"

def execute_insert(conn,tblname,splitted_line):
    insertcommand="INSERT INTO "+tblname+" VALUES ("
    for i in splitted_line:
        insertcommand+='"'+i+'",'
    insertcommand=insertcommand[:-1]
    insertcommand+=")"
    # print(insertcommand)
    try:
        conn.execute(insertcommand)
    except sqlite3.OperationalError:
        print(traceback.format_exc())
        print("oops")

def parse_and_make(csvfile):
    csvpath=os.path.join(BASE_DIR,"localdb",csvfile)
    tblname=csvfile.split(".")[0]
    dbpath=os.path.join(BASE_DIR,"localdb",tblname+".db")
    conn=sqlite3.connect(dbpath)
    c=conn.cursor()

    with open(csvpath, 'r') as db:
        firstline=db.readline().strip()
        field_names=firstline.split("|")
        secondline=db.readline().strip()
        secondline=secondline.split("|")
        thirdline=db.readline().strip()
        thirdline=thirdline.split("|")

        types=[]
        for val in thirdline:
            # print(gettype(val))
            types.append(gettype(val))

        create_table_command="CREATE TABLE IF NOT EXISTS "+tblname+" ("
        for field, type in zip(field_names,types):
            create_table_command+=field+" "+type+", "
        create_table_command=create_table_command[:-2]+")"

        # print(create_table_command)
        c.execute(create_table_command)

        execute_insert(c,tblname,secondline)
        execute_insert(c,tblname,thirdline)
        for line in db:
            redline = line.strip()
            redline = redline.split("|")
            execute_insert(c,tblname,redline)
    conn.commit()
    conn.close()


if __name__=="__main__":
    parse_and_make("country.csv")
    parse_and_make("city.csv")
    parse_and_make("country_language.csv")
    print("All csv files have been parsed and db files have been created.")