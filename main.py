import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Existing code to create table and insert data
cursor.execute('DROP TABLE IF EXISTS CAN_Messages')

# <Time>       <Tx/Rx> <Channel>   <CAN ID>  <Type>  <DLC>  <DataBytes>***

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

with open('candump.log', 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            parts = line.split()
            if len(parts) >= 3:
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

conn.commit()

# Your new code goes here, before the connection is closed
cursor.execute("SELECT rowid, time, tx_rx, channel, can_id, type, dlc, data_bytes FROM CAN_Messages where time = '22:20:23:542' ;")

# get all CAN_ID's:
# Execute a query to select all CAN_ID values
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


print(f" can_id_list is {unique_list}")
print(len(unique_list))

results = cursor.fetchall()

print("results with the same time")
for row in results:
    print(row)

# Now, close the connection
conn.close()

# <Time>       <Tx/Rx> <Channel>   <CAN ID>  <Type>  <DLC>  <DataBytes>***
# 22:20:14:992    Rx       0       0000021A     s     8      FE 36 12 FE 69 05 07 AD