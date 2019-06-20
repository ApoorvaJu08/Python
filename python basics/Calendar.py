import calendar
c = calendar.TextCalendar(calendar.THURSDAY)
#str = c.formatmonth(2025, 1)
#print(str)
#for printing calendar
#4 for april month
for i in c.itermonthdays(2025, 4):
	print(i)
