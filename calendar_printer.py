import yearinfo
import date_calculator as dc


def make_calendar_string(month, year):
    """
    Creates a string representing the given month formatted in the following format:
      M  T  W  T  F  S  S
      1  2  3  4  5  6  7
      8  9 10 11 12 13 14
     15 16 17 18 19 20 21
     22 23 24 25 26 27 28
     29 30 31
    :param month: Month to get the string of (1 to 12)
    :param year: Year to get the month from
    :return: The stringified version of the given month
    """
    days_string = 'MTWTFSS'
    top_string = ''.join(_format(c) for c in days_string)

    days_in_month = yearinfo.get_month_to_day_dict(year)[month]
    starting_day = dc.calculate_weekday(1, month, year)

    formatted_days = [_format(' ')] * starting_day + [_format(day) for day in range(1, days_in_month + 1)]
    calendar_rows = [top_string] + [''.join(chunk) for chunk in _split_in_chunks(formatted_days, 7)]

    return '\n'.join(calendar_rows)


def _format(element):
    return f'{element:>3}'


def _split_in_chunks(the_list: list, chunk_size: int):
    """
    Transforms a list into a list of lists of a determined max size
    :param the_list: List to split
    :param chunk_size: Max size of the inner lists
    :return: A list of lists with the max size in place
    """
    result = []
    start_idx = 0
    end_idx = chunk_size
    while True:
        chunk = the_list[start_idx:end_idx]
        if len(chunk) > 0:
            result.append(chunk)
            start_idx += chunk_size
            end_idx += chunk_size
        else:
            break

    return result

