from time import localtime


# Converts time from this format: 1672661813.1783261
# To this format: Jan 02 12:47
def convert_time(seconds):
    if seconds == '':
        return ''
    if localtime(seconds).tm_mon == 1:
        month = 'Jan'
    elif localtime(seconds).tm_mon == 2:
        month = 'Feb'
    elif localtime(seconds).tm_mon == 3:
        month = 'Mar'
    elif localtime(seconds).tm_mon == 4:
        month = 'Apr'
    elif localtime(seconds).tm_mon == 5:
        month = 'May'
    elif localtime(seconds).tm_mon == 6:
        month = 'Jun'
    elif localtime(seconds).tm_mon == 7:
        month = 'Jul'
    elif localtime(seconds).tm_mon == 8:
        month = 'Aug'
    elif localtime(seconds).tm_mon == 9:
        month = 'Sep'
    elif localtime(seconds).tm_mon == 10:
        month = 'Oct'
    elif localtime(seconds).tm_mon == 11:
        month = 'Nov'
    elif localtime(seconds).tm_mon == 12:
        month = 'Dec'

    day = localtime(seconds).tm_mday
    hour = localtime(seconds).tm_hour
    minutes = localtime(seconds).tm_min

    return (f'{month} '
            f"{'0'*(2-len(str(day)))}{day} "
            f"{'0'*(2-len(str(hour)))}{hour}:"
            f"{'0'*(2-len(str(minutes)))}{minutes}")