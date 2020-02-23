from datetime import datetime
import datetime

#Παίρνω την ημερομηνία απ'τον χρήστη
year = int(input('Enter a year'))
month = int(input('Enter a month'))
day = int(input('Enter a day'))
date1 = datetime.date(year, month, day)
print (date1)



#Υπολογίζω την διαφορά

from datetime import datetime
diff = datetime.now().date() - date1
print (diff)

