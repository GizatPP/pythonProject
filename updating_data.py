#!/usr/bin/python

import psycopg2
from config import config


def update_data(id, name, phone):
    """ update vendor name based on the vendor id """
    sql = """ UPDATE phonebook
                SET name = %s, phone = %s
                WHERE id = %s"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (name, phone, id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("SUCCESSFULLY!!!")

    return updated_rows


if __name__ == '__main__':
    # insert name and id
    id = input("Enter id :")
    name = input("Enter name :")
    phone = input("Enter telephone number :")
    # Update data id 1
    update_data(id, name, phone)