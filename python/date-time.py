#001-002 PRINTING CURRENT DATE AND TIME
from datetime import datetime
now = datetime.now()
print now

#003 EXTRACTING INFORMATION
from datetime import datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

print current_year
print current_month
print current_day

#004-006 FORMATTING DATE & TIME - dd/mm/yyy hh:mm:ss
from datetime import datetime
now = datetime.now()

print '%02d/%02d/%04d' % (now.day, now.month, now.year)
print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
