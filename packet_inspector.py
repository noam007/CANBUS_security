import datetime
import sqlite3
import statistics

import Access_Control_List


def canid_timing(results):
    can_message_list = []
    FORMAT = '%Y-%m-%d %H:%M:%S.%f'
    diff_all = []

    for index in results:
        can_message = list(index)    # change Tuple number to list
        can_message_time = datetime.datetime.strptime(str(can_message[0]), FORMAT)
        can_message_list.append(can_message_time)
        print(can_message_time)

    for i in range(1, len(can_message_list)):
        diff = can_message_list[i] - can_message_list[i-1]
        print(diff)


    # TODO:
    # Example data
    # Calculate variance and standard deviation







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
        print(results,'\n')
        print(type(results))
      #  canid_timing(results)

        # TODO: add a DPI value for each can_ID message - and specific value per DPI



if __name__ == "__main__":
     conn = sqlite3.connect('my_database.db')
     Access_Control_List.allowed_can_ids(conn)
     acl = Access_Control_List.allowed_can_ids(conn)
  #    deep_packet_analyzer(conn, acl)

     results = [ ('22:20:15:82',  'Rx', '0', '0000028A', 's', 8, '0A'),
                ('22:20:15:182', 'Rx', '0', '0000028A', 's', 8, '0A')
               ]

     canid_timing(results)




"""

from datetime import datetime

# 1. הנתונים שלך
time_a_str = "22:20:15:82"
time_b_str = "22:20:15:182"

# 2. הגדרת הפורמט שפייתון מצפה לו לאחר הניקוי
# אנחנו יודעים שנצטרך להגיע ל: HH:MM:SS.ffffff
FINAL_FORMAT = '%H:%M:%S.%f'


def clean_time(time_raw: str) -> str:
    """מתקן את הבעיות בקלט: מחליף ':' אחרון ב'.' וממלא אפסים."""

    # פיצול ל-4 חלקים (שעות, דקות, שניות, חלקיקי שנייה)
    parts = time_raw.split(':')

    # 1. ניקוי המפריד: מחליף את הנקודתיים האחרונות בנקודה
    time_without_micros = f"{parts[0]}:{parts[1]}:{parts[2]}"
    micro_part = parts[3]

    # 2. מילוי אפסים: '%f' דורש 6 ספרות (מיקרו-שניות)
    # 82 הופך ל-820000, ו-182 הופך ל-182000
    padded_micro = micro_part.ljust(6, '0')

    # הרכבת המחרוזת מחדש
    return f"{time_without_micros}.{padded_micro}"


# --- ביצוע החישוב ---

# 3. ניקוי והמרת הנתונים לאובייקטי datetime
# פייתון יניח תאריך בסיס (1900-01-01) כי לא סיפקת תאריך
cleaned_time_a = clean_time(time_a_str)
cleaned_time_b = clean_time(time_b_str)

time_a = datetime.strptime(cleaned_time_a, FINAL_FORMAT)
time_b = datetime.strptime(cleaned_time_b, FINAL_FORMAT)

# 4. מציאת ההבדל (ההפרש)
# נחסיר את הקטן מהגדול כדי לקבל תוצאה חיובית
if time_a > time_b:
    difference = time_a - time_b
else:
    difference = time_b - time_a

# --- הצגת התוצאה ---
print(f"הזמן המנוקה הראשון (לצורך בדיקה): {time_a}")
print(f"הזמן המנוקה השני (לצורך בדיקה): {time_b}")
print("-" * 35)
print(f"ההפרש המוחלט (Timedelta) הוא: {difference}")
print(f"כלומר, ההבדל הוא: {difference.total_seconds():.4f} שניות")

"""