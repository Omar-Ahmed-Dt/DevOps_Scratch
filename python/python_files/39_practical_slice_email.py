# ---------------------------------
# ---Practical Slice Email---------
# ---------------------------------

# Example :
# email = "Omarahmed990@gmail.com"
# print(email.index("@"))
# print(email[:email.index("@")])

theName = input("What's Your Name?").strip().capitalize()
theEmail = input('what\s Your Email?').strip()

username = theEmail[:theEmail.index("@")]
domain = theEmail[theEmail.index("@")+1:]

print(f"Hello {theName}, Your Email Is {theEmail}")
print(f"Your Username Is {username} \nYour Domain Is {domain}")
