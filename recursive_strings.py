# Recursive, from one string get characters combinations.

def r_rio( originalStr , sub="" , i=0 ):

    if i == len(originalStr):
        return [sub]                # returns a list. It returns the string sub in a list.
    else:
        return r_rio( originalStr , sub + originalStr[i] , i+1 ) + r_rio( originalStr , sub , i+1)



new_list = r_rio("Darling")
print(new_list)
print("Qty of unique combinations (little strings) 2^characters =", len(new_list))
print()

new_list = r_rio("Yes")
print(new_list)
print("Qty of unique combinations (little strings) 2^characters =", len(new_list))
print()

