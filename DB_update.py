import sqlite3

# Create an sqlite3 database passed as conn.
def create_db(conn):
    # DB setup
    # conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Create table and insert data
    cursor.execute('DROP TABLE IF EXISTS CAN_Messages')

    # <Time> <Tx/Rx> <Channel> <CAN ID> <Type> <DLC> <DataBytes>***
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CAN_Messages (
            time TEXT,
            tx_rx TEXT,
            channel TEXT,
            can_id TEXT,
            type TEXT,
            dlc INTEGER,
            data_bytes TEXT
        )
        ''')

    # check SQL was created :
    rows = cursor.fetchall()
    print(f"DB was created with {len(rows)} rows")


def update_db(conn, db_file):
    cursor = conn.cursor()

    with open(db_file, 'r') as CAM_log:
        for line in CAM_log:
            line = line.strip()
            if line:
                parts = line.split()
                if len(parts) >= 7:
                    time = parts[0]
                    tx_rx = parts[1]
                    channel = parts[2]
                    can_id = parts[3]
                    type = parts[4]
                    dlc = parts[5]
                    data_bytes = parts[6]

                    cursor.execute('''
                        INSERT INTO CAN_Messages (time, tx_rx, channel, can_id, type, dlc, data_bytes)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (time, tx_rx, channel, can_id, type, dlc, data_bytes))

    conn.commit()  # commit the data to the DB

    # print first ROW in DB:
    cursor = conn.cursor()
    query = "SELECT * FROM CAN_Messages"
    cursor.execute(query)

    row = cursor.fetchone()  # gets only the first row
    print("First row:", row)

    # print all values in the Date base:
    # print("Data in table:", cursor.fetchall()")  # gets all Values


def DB_quarry(conn):

    cursor = conn.cursor()

    # gets a single line where it's time is '22:20:23:542'
    time = '22:20:23:542'
    cursor.execute(""" SELECT rowid, time, tx_rx, channel, can_id, type, dlc, data_bytes
        FROM CAN_Messages WHERE time = ? """, (time,))
    # get all CAN_ID's:
    cursor.execute("SELECT CAN_ID FROM CAN_Messages")
    # Fetch all the results
    results = cursor.fetchall()
    # Use a list comprehension to flatten the list of tuples into a simple list
    can_id_list = [row[0] for row in results]

    # get unique Id's:
    # Convert the list to a set to get unique elements
    unique_set = set(can_id_list)

    # Convert the set back to a list if needed
    unique_list = list(unique_set)

    print('\n')
    print(f" can_id_list is {unique_list}")
    print(len(unique_list))

    results = cursor.fetchall()

    print("results with the same time")
    for row in results:
        print(row)


    # <Time>       <Tx/Rx> <Channel>   <CAN ID>  <Type>  <DLC>  <DataBytes>***
    # 22:20:14:992    Rx       0       0000021A     s     8      FE 36 12 FE 69 05 07 AD

if __name__ == "__main__":
    conn = sqlite3.connect('my_database.db')

    create_db(conn)
    update_db(conn,'can_dump.log')
    DB_quarry(conn)

    # Now, close the connection
    conn.close()