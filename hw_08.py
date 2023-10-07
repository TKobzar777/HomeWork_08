from datetime import date, timedelta
from collections import defaultdict

def get_period(start_day:date, days:int ):
    result ={}
    for _ in range(days+1):
        result[start_day.day, start_day.month]=start_day.year
        start_day += timedelta(1)
    return result



def get_birthdays_per_week(users:list)-> list:
    result = defaultdict(list)
    #start_day = date.today()
    start_day = date.today()
    if not start_day.weekday():
        list_period = get_period(start_day-timedelta(2),7)
    else:
        list_period = get_period(start_day,7)
    
    for us in users:
        bd:date = us['birthday']
        
        if (bd.day, bd.month) in list(list_period):
            new_year_bd = bd.replace(year=list_period[bd.day, bd.month]) #date(list_period[(bd.day,bd.month)],bd.month,bd.day)
            wd = new_year_bd.weekday() # new_year_bd.strftime('%A')
            
            if wd in (5, 6):
                result["Monday"].append(us["name"])
            else:
                result[new_year_bd.strftime("%A")].append(us["name"])

            
    
    return result
    


if __name__ == "__main__":
    users = [{'name': 'Bill', 'birthday': date(1990, 10, 12)},
             {'name': 'Mike', 'birthday': date(1970, 10, 7)},
             {'name': 'Mariia', 'birthday': date(2000, 10, 7)},
             {'name': 'Vicki', 'birthday': date(1999, 10, 9)},
             {'name': 'Bob', 'birthday': date(1990, 10, 6)},
             {'name': 'Dikki', 'birthday': date(1970, 10, 8)},
             {'name': 'Mia', 'birthday': date(2000, 10, 12)},
             {'name': 'Vlad', 'birthday': date(1999, 10, 11)}
             ]
    for key, value in get_birthdays_per_week(users).items():
        print(f'{key}: {" ".join(value)}')
    


    
