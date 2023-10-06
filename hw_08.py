from datetime import date, timedelta

global dict_weekday 
dict_weekday = {'Monday': '', 'Tuesday': '', 'Wednesday': '', 'Thursday': '', 'Friday':'', 'Saturday': '', 'Sunday': ''}

def get_period(start_day:date, days:int ):
    result ={}
    for _ in range(days+1):
        result[start_day.day, start_day.month]=start_day.year
        start_day += timedelta(1)
    return result



def get_birthdays_per_week(users:list)-> list:
    #start_day = date.today()
    start_day = date(2023,10,9)
    if not start_day.weekday():
        list_period = get_period(start_day-timedelta(2),7)
    else:
        list_period = get_period(start_day,7)
    
    for us in users:
        bd:date = us['birthday']
        
        if (bd.day,bd.month) in list(list_period):
            new_year_bd= date(list_period[(bd.day,bd.month)],bd.month,bd.day)
            wd = new_year_bd.strftime('%A')

            for key, value in dict_weekday.items():
                if wd == 'Saturday'or key == 'Sunda':
                    wd ='Monday'
                if key == wd: 
                    if not value: 
                        dict_weekday[key]= value + us['name']
                    else:
                        dict_weekday[key]= value + ', ' + us['name']
    
    
    for key, value in dict_weekday.items():
        if value:
            print(f'{key}: {value}')
  


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
    get_birthdays_per_week(users)
    


    