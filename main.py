from datetime import datetime
import pytz


timezone_paris = pytz.timezone('Europe/Paris')
date = datetime.now(timezone_paris)
current_time_formatted = date.strftime("%H:%M:%S")
print(current_time_formatted)