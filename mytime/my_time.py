from time import time, localtime

def time_now_hms():
    return f'{localtime(time()).tm_hour}:' \
           f'{localtime(time()).tm_min}:' \
           f'{localtime(time()).tm_sec}'
