#   Validate a string with parenthesis
#   with the correct order & qty of parenthesis.
#   example:    "(a)"   valid
#               ")("    not valid

def parenthesis_check( someString ):
    openP  = 0
    closeP = 0

    for i in range( 0 , len( someString ) , 1):
        
        if someString == "(":
        
            openP = openP + 1

            if openP >= closeP:
                continue
            else:
                return False
        
        elif someString == ")":

            closeP = closeP + 1
        
            if closeP > openP:
                return False
        
    if closeP != openP:
        return False
    else:
        return True

print( parenthesis_check("(ab)((abc)") )
    