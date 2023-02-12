# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

import calendar

def is_leap(n):


    return calendar.isleap(n)


def count_days(year, month, day):
    MONTHS_OF_YEAR = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    MONTHS_OF_LEAPYEAR = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0 
    i = 0
    while i < year:
        if is_leap(i):
            days = days + 366
        else:
            days = days + 365
        i = i + 1
        print("Values of i is:", i, days)


    i = 0
    while i < month - 1 :
        if is_leap(year) and i == 1:
            days = days + MONTHS_OF_LEAPYEAR[i]
            print ("I am in if one")
        else:
            days = days + MONTHS_OF_YEAR[i]
            print ("I am in if else one")
        i = i + 1

    days = days + day
    print ("Values of days and day:", days, day)

    return days


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
  #TODO: Check inputs for impossible values month1 > 12 or days in month
    if year1 > year2:
        return "You're timetravelling"
    elif year1 == year2 and month1 > month2:
        return "You're timetravelling"
    elif year1 == year2 and month1 == month2 and day1 > day2:
        return "You're timetravelling"
    else:
        days1 = count_days(year1, month1, day1)
        days2 = count_days(year2, month2, day2)
        return days2 - days1

result = daysBetweenDates(2012,1,1,2012,2,28)
print ("Age is:", result)
# Test routine

# def test():
#     test_cases = [((2012,1,1,2012,2,28), 58), 
#                   ((2012,1,1,2012,3,1), 60),
#                   ((2011,6,30,2012,6,30), 366),
#                   ((2011,1,1,2012,8,8), 585 ),
#                   ((1900,1,1,1999,12,31), 36523),
#                   ((2013,7,5,2013,8,5), 31)]
#     for (args, answer) in test_cases:
#         result = daysBetweenDates(*args)
#         if result != answer:
#             print "Test with data:", args, "failed"
#         else:
#             print "Test case passed!"

# test()