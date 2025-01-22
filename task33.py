from datetime import datetime
now = datetime.now()
date = now.replace(microsecond=0)
#print with microseconds
print (now)
#print without microseconds
print (date)