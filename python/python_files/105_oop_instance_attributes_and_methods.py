# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------

# class Member:
#     def __init__(self):
#         self.name = "Omar"


# member_one = Member()
# member_two = Member()

# print(member_one.name)
# print(member_two.name)

class Member:
    def __init__(self, first_name, middle_name, last_name):
        self.f_name = first_name
        self.m_name = middle_name
        self.l_name = last_name


member_one = Member("Omar", "Ahmed", "Mohamed")
member_two = Member("Ahmed", "Ali", "Osama")

print(member_one.f_name, member_one.m_name, member_one.l_name)
print(member_two.f_name, member_two.m_name, member_two.l_name)
