# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# --       Advanced Example        --
# -----------------------------------
from omar import seperator__ as sp

the_file = None
tries = 5
while tries > 0:

    try:  # Try Open File
        print("Enter The File Name With Absolute Path To Open")
        print(f"{tries} Tries Left.")
        print("Example: D:\Python\Files\yourfile.extension")
        sp()
        file_name_and_path = input("File Name => : ").strip()
        the_file = open(file_name_and_path, "r")
        print(the_file.read())
        break

    except FileNotFoundError:
        print("File Not Found Please Be Sure The Name is Valid")
        tries -= 1
    except:
        print("Error Happen !")
    finally:
        if the_file is not None:
            sp()
            the_file.close()
            print("File Closed.")
            sp()
else:
    print("All Tries Is Done.")
