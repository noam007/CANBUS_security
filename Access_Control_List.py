import sqlite3

def allowed_can_ids(conn):

    # Create a cursor object from the connection to execute SQL queries
    cursor = conn.cursor()

    # get all CAN_ID's:
    cursor.execute("SELECT CAN_ID FROM CAN_Messages")

    # Fetch all the results
    results = cursor.fetchall()

    # Use a list comprehension to flatten the list of tuples into a simple list
    can_id_list = [row[0] for row in results]

    unique_set = set(can_id_list)

    # Convert the set back to a list if needed
    unique_list = list(unique_set)
    # print(unique_list)

    # Create a Table named : 'Allowed_CAN_ID'
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Allowed_CAN_ID (
                can_id TEXT  )
            ''')

    # Update table with values
    for can_id in unique_list:
        cursor.execute('''
            INSERT INTO Allowed_CAN_ID (can_id) 
            VALUES (?)
            ''', (can_id,))

    return unique_list



def print_allowed_can_ids(conn):

    # Create a cursor object from the connection to execute SQL queries
    cursor = conn.cursor()

    # printer the values in the Table
    print(cursor.execute('Select * FROM Allowed_CAN_ID'))
    # Fetch and print all rows from the result
    rows = cursor.fetchall()
    for row in rows:
        print(row)



if __name__ == "__main__":
     conn = sqlite3.connect('my_database.db')
     allowed_can_ids(conn)
     print_allowed_can_ids(conn)