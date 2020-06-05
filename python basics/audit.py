import calendar
for month in range(1, 13):
    #It retrieves a list of weeks that represent a month
    mycal = calendar.monthcalendar(2025, month)
    print(mycal)
    #The first MONDAY has to be within first 2 weeks
    week1 = mycal[0]
    week2 = mycal[1]
    if week1[calendar.MONDAY] != 0:
        auditday = week1[calendar.MONDAY]
    else:
        auditday = week2[calendar.MONDAY]
    print("%10s %2d" % (calendar.month_name[month], auditday))