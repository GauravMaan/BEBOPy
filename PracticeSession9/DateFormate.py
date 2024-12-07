from datetime import datetime
current_time = datetime.now()
print("Current Date and Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
specific_time = datetime(2025, 1, 1, 12, 0)
print("Specific Date and Time:", specific_time.strftime("%A %B, %Y at %H:%M"))
