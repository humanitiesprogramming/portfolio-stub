# Time traveller looking at different datesself.
# Before 1900
# Present 1900-2020
# Future 2021 +

def greeting_old():
    print("1 Welcome visitor from the past. You have arrived in the city of Philadelphia. You have arrived in the year 2018. You will notice many changes.")
    print("")
def greeting_now():
    print("2 Welcome vistor to the city of Brotherly Love. We recommend using Lyft if you're travleling to the beer festival.")
    print("")
def greeting_future():
    print("3 Welcome visitor of the future. Philadelphia in the year 2018 is a city of 3 million in a transitional phase between carbon-based transportation and electric. Look out for the cars and buses. ")
    print("")

vistor_names = ['Edgar','Ken' ,'Sherdoofl']
visitor_dates = [1880,2017,2120]

counter = 0
# while counter <= len(visitor_dates):
while counter < 3:
    if (visitor_dates[counter] < 1900):
        greeting_old()
    elif ((visitor_dates[counter] > 1900) and (visitor_dates[counter] < 2019)):
        greeting_now()
    else:
        greeting_future()
    counter = counter + 1
