# --------------------------------------------
# -- Doc String & Commenting vs Documenting --
# --------------------------------------------
# [1] Documentation String For Class, Module or Function
# [2] Can Be Accessed From The Help and Doc Attributes
# [3] Made For Understanding The Functionality of The Complex Code
# [4] Theres One Line and Multiple Line Doc Strings
# -------------------------------------------------

from omar import seperator__ as sp


def sayhello(name):
    '''' 
    sayhello Function
    This Function To Say Hello From Python
    Parameter : name 
    Return => Hello preson's name 
    '''    # This Line Isn't Comment, This Is Document

    print(f"Hello {name}")


sayhello("Omar")

sp()

# To Print Doumention For This Function
print(sayhello.__doc__)
sp()
# or
help(sayhello)
