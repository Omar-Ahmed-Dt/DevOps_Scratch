# ------------------------------------------------------------------------
# ------------- Practical Image Manipulation With  Pillow ----------------
# ---- https://pillow.readthedocs.io/en/stable/handbook/tutorial.html ----
# ------------------------------------------------------------------------

from PIL import Image

# Open The Image
myImage = Image.open("D:\InfluentialPicture.jpg")

# Show The Image
# Image.open("D:\InfluentialPicture.jpg").show()
# or
# myImage.show()

# Cropped My Image
mybox = (0, 0, 400, 400)        # Left, Upper, right, Lower
# mybox = (300, 300, 800, 800)
newimage = myImage.crop(mybox)

# Show New Image
# newimage.show()

# Convert My Image
mycon = myImage.convert("L")

# Save My Image
# mycon.save("D:\InfluentialPicture2__.jpg")

mycon.show()
