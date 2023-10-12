def last_day_of_month(date):
    import datetime as dt
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month+1,day=1) - dt.timedelta(days=1)