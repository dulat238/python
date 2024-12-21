from datetime import datetime

def datetime_info(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return{
        'formatted_date' : date.strftime('%d-%m-%Y'),
        'weekday': date.strftime('%A'),
        'days_until_next_year':(datetime(date.year + 1, 1, 1)-date).days 
    }
print (datetime_info('2024-09-19'))