#!/usr/bin/python

import psycopg2

db_name = "prototype_db"
db_user = "bb_admin"
db_host = "localhost"
db_password = "welcome123"

def drop_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
                'DROP TABLE "request";',
                'DROP TABLE "person";',
                'DROP TABLE "inventory";',
                'DROP TABLE "product";',
                'DROP TABLE "room";',
                'DROP TABLE "office";',
                'DROP TABLE "address";',
                'DROP TABLE "category";',
                'DROP TABLE "stage";',
                'DROP TABLE "job";'
                )
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect("dbname=" + db_name + " user=" + db_user + " host=" + db_host + " password=" + db_password)
        cur = conn.cursor()
        # drop tables one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    drop_tables()
