from datetime import datetime, timedelta
now = datetime.now()
yesterday = now - timedelta(days = 1)
tomorrow = now + timedelta(days = 1)
print("yesterday:", yesterday.strftime("%y-%m-%d"))
print("now:", now.strftime("%y-%m-%d"))
print("tomorrow:", tomorrow.strftime("%y-%m-%d"))