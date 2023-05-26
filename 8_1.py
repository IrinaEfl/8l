from PIL import Image

filename = "8m.jpg"
with Image.open(filename) as img:
    img.load()

cropped_img = img.crop((100, 200, 600, 400))
cropped_img.save("c_8m.jpg")

img.show()
