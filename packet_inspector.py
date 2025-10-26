import sqlite3
import Access_Control_List

def deep_packet_analyzer(conn,acl):

    # Create a cursor object from the connection to execute SQL queries
    cursor = conn.cursor()

    # loop for each can_id:
    for packet in acl:
        query = '''
                SELECT * FROM CAN_Messages 
                WHERE can_id = ?
            '''

        # 2. Execute the query
        # The second argument is a tuple containing the value(s) for the placeholder(s).
        cursor.execute(query, (packet,))

        # 3. Fetch the results
        # Use fetchall() to get a list of all matching rows.
        # Each row is returned as a tuple of values.
        results = cursor.fetchall()
        print(results)

        # TODO: add a DPI value for each can_ID message - and specific value per DPI









if __name__ == "__main__":
     conn = sqlite3.connect('my_database.db')
     Access_Control_List.allowed_can_ids(conn)
     acl = Access_Control_List.allowed_can_ids(conn)
     deep_packet_analyzer(conn, acl)