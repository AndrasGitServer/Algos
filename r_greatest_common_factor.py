# Euclid's algorithm

def rGCF( num1 , num2 ):

	if num1 == num2:		# if num1 - num2 == 0 then return num1.
		return num1

	if num1 > num2:
		print("A subtraction =", num1 - num2)
		return rGCF(num1 - num2 , num2)

	if num2 > num1:
		print("A subtraction =", num2 - num1)
		return rGCF(num2 - num1, num1)



print("=== The result is ===>" , rGCF( 12 , 3))

# The factors of 3 are: 1, 3
# The factors of 12 are: 1, 2, 3, 4, 6, 12
# Then the greatest common factor is 3.

print("=== The result is ===>" ,  rGCF( 71 , 63))

# The factors of 63 are: 1, 3, 7, 9, 21, 63
# The factors of 71 are: 1, 71
# Then the greatest common factor is 1.

