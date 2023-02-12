import calendar

MONTHS_OF_YEAR = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTHS_OF_LEAPYEAR = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(n):


    return calendar.isleap(n)

def year_to_days(birth_year,current_year):
    days=0
    i=birth_year+1
    while i < current_year:
        #print ("Year is:", i)
        if is_leap(i):
            days = days + 366
            #print ("Leap year")
        else:
            days = days + 365
            #print ("Non Leap Year")
        i=i+1
    return days

  


def excluded_current_year_day(current_year,current_month,current_day):

     ##2 2 1996
     #i=current_day+1
     i=current_day
     if is_leap(current_year):
        #print ("I am in leap year")
        days = 366
        while i <= MONTHS_OF_LEAPYEAR[current_month-1]:
            
            days = days - 1
            i=i+1
     else:
        days = 365
        #print ("I am in non leap year")
        #print ("Value of i is:", i)
        #print (MONTHS_OF_YEAR[current_month-1])
        #print ("Days are:", days)
        
        while i <= MONTHS_OF_YEAR[current_month-1]:
        
            days = days - 1
            #print ("Value of inside:", i, days)
            i=i+1
            
     return days

def excluded_current_year_month(current_year,current_month,current_day, excluded_day):
    days = excluded_day
    i=current_month+1
    j=current_month
    if is_leap(current_year):
     
        while i <= len(MONTHS_OF_LEAPYEAR): #MONTHS_OF_LEAPYEAR[current_month]:
            #print ("Now days are: leap", j, days, MONTHS_OF_LEAPYEAR[j],i)
            days = days - MONTHS_OF_LEAPYEAR[j]
            i=i+1
            j=j+1  
    else:
      
        while i <= len(MONTHS_OF_YEAR): #MONTHS_OF_LEAPYEAR[current_month]:

            #print ("Now days are: non leap", j, days, MONTHS_OF_YEAR[j],i)
            days = days - MONTHS_OF_YEAR[j]
            i=i+1
            j=j+1   
    return days
    
def excluded_birth_year_day(birth_year,birth_month,birth_day):

     ##2 2 1996
     #i=birth_day-1
     i=1
     if is_leap(birth_year):
        #print ("I am in leap year")
        days = 366
        while i < birth_day:
            
            days = days - 1
            i=i+1
     else:
        days = 365
        #print ("I am in non leap year")
        while i < birth_day:
            days = days - 1
            i=i+1
            
     return days
def excluded_birth_year_month(birth_year,birth_month,birth_day, excluded_birth_day):

    days = excluded_birth_day
    i=1

    if is_leap(birth_year):
        #print ("I am birth leap")
        while i < birth_month: 
            days = days - MONTHS_OF_LEAPYEAR[i-1]
            i=i+1 
    else:
        #print ("I am birth non leap")
        while i < birth_month:
             days = days - MONTHS_OF_YEAR[i-1]
             i=i+1
        
    return days

def equal_year(birth_day,birth_month,birth_year,current_day,current_month,current_year):

    a=is_leap(birth_year)
    i=1
    if a==True:
        #print ("Leap Year detected")
        days=0
        while birth_month <= current_month:
            days = days + MONTHS_OF_LEAPYEAR[birth_month - 1]
            birth_month = birth_month + 1
        while i < birth_day:
            days = days - 1
            i=i+1
        i = current_day 
        while i <= MONTHS_OF_LEAPYEAR[current_month - 1]:
            days = days - 1
            i = i + 1
        return days
    else:

        days=0
        while birth_month <= current_month:
            days = days + MONTHS_OF_YEAR[birth_month - 1]
            birth_month = birth_month + 1
        while i < birth_day:
            days = days - 1
            i=i+1

        i = current_day 
        while i <= MONTHS_OF_YEAR[current_month - 1]:
            days = days - 1
            i = i + 1
        return days

#inputs=(1996,3,3,1999,5,17) #(year month day)
inputs=(2012,1,1,2012,2,28)        #58
#inputs=(2012,1,1,2012,3,1)      #60
#inputs=(2011,6,30,2012,6,30)    #366
#inputs=(2011,1,1,2012,8,8)      #585
#inputs=(1900,1,1,1999,12,31)    #36523
#inputs=(2013,7,5,2013,8,5)      #31

birth_year=inputs[0]
birth_month=inputs[1]
birth_day=inputs[2]
current_year=inputs[3]
current_month=inputs[4]
current_day=inputs[5]
if birth_year > current_year:
    print ("Wrong Input")
elif birth_year == current_year and birth_month > current_month:
    print ("Wrong Input")
elif birth_year == current_year and birth_month == current_month and birth_day > current_day:
    print ("Wrong Input")
elif current_year == birth_year:
   equals=equal_year(birth_day,birth_month,birth_year,current_day,current_month,current_year)
   print ("Age in days is:", equals)

else:
    year_days=year_to_days(birth_year,current_year)
    excluded_current_day=excluded_current_year_day(current_year,current_month,current_day)
    excluded_current_month=excluded_current_year_month(current_year,current_month,current_day, excluded_current_day)
    excluded_birth_day=excluded_birth_year_day(birth_year,birth_month,birth_day)
    excluded_birth_month=excluded_birth_year_month(birth_year,birth_month,birth_day, excluded_birth_day)
    print ("Age in days is:", year_days+excluded_current_month+excluded_birth_month)