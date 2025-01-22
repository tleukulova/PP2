from datetime import datetime, timedelta
current_date = datetime.now()
days = timedelta(days = 5)
result = current_date - days
print (result)