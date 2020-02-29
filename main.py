import date_parser as parser
import date_calculator as calc
import calendar_printer as printer


def _wait_for_restart(text):
    input(text + '. Press enter to restart the menu')
    print()


def _get_day_of_week(day):
    day_to_string = {
        0: 'Monday', 1: 'Tuesday',
        2: 'Wednesday', 3: 'Thursday',
        4: 'Friday', 5: 'Saturday',
        6: 'Sunday'
    }

    return day_to_string[day]


def _date_to_day_of_week():
    date_string = input('Please input a date (dd.mm.yyyy): ')
    date_tup = parser.date_str_to_tuple(date_string)
    if not date_tup:
        _wait_for_restart('Invalid date')
    else:
        day, month, year = date_tup
        weekday_number = calc.calculate_weekday(day, month, year)
        weekday_string = _get_day_of_week(weekday_number)
        _wait_for_restart(f'The day of the week is {weekday_string}')


def _date_to_month_string():
    date_string = input('Please input a date (mm.yyyy): ')
    date_tup = parser.date_str_to_tuple('01.' + date_string)
    if not date_tup:
        _wait_for_restart('Invalid date')
    else:
        _, month, year = date_tup
        calendar_string = printer.make_calendar_string(month, year)
        print(calendar_string)
        _wait_for_restart(f'This is the calendar for {date_string}')


if __name__ == '__main__':
    print('Welcome to the calendar calculator!')
    while True:
        print('Please choose among the following options')
        print('1) Input a date to get the day of the week')
        print('2) Choose a month of a year to see the full month calendar')
        print('3) Exit')
        option = input('Choose an option number: ')
        if not option.isnumeric() or not (1 <= int(option) <= 2):
            _wait_for_restart('Invalid option')
            continue

        option_nr = int(option)
        if option_nr == 1:
            _date_to_day_of_week()
        elif option_nr == 2:
            _date_to_month_string()
        elif option_nr == 3:
            print('Thanks for using the calendar calculator!')
            break
