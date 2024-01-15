from datetime import datetime
import pytz

timezone_paris = pytz.timezone('Europe/Paris')
timezone_reunion = pytz.timezone('Indian/Reunion')

def get_date_formatted(timezone):
    date = datetime.now(timezone)
    return date.strftime("%H:%M:%S")

print(get_date_formatted(timezone_paris))
print(get_date_formatted(timezone_reunion))