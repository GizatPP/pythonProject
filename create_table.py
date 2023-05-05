#!/usr/bin/python
import psycopg2
from config import config
import csv

def upload_data_from_csv(filename):
    with open(filename, 'r') as f:
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        reader = csv.reader(f, delimiter=";")
        next(reader)
        for row in reader:
            columns, name, phone = row
            cur.execute(
                "INSERT INTO phoneBook (id, name, phone) VALUES (%s, %s, %s)",
                (columns, name, phone)
            )
        conn.commit()
        print("Data uploaded successfully from", filename)

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE user_score (
            id SERIAL PRIMARY KEY,
            name_score bigint NOT NULL
        )
        """

        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
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

    upload_data_from_csv('DATA.csv')