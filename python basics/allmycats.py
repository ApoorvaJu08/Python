catNames = []
while True:
	name = input('enter the name of cat' + str(len(catNames) + 1) +'(or enter nothing to stop).')
	if name == '':
		break
	catNames = catNames + [name]
print('the cat names are:')
for name in catNames:
	print(''+name)
