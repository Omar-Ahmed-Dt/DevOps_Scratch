# ---------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------

# [1] Dictionary
user = {
    "name": "Omar",     # name => Key && Omar => value
    "age": 24,
    "country": "Egypt",
    # Key be Immutable => Number & String & Tuple
    1: "One",
    (1, 2, 3, 4): "this is a Tuple",
    # Key be not  Mutable => List
    # [1,2,3,4] : "this is Error",

    # Value be any data type
    "list": [1, 2, 3, 4, 5],
    "skills": ["python", "bash", "linux"],
    "rating": 10.034,
    # Value be unique
    # "rating": 20.10
}

print(user)

# [2] Dict Is Not Ordered You Access Its Element With Key
print(user["country"])
print(user.get("country"))
print(user.keys())      # Print all keys
# Print: dict_keys(['name', 'age', 'country', 1, (1, 2, 3, 4), 'list', 'skills', 'rating'])
print(user.values())    # Print all values
# Print: dict_values(['Omar', 24, 'Egypt', 'One', 'this is a Tuple', [1, 2, 3, 4, 5], ['python', 'bash', 'linux'], 10.034])

# [3] Two-Dimensional Dictionary
# Values can be Dictionary (any data type)
languages = {
    "One": {
        "name": "HTML",
        "progress": "80%",
    },
    "Two": {
        "name": "Css",
        "progress": "90%"
    },
    "Three": {
        "name": "Js",
        "progress": "90%"
    },
}

print(languages)
print(languages["One"])
print(languages["Two"])
print(languages["Two"]["progress"])        # Print: 90%
print(languages["Two"]["name"])        # Print: Css
print(len(languages))           # Print: 3
print(len(languages["One"]))    # Print: 2

# Create Dictionary From Variables
frameworkOne = {
    "name": "Vuejs",
    "progress": "80%"
}

frameworkTwo = {
    "name": "ReactJs",
    "progress": "80%"
}

frameworkThree = {
    "name": "Angular",
    "progress": "80%"
}

allframework = {
    "One": frameworkOne,
    "Two": frameworkTwo,
    "Three": frameworkThree,
}
print(allframework)
