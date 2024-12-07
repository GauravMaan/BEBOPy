import datetime
import time
date=datetime.datetime.now()
print(date)
print("--------------------------------------------------")
date1=datetime.date.today()
print("today date: ",date1)
print("--------------------------------------------------")
date2=datetime.date(2025,5,10)
print("Today date in formate: ",date2)
print("--------------------------------------------------")
time1=datetime.time(14,30,35)
print("Today time: ",time1)
print("--------------------------------------------------")
now=datetime.datetime.now()
print("year",now.year)
print("month",now.month)
print("day",now.day)
print("hour",now.hour)
print("minute",now.minute)
print("second",now.second)
print("--------------------------------------------------")
today=datetime.date.today()
future_date=today+datetime.timedelta(days=15)
print("future_date is : ",future_date)
print("--------------------------------------------------")
now = datetime.datetime.now()
new_year = now.year + 10
print(new_year)
print("--------------------------------------------------")
from datetime import datetime
start_date = datetime(2024, 1, 1)
current_date = datetime.now()
days = (current_date - start_date).days
print("total dates: ",days)
print("--------------------------------------------------")
from datetime import datetime
current_date = datetime.now()
date = current_date.strftime("%m %d %Y")
print("Current Date:", date)
print("--------------------------------------------------")
from datetime import datetime

time1 = datetime.strptime("10:30:00", "%H:%M:%S")
time2 = datetime.strptime("14:45:30", "%H:%M:%S")
time_difference = time2 - time1
print(time_difference)
print("--------------------------------------------------")


