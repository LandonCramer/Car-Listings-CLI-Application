from datetime import datetime

current_date = datetime.now()

def parse_date(datetime_obj):
    return f'{datetime_obj.month}/{datetime_obj.day}/{datetime_obj.year}'