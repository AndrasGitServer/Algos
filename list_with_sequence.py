def function_find_range( mylist ):
    print( mylist )
    
    out = ""
    list2 = []

    for i in range( 0 , len(mylist) , 1 ):
        
        if i != len(mylist):

            if (mylist[i]+1) == (mylist[i+1]):
                list2.append(mylist[i])
            else:
                list2.append(mylist[i])
                if len(list2) == 1:
                    out = str(list2[0])
                else:
                    out = str(list2[0]) + "-" + str(list2[len(list2)-1]) + "," + str(mylist[i+1])
                list2 = []
        else:
            print("end of list")

    return out


#-----------------------------
mylist = [1,2,3,9,17,18,19,23]
print(  function_find_range( mylist )   )

