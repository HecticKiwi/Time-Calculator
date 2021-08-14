def add_time(start, duration, start_day=None):
    start_time, period = start.split(' ')

    start_hour, start_minute = start_time.split(':')
    duration_hour, duration_minute = duration.split(':')

    new_hour = int(start_hour) + int(duration_hour)
    new_minute = int(start_minute) + int(duration_minute)

    new_hour += new_minute // 60
    new_minute = new_minute % 60

    days_passed = 0
    while new_hour > 12:
        new_hour -= 12

        if period == 'PM':
            period = 'AM'
            days_passed += 1
        else:
            period = 'PM'

    new_time = f'{new_hour}:{new_minute:02d} {period}'

    if start_day != None:
        days_key = {
            'Sunday': 0,
            'Monday': 1,
            'Tuesday': 2,
            'Wednesday': 3,
            'Thurdsay': 4,
            'Friday': 5,
            'Saturday': 6
        }

        new_day = days_key[start_day.capitalize()]
        new_day += days_passed
        new_day = {v: k for k, v in days_key.items()}[new_day % 7]

        new_time = ', '.join([new_time, new_day])

    if days_passed == 1:
        new_time = ' '.join([new_time, '(next day)'])
    elif days_passed > 1:
        new_time = ' '.join([new_time, f'({days_passed} days later)'])

    return new_time

print(add_time("11:55 AM", "3:12"))
print(add_time("11:40 AM", "0:25"))