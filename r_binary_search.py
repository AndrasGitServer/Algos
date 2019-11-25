
def rbs( myList , num , i=0 , bool=False ):

	if myList[i] == num:
		print("returning bool found number in the list !")
		bool = True

	if i == len(myList) - 1:
		print("returning bool at end of the list !")
		return bool

	return rbs( myList , num , i = i+1 , bool=bool)



my_list = ( 0 , 1 ,2 ,3 , 4 , 5 , 100 ,99 ,88)

num_check = 88

result = rbs( my_list , num_check )

print(result)

