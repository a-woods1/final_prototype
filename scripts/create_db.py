#!/usr/bin/python
#from http://www.postgresqltutorial.com/postgresql-python/create-tables/

import psycopg2

db_name = "prototype_db"
db_user = "bb_admin"
db_host = "localhost"
db_password = "welcome123"


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
                """
                    CREATE TABLE job (
                    job_id SERIAL PRIMARY KEY,
                    job_title VARCHAR(255)
                    )
                """,
                """
                    CREATE TABLE stage (
                    stage_id SERIAL PRIMARY KEY,
                    stage_title VARCHAR(255)
                    )
                """,
                """
                    CREATE TABLE category (
                    category_id SERIAL PRIMARY KEY,
                    category_name VARCHAR(255)
                    )
                """,
                """
                    CREATE TABLE address (
                    address_id SERIAL PRIMARY KEY,
                    street_address VARCHAR(255),
                    postal_code integer,
                    city VARCHAR(100),
                    state VARCHAR(100),
                    country VARCHAR(100)
                    )
                """,
                """
                    CREATE TABLE office (
                    office_id SERIAL PRIMARY KEY,
                    address_id integer REFERENCES address (address_id),
                    office_name VARCHAR(255)
                    )
                """,
                """
                    CREATE TABLE room (
                    room_id SERIAL UNIQUE,
                    office_id integer REFERENCES office (office_id),
                    room_name VARCHAR(100),
                    elevator_accessible BOOLEAN,
                    PRIMARY KEY(room_id, office_id)
                    )
                """,
                """
                    CREATE TABLE product (
                    product_id SERIAL PRIMARY KEY,
                    product_name VARCHAR(255),
                    product_description TEXT,
                    category_id integer REFERENCES category (category_id),
                    pre_approved BOOLEAN
                    )
                """,
                """
                    CREATE TABLE inventory (
                    product_id integer REFERENCES product (product_id),
                    room_id integer REFERENCES room (room_id),
                    quantity integer,
                    PRIMARY KEY(product_id, room_id)
                    )
                """,
                """
                    CREATE TABLE person (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(255),
                    last_name VARCHAR(255),
                    email VARCHAR(255) NOT NULL,
                    phone_number VARCHAR(50),
                    password_hash VARCHAR(500) NOT NULL,
                    address_id integer REFERENCES address (address_id),
                    job_id integer REFERENCES job (job_id),
                    stage_id integer REFERENCES stage (stage_id)
                    )
                """,
                """
                    CREATE TABLE request (
                    request_id SERIAL PRIMARY KEY,
                    product_id integer REFERENCES product (product_id),
                    person_id integer REFERENCES person (id),
                    request_justfication text,
                    request_date date
                    )
                """)
    
    
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect("dbname=" + db_name + " user=" + db_user + " host=" + db_host + " password=" + db_password)
        cur = conn.cursor()
        # create table one by one
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
    create_tables()
