import time
from datetime import datetime
from google_drive_manager import get_data_from_google_drive
from db_managar import create_db, is_exist, add_item 
from whatsapp_sender import send_form_to_specialist

# 5 seconds
LOOP_INTERVAL = 5

if __name__ == "__main__":

    while True:
        time.sleep(LOOP_INTERVAL)

        df = get_data_from_google_drive()

        # todo: it is stupid to iterate over the list every time, fixit somehow
        for index, row in df.iterrows():
            # todo - move it to utils.py
            timestamp = datetime.strptime(row['timestamp'], "%d/%m/%Y %H:%M:%S")
            intern = row['intern']
            specialist = row['specialist']

            # todo: create class instead
            create_db()

            if not is_exist(timestamp, intern, specialist):
                print(f"Got new form! Sending message to specialist {specialist}")
                send_form_to_specialist(intern, specialist)
                add_item(timestamp, intern, specialist)
