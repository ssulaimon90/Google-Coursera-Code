def multiplication_table(start, stop):
	for x in range(, stop):
		for y in (start, stop):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above