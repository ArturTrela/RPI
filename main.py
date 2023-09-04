# RPi DataLogger Project start data : 2023/08/28
# WEB PAGE / DB connected to https://rpidatalogger.000webhostapp.com/


# It's a simple script for emulating analog value recive from physical sensor connected to Raspberry Pi.
# In future this script will be change to real-time reader value from any sensor
# Script created for configure and check connection with remote server and try show value in web and desktop app
# After run minimal required function , will be create app for mobile device for administartors and end-users.
# Mobile app  should contain two levels with diferent access rights


import random
import datetime as dt
import csv
import pymysql


min_gen_value = 2200
max_gen_value = 2300
voltage_L1 = 0
curr_L1_min = 0
curr_L1_max = 160
current_L1 = 0
condition = 1
sample_count = 0
sample_time_resolution = 2
timer = dt.datetime.now()
now = timer.strftime("%Y-%m-%d /%H:%M:%S  ")
measureTable = []
act_hours = timer.strftime("%H:%M:%S")
act_date = timer.date()
# save_file_name = 'measureTable/measureValue '+str(dt.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))+'.csv'
save_file_name = 'MeasureValue.csv'
print(now)

while condition:

    delta = dt.datetime.now() - timer
    if delta.seconds >= sample_time_resolution:
        voltage_L1 = random.randint(min_gen_value, max_gen_value)
        last_record = dt.datetime.now()
        last_record = last_record.strftime("%Y-%m-%d godz. %H:%M:%S  ")
        voltage_L1 = voltage_L1 / 10
        current_L1 = random.randint(curr_L1_min, curr_L1_max)
        current_L1 = current_L1 / 10
        timer = dt.datetime.now()
        sample_count += 1
        sample_package = [(sample_count), (last_record) , (voltage_L1), (current_L1)]
        measureTable.append(sample_package)
        print(
            f' [{sample_count}] Data pomiaru : {act_date} godz, {act_hours} wykazał {voltage_L1}V dla L1 a prąd zarejestrowany {current_L1}A')

    def filesaver():
        if sample_count == 10:
            # for i in range(0, sample_count):
            #     print(measureTable[i])
            #     i +=1

            with open(save_file_name, 'w', encoding='UTF8',newline='') as f:
                header = ['No', 'Date&Hour', 'Measure Valve 1 ', 'Measure Value 2']
                data = measureTable
                writer = csv.writer(f)

                # write the header
                writer.writerow(header)

                # write the data
                writer.writerows(data)

    filesaver()
    if sample_count == 2:
        condition = False


def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="malina",
        db='rpi_db',
    )
    ask_query = 'SELECT measure_count , L1_Current , L1_Voltage from last_values '
    cur = conn.cursor()
    # cur.execute(f"select @@version")
    # cur.execute(ask_query)

    # for (measure_count, L1_Current, L1_Voltage ) in cur:
    #      print(f'{measure_count} - {L1_Current}  & {L1_Voltage}')
    #
    insert_query = 'INSERT INTO last_values (measure_count , L1_Current , L1_Voltage)' \
                   ' VAlUES(%(measure_count)s, %(L1_Current)s,%(L1_Voltage)s)'
    insertData = {
         'measure_count': 0,
        'L1_Current': current_L1,
        'L1_Voltage': voltage_L1,
    }
    cur.execute(insert_query, insertData)
    output = cur.fetchall()
    print(output)
    print(act_hours)
    print(act_date)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    mysqlconnect()


