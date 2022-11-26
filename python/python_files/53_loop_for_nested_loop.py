# -------------------------
# ----- Loop => For -------
# ---- Nested Loop --------
# -------------------------

# peoples = ["Omar", "Ali", "Mohamed", "Ahmed", "Osama"]

# skills = ["Httml", "Css", "Js"]

# for name in peoples:
#     print(f"{name} Skills is: ")
#     for skill in skills:
#         print(f"- {skill}")

# print("#" * 50)

# Dictionary

peoples = {
    "Osama": {
        "Html": "70%",
        "Css": "80%",
        "Js": "70%"
    },
    "Ahmed": {
        "Html": "90%",
        "Css": "80%",
        "Js": "90%"
    },
    "Sayed": {
        "Html": "70%",
        "Css": "60%",
        "Js": "90%"
    }
}

# print(peoples["Osama"])
# print(peoples["Osama"]["Css"])

for name in peoples:
    # print(f"Skills For {name} is: {peoples[name]}")
    print(f"Skills For {name} is:")
    for skills_ in peoples[name]:
        print(f"=>{skills_.upper()}: {peoples[name][skills_]}")
