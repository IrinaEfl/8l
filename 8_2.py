from PIL import Image
a = {1: "8m.jpg", 2: "23f.jpg", 3: "d.jpg", 4: "ng.jpg"}
print("1 - 8 март"
      "2 - 23 февраля"
      "3 - день рождения"
      "4 - новый год")
b = int(input("введите число:"))
filename = a[b]
with Image.open(filename) as img:
    img.load()
    img.show()
