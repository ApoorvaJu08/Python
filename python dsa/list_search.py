#l = input('Enter your list: ')
#l = [int(y) for y in l.split(',')]
#v = input('Enter the number to be searched')
def findpos(l,v):
        
	(found,i) = (False,0)
	while i<len(l):
		if not found and l[i] == v:
			(found,pos) = (True,i)
		i=i+1
	if not found:
		pos = -1
	return(pos)	   




     




















