# -*- coding: utf-8 -*-
from datetime import datetime, time
import pytz

time_zone = pytz.timezone('Etc/GMT-3')

end_times = {
    '1': time(9, 40),
    '2': time(10, 35),
    '3': time(11, 30),
    '4': time(12, 20),
    '5': time(13, 20),
    '6': time(14, 20),
    '7': time(15, 20),
    '8': time(16, 10),
}


def time_until_end_of_lesson():
    now = datetime.now(time_zone).time()

    for lesson, end_time in end_times.items():
        if now < end_time:
            remaining_time = datetime.combine(datetime.today(), end_time) - datetime.combine(datetime.today(), now)
            minutes, seconds = divmod(remaining_time.total_seconds(), 60)
            return f"До конца урока осталось: {int(minutes)} минут и {int(seconds)} секунд."
    return f'Уроки закончились😎🤙'


print(time_until_end_of_lesson())