# Python Pillow Image Kutuphanesi

## Pillow Nedir ?
Pillow modülü Python için geliştirilen, bizlere görüntü işleme yetenekleri sağlayan açık kaynak kodlu bir yazılımdır. 
Bu makalede bize tanınan imkanları uygulamalı olarak ele alacağız. Vakit kaybetmeden kurulum aşamasına geçelim.

## Nasıl Kurulur?
Öncelikle komut satırını açıyoruz. Ardından komut satırına 'pip3 install pillow' yazıyoruz. Kurulum işlemimiz gerçekleşti!

## Kod Zamanı...
İlk olarak temel fonksiyonların nasıl kullanılacağını öğrenelim. Ama ondan önce modülü import etmemiz gerekiyor. Bunun için PIL'in altındaki Image fonksiyonunu
dahil ediyoruz. 'from PIL import Image' yazarak.

Dosya açmak için 'open()' fonksiyonunu, görüntülemek içinse 'show()' fonksiyonunu kullanıyoruz.

![image](https://user-images.githubusercontent.com/78909023/194879360-863c5790-05f1-4641-9ee4-e9fa46372d37.png)

Resimdeki gibi jpg dosyamız açılıyor.

#### Görüntü hakkında bilgi almak:
![image](https://user-images.githubusercontent.com/78909023/194879492-605a354e-83a7-40c8-a847-99d54bff02c4.png)

#### Görüntüyü döndürmek:

-> 90 derece döndürmek :

![image](https://user-images.githubusercontent.com/78909023/194879765-ffe220a1-ad04-40ef-8d5b-dd340d1d20d4.png)


-> 180 derece döndürmek

![image](https://user-images.githubusercontent.com/78909023/194879851-2876166a-29ff-4eb3-a9aa-e8cfb41a98a2.png)


-> orantılı boyut değiştirme

![image](https://user-images.githubusercontent.com/78909023/194880063-c372b285-6cf4-45e3-9c7a-4e6b36c0431a.png)




