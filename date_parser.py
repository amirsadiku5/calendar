import yearinfo


def date_str_to_tuple(date_string: str):
    """
    Calculates a date tuple (day, month, year) from a date string in the format dd.mm.yyyy
    :param date_string: Date string with the form dd.mm.yyyy
    :return: The date tuple with three integers if the parsing was successful, None otherwise
    """
    date_fields = date_string.split('.')
    if len(date_fields) != 3:
        return None

    try:
        day, month, year = (int(field) for field in date_fields)
        if not _is_valid_date(day, month, year):
            return None

        return day, month, year
    except ValueError:
        return None


def _is_valid_date(day, month, year):
    """
    Determines whether a date is valid
    :param day: Day of the date
    :param month: Month of the date
    :param year: Year of the date
    :return: True if the date is valid, False otherwise
    """
    if not 1 <= month <= 12:
        return False

    days_in_month = yearinfo.get_month_to_day_dict(year)
    if not 1 <= day <= days_in_month[month]:
        return False

    return True
