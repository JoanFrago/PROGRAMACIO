def format_duration(segons):
    year = segons // (86400 * 365)
    segons -= year*(86400 * 365)
    day = segons // 86400
    segons -= day * 86400
    hours = segons // 3600
    segons -= hours * 3600
    minutes = segons // 60
    segons -= minutes * 60
    
    if year > 1:
        print(year, 'years', end=', ')
    elif year == 1:
        print('1 year', end=', ')
    if day > 1:
        print(day, 'days', end=', ')
    elif day == 1:
        print('1 day', end=', ')
    if hours > 1:
        print(hours, 'hours', end=', ')
    elif hours == 1:
        print('1 hour', end=', ')
    if minutes > 1:
        print(minutes, 'minute', end=' and ')
    elif minutes == 1:
        print('1 minute', end=' and ')
    if segons > 1:
        print(segons, 'seconds')
    elif segons == 1:
        print('1 second')
    
format_duration(int(input("Escriu aquí: ")))