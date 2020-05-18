# -*- coding: utf-8 -*-

import hashlib 
from timeit import default_timer as timer

arananDeger = "26b1c3e65b82020df69f7401a2c807124ba58a2d"
toplamSayi = 0

print ("Bulunacak SHA1 hash değeri:",arananDeger)

with open('kelimeler.txt', 'r', encoding="utf8") as f:
	for line in f:
		toplamSayi +=1
print ("Textlist toplam kelime sayısı:",toplamSayi)

start = timer()

liste = [dosya.rstrip() for dosya in open('kelimeler.txt', encoding="utf8")]

for i in range(toplamSayi-1):
	sonuc = hashlib.sha1(liste[i].encode()).hexdigest()
	if arananDeger == sonuc:
		print ("Hash değeri bulundu:",liste[i])
		print ("Hesaplama",timer()-start,"saniye sürdü.")
		break
else:
	print ("Hash değeri textlist içerisinde yer almıyor.")
	print ("Hesaplama",timer()-start,"saniye sürdü.")



