import yearinfo

_REFERENCE_DATE = (1, 1, 1968)
_REFERENCE_DATE_WEEKDAY = 0


def calculate_weekday(day, month, year):
    """
    Calculates the weekday (0 to 6) corresponding to the given date
    :param day: The day of the month
    :param month: The month
    :param year: The year
    :return: The day of the week as an integer from 0 to 6
    """
    return _days_since_reference_date(day, month, year) % 7


def _days_since_reference_date(day, month, year):
    """
    Calculates the number of days since the reference date
    :param day: Day of the month
    :param month: Month of the year
    :param year: Year
    :return: The number of dates since the reference date. May be negative.
    """
    ref_year = _REFERENCE_DATE[2]

    if year >= ref_year:
        return (year - ref_year) * 365 \
               + _leap_years_in_range(ref_year, year - 1) \
               + _days_since_first_january(day, month, year)
    else:
        return (year - ref_year) * 365 \
           - _leap_years_in_range(year + 1, ref_year) \
           + _days_since_first_january(day, month, year)


def _days_since_first_january(day, month, year):
    """
    Calculates the number of days since the 1st of January for a given date
    :param day: Day of the month
    :param month: Month of the year
    :param year: Year
    :return: The number of days since the 1st of January
    """
    month_to_days = yearinfo.get_month_to_day_dict(year)

    day_count = 0
    for month in range(1, month):
        day_count += month_to_days[month]

    return day_count + day - 1


def _leap_years_in_range(first_year, second_year):
    """
    Calculates the number of leap years in the given range of years
    :param first_year: Start of the year range
    :param second_year: End of the year range
    :return: Number of leap years in the given range
    """
    lowest_year, highest_year = sorted([first_year, second_year])
    count = 0
    for year in range(lowest_year, highest_year):
        count += int(yearinfo.is_leap_year(year))

    return count
