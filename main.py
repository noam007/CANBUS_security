import sqlite3
import DB_update


if __name__ == '__main__':
    conn = sqlite3.connect('my_database.db')
    DB_update.create_db(conn)  # 👈 Pass conn just like before

    # update db with file can_dump.log
    DB_update.update_db(conn, "can_dump.log")

    DB_update.DB_quarry(conn)

    
    # conn = sqlite3.connect('my_database.db')
    #
    # create_db(conn)
    # update_db(conn, 'candump.log')
    # db_commands(conn)
    #
    # # Now, close the connection
    # conn.close()