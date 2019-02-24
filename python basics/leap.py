year = int(input())
def is_leap(year):
	leap1 = False
	leap2 = True
	if (year>=1990 and year<=100000):
		if( year%4 == 0 ):
			if( year%100 == 0):
				if( year%400 == 0):
					return leap2
				else:
					return leap1
			else:
				return leap2
		else: 
			return leap1
	else:
		return leap1

print(is_leap(year))
