from datetime import datetime
day1 = datetime(2024, 2, 10, 3, 25)
day2 = datetime(2024, 2, 12, 3, 25)
difference = day2 - day1
print(difference.total_seconds())
