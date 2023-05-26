from PIL import Image, ImageDraw, ImageFont
name = input("Введите имя:")
filename = "ng.jpg"
with Image.open(filename) as img:
        img.load()
font = ImageFont.truetype("arial.ttf", 20)
draw_text = ImageDraw.Draw(img)
draw_text.text((50, 100), name + " , с праздником!", font=font, fill=("black"))
img.show()
img.save(name + "namen.jpg")

