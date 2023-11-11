from datetime import datetime, timedelta

busy = [
    {'start': '10:30',
     'stop': '10:50'},

    {'start': '14:40',
     'stop': '15:50'},

    {'start': '16:40',
     'stop': '17:20'},
    {'start': '18:40',
     'stop': '18:50'},
    {'start': '20:05',
     'stop': '20:20'}
]

returned_list = []

counter = 0
busy_time = False

start_time = datetime(1, 1, 1, 9, 0)  # Начало с 9:00
end_time = datetime(1, 1, 1, 21, 0)  # Конец в 21:00

current_time = start_time

while current_time <= end_time:
    try:
        busy_start_time = datetime.strptime(busy[counter]['start'], '%H:%M').time()
        current_time_time = current_time.time()

        busy_minutes = busy_start_time.hour * 60 + busy_start_time.minute
        current_minutes = current_time_time.hour * 60 + current_time_time.minute

        time_difference = abs(current_minutes - busy_minutes)

        if time_difference >= 30:
            returned_list.append(current_time.strftime("%H:%M"))
            current_time += timedelta(minutes=30)

        elif time_difference == 0:
            returned_list.append(busy[counter]['start'])
            hours, minutes = map(int, busy[counter]['stop'].split(':'))
            current_time = current_time.replace(hour=hours, minute=minutes)
            counter += 1

        else:
            returned_list.append(current_time.strftime("%H:%M"))
            hours, minutes = map(int, busy[counter]['stop'].split(':'))
            current_time = current_time.replace(hour=hours, minute=minutes)
            counter += 1

    except IndexError:
        current_time += timedelta(minutes=30)
        returned_list.append(busy[-1]['stop'])
        returned_list.append((datetime.strptime(busy[-1]['stop'], "%H:%M") + timedelta(minutes=30)).strftime('%H:%M'))

        break

print(returned_list)
