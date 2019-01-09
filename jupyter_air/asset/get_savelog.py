"""
# get_savelog()
#"""
print(__doc__)
# NOW_DATE
# datetime.datetime.now() # ... datetime.datetime(2019, 1, 7, 18, 21, 13, 734730)

import datetime


def get_savelog():
    """
    return 2
    SAVE_LOG  = '20190107_Mon_1800'
    SAVE_LOG1 = '20190107_1800_Mon'
    """
    NOW_DATE = datetime.datetime.strftime(
        datetime.datetime.now(),
        '%Y%m%d_%a_%H00',
    )                               # '20190107_Mon_1800'

    YEAR = NOW_DATE[:4]
    MONTH = NOW_DATE[4:6]
    DAY = NOW_DATE[6:8]
    WEEK = NOW_DATE[9:12]
    HOUR = NOW_DATE[-4:-2]

    SAVE_LOG = f"{YEAR}{MONTH}{DAY}_{WEEK}_{HOUR}00"  # '20190107_Mon_1800'
    SAVE_LOG1 = f"{YEAR}{MONTH}{DAY}_{HOUR}00_{WEEK}"  # '20190107_1800_Mon'
    return (SAVE_LOG, SAVE_LOG1)


if __name__ == '__main__':
    print(get_savelog())
    pass
