
duration = 400153
if duration > 0 and duration < 60:
    print(duration, "сек")
elif duration > 0 and duration < 3600:
    min = duration // 60
    sec = duration % 60
    print(min, "мин", sec, "сек")
elif duration > 0 and duration < 86400:
    hour = duration // 3600
    min = (duration % 3600) // 60
    sec = duration % 60
    print(hour, "час", min, "мин", sec, "сек")
elif duration >= 86400:
    day = duration // 86400
    hour = (duration % 86400) //3600
    min = (duration % 3600) // 60
    sec = duration % 60
    print(day, "дн", hour, "часы", min, "мин", sec, "сек")

