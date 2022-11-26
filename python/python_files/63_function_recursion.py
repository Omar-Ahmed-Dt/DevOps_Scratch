# -----------------------------------------------------------
# -------------- Function Recursion -------------------------
# -----------------------------------------------------------
def seperator_():
    print("#" * 50)

# x = "WWWooooooooorrrrrldd"
# print(x[1:])         # Print: WWooooooooorrrrrldd


def clean_word(word):
    if len(word) == 1:
        return word
    if word[0] == word[1]:
        return clean_word(word[1:])
    # return word
    return word[0] + clean_word(word[1:])


print(clean_word("WWWooooorrrldd"))

seperator_()
