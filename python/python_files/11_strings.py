# --------------------------
# Strings
# --------------------------


fvarold = "this is single quote \"Test\""
fvar = "This is single quote 'test'"
svar = 'This is second single quote "test"'
print(fvarold)
print(fvar)
print(svar)

# ----------------------------------

multivarold = "omar\nahmed\nmohamed"
multivar = """ omar 
ahmed 
mohamed """
multivar2 = ''' omar 
ahmed 
alshishiny 
'''
multivar3 = """ Omar "First"
Ahmed 'Second' 
Mohamde "Third" '& End '
"""
multivar4 = """ Omar "First" \
Ahmed 'Second' 
Mohamde  "Third" '& End '
"""
multivar5 = """ Omar "First" \\
Ahmed 'Second' 
Mohamde  "Third" '& End '
"""
print(multivarold)
print(multivar)
print(multivar2)
print(multivar3)
print(multivar4)    # escape to new line
print(multivar5)    # escape to \
