def is_leap_year(year):
    if (year % 4) != 0:
        return False
    elif (year % 100) == 0:
        return (year % 400) == 0
    else:
        return True


def get_month_to_day_dict(year):
    feb_days = 28 if not is_leap_year(year) else 29
    month_to_days = {
        1: 31, 2: feb_days, 3: 31,
        4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30,
        10: 31, 11: 30, 12: 31
    }

    return month_to_days
