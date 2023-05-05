#!/usr/bin/python

import psycopg2
from config import config


def insert_data():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        INSERT INTO users (id, name) VALUES (
        10, 'Gizat')""",
        """
        INSERT INTO user_score (id, name_score) VALUES (
        10, 12)
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
    insert_data()