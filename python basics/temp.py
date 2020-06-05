fn = 0.0
print("Fahrenheit Celsius")
while fn <= 250:
	cs = (fn - 32.0)/1.8
	print("%5.1f %7.2f" % (fn, cs))
	fn = fn + 25
