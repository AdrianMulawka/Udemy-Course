# Example of creating function this script count days to New Years Eve
from datetime import date
from datetime import timedelta


def TimeToNewYersEve (year = date.today().year, month = date.today().month, day = date.today().day):
    day = date(year, month, day)
    #day = date()
    currentYear = day.year
    newYearsEve = date(currentYear, 12, 31)
    timeToNewYear = newYearsEve-day

    # print("Until New Year Eve left %s days." % timeToNewYear)
    return TimeToNewYersEve()

TimeToNewYersEve()