import hashlib

my_dicto_table ={
					"1" : "one",
					"2" : "two",
					"3" : "three",
					"4" : "four",
}

list_to_check_in_table = [ "1" , "four" ]


for i in my_dicto_table:
	print(i , my_dicto_table[i])

print()

for i in list_to_check_in_table:
	print(i)

print()

for j in list_to_check_in_table:
	for k in my_dicto_table:
		if j == k:
			print("found", j , k)
		if my_dicto_table[k] == j:
			print("Found element in list and also in the WHOLE dictionary_table (key & value):",j)

print()

if "4" in my_dicto_table:
	print("Checks the KEY only ! and found it without for loop in the dictionary! :", "4")

print()

for value in my_dicto_table.values():
	print("value: " , value)

print()

string_to_hash = "horse"
print( string_to_hash + " : " +	hashlib.md5(	string_to_hash.encode()		).hexdigest()	)

string_to_hash = "dog"
print( string_to_hash + " : " +	hashlib.md5(	string_to_hash.encode()		).hexdigest()	)

print()

print("The length of the dictionary is: ", len(my_dicto_table))
print("The length of the list is: ", len(list_to_check_in_table))

print()

for key,value in my_dicto_table.items():
	print(key,value)

	

