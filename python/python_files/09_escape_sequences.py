# --------------------------
# Escape Sequances Characters :
# \ : back slash
# \b => Back Space
# \newline => Escape new line + \
# \\ => Escape Back Slach
# \' => Escape Single Quotes
# \" => Escape Double Quotes
# \n => Line feed
# \r => Carriage return
# \t => Horizontal tab
# \xhh => Character Hex value , hh : char hex value "https://www.ibm.com/docs/en/ste/8.4.1?topic=information-hex-decimal-symbol-values"
# --------------------------

# Back Space
print("Hello\bWorld")   # Will remove o

# Escape new line + \
print(" Hello \
I love \
python")

# Escape Back Slach
print("I love Back Slash \\")

# Escape Single Quotes
print('I love Sigle Quote \'Test\'')

# Escape Double Quotes
print("I love Double Quote \"Test\"")

# Line feed
print("Hello World \nSecond line")

# Carriage return
print("1234\rabc")
print("12345\rab")

# Horizontal tab
print("Hello\tPython")

# Character Hex value
print("\x4F\x6D\x61\x72")
