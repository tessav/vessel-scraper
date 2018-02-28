from datetime import datetime as dt
from datetime import timedelta

DEFAULT_SELECTION = 'Today'
TODAY = 'Today'
TOMORROW = 'Tomorrow'
PAST_5_DAYS = 'Past 5 Days'


def get_dt_range(selection):
    if selection == TODAY:
        return create_dt_range(dt.now(), 1)
    elif selection == TOMORROW:
        return create_dt_range(dt.now() + timedelta(days=1), 1)
    else:
        return create_dt_range(dt.now() - timedelta(days=5), 5)


def create_dt_range(selected_dt, days_lapsed):
    start_day = selected_dt.date()
    end_day = selected_dt.date() + timedelta(days=days_lapsed)
    return dt(start_day.year, start_day.month, start_day.day), \
        dt(end_day.year, end_day.month, end_day.day)
