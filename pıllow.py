import os

from PIL import Image
import PIL

img = Image.open(r'C:\Users\Casper\PycharmProjects\Miuul\dss.jpg')
img.show()

img.size
#boyutlarını yazdırır

img.mode

img.rotate(90, expand=1).show()
#90 derece çevirir

img.transpose(method=Image.FLIP_TOP_BOTTOM).show()
#altını üstüne çevirir.

img.resize((300, 300)).show()
#istediğimiz boyut değerlerine getiriyor

width, height = img.size

new_width =int(width/3)
new_height =int(height/3)

new_height
small_image = img.resize((new_width, new_height)).show()
#orantılı bir şekilde fotograf boyutunu küçültmeye yarar.

folder_path =(r'C:\Users\Casper\PycharmProjects\images')
paths = os.listdir(folder_path)
#image klasörü altındaki bütün jpg dosylarını getiriyor.

for path in paths:
    if path.endswith('.jpg'):
        img = os.path.join(folder_path, path)
        print(img)
# uzantısı jpg olan dosyaları gösterir

for path in paths:
    if path.endswith('.jpg'):
        img = Image.open(os.path.join(folder_path, path))
        thumb = img.copy()
        thumb.thumbnail((300, 300))
        thumb = thumb.transpose(Image.FLIP_LEFT_RIGHT)
thumb.show()
