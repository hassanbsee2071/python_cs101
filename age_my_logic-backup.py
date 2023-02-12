import calendar

MONTHS_OF_YEAR = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTHS_OF_LEAPYEAR = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(n):


    return calendar.isleap(n)

def year_to_days(birth_year,current_year):
    days=0
    i=birth_year+1
    while i < current_year:
        print ("Year is:", i)
        if is_leap(i):
            days = days + 366
            print ("Leap year")
        else:
            days = days + 365
            print ("Non Leap Year")
        i=i+1
    return days

  


def excluded_current_year_day(current_year,current_month,current_day):

     ##2 2 1996
     i=current_day+1
     if is_leap(current_year):
        print ("I am in leap year")
        days = 366
        while i <= MONTHS_OF_LEAPYEAR[current_month-1]:
            
            days = days - 1
            i=i+1
     else:
        days = 365
        print ("I am in non leap year")
        print ("Value of i is:", i)
        print (MONTHS_OF_YEAR[current_month-1])
        print ("Days are:", days)
        
        while i <= MONTHS_OF_YEAR[current_month-1]:
        
            days = days - 1
            print ("Value of inside:", i, days)
            i=i+1
            
     return days

def excluded_current_year_month(current_year,current_month,current_day, excluded_day):
    days = excluded_day
    i=current_month+1
    j=current_month
    if is_leap(current_year):
     
        while i <= len(MONTHS_OF_LEAPYEAR): #MONTHS_OF_LEAPYEAR[current_month]:
            print ("Now days are: leap", j, days, MONTHS_OF_LEAPYEAR[j],i)
            days = days - MONTHS_OF_LEAPYEAR[j]
            i=i+1
            j=j+1  
    else:
      
        while i <= len(MONTHS_OF_YEAR): #MONTHS_OF_LEAPYEAR[current_month]:

            print ("Now days are: non leap", j, days, MONTHS_OF_YEAR[j],i)
            days = days - MONTHS_OF_YEAR[j]
            i=i+1
            j=j+1   
    return days
    
def excluded_birth_year_day(birth_year,birth_month,birth_day):

     ##2 2 1996
     #i=birth_day-1
     i=1
     if is_leap(birth_year):
        print ("I am in leap year")
        days = 366
        while i < birth_day:
            
            days = days - 1
            i=i+1
     else:
        days = 365
        print ("I am in non leap year")
        while i < birth_day:
            days = days - 1
            i=i+1
            
     return days
def excluded_birth_year_month(birth_year,birth_month,birth_day, excluded_birth_day):

    days = excluded_birth_day
    i=1

    if is_leap(birth_year):
        print ("I am birth leap")
        while i < birth_month: 
            days = days - MONTHS_OF_LEAPYEAR[i-1]
            i=i+1 
    else:
        print ("I am birth non leap")
        while i < birth_month:
             days = days - MONTHS_OF_YEAR[i-1]
             i=i+1
        
    return days


inputs=(2018,2,16,2023,2,11) #(year month day)
birth_year=inputs[0]
birth_month=inputs[1]
birth_day=inputs[2]
current_year=inputs[3]
current_month=inputs[4]
current_day=inputs[5]

year_days=year_to_days(birth_year,current_year)
print (year_days)
excluded_current_day=excluded_current_year_day(current_year,current_month,current_day)
print (excluded_current_day)
excluded_current_month=excluded_current_year_month(current_year,current_month,current_day, excluded_current_day)
print (excluded_current_month)

excluded_birth_day=excluded_birth_year_day(birth_year,birth_month,birth_day)
print (excluded_birth_day)
excluded_birth_month=excluded_birth_year_month(birth_year,birth_month,birth_day, excluded_birth_day)
print(excluded_birth_month)

print ("Age in days is:", year_days+excluded_current_month+excluded_birth_month)