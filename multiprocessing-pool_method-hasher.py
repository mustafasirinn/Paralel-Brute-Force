# -*- coding: utf-8 -*-

import hashlib
from timeit import default_timer as timer
from multiprocessing import Pool

def kelimeSayar(textlist):
    toplamSayi=0
    print(textlist)
    with open(textlist, 'r', encoding="utf8") as f:
        for line in f:
            toplamSayi += 1
    return toplamSayi

def hasher(textlist, hashDegeri, basla, bitir):
    liste = [dosya.rstrip() for dosya in open(textlist, encoding="utf8")]

    for i in range(basla,bitir):
        sonuc = hashlib.sha1(liste[i].encode()).hexdigest()
        if hashDegeri == sonuc:
            print("Hash değeri bulundu:", liste[i])
            break
    else:
        print("Hash değeri textlist içerisinde yer almıyor.")

def multi_run_wrapper(args):
   return hasher(*args)

if __name__=='__main__':
    arananDeger = "26b1c3e65b82020df69f7401a2c807124ba58a2d"
    a = []

    dosya = input("dosya ismi:")
    kelimeSayisi = kelimeSayar(dosya)
    print("Textlist toplam kelime sayısı:", kelimeSayisi)

    a.append(kelimeSayisi)
    b = int(kelimeSayisi/4)
    for i in range(4):
        a.append(kelimeSayisi - b)
        kelimeSayisi -= b

    print("İşlem parçaları")
    for i in range(4):
        print(a[i+1],"-",a[i])

    p = Pool(6)
    start = timer()
    p.map(multi_run_wrapper, [(dosya, arananDeger, a[1], a[0]), (dosya, arananDeger, a[2], a[1]),
                              (dosya, arananDeger, a[3], a[2]), (dosya, arananDeger, a[4], a[3])])
    print("işlem", timer() - start, "saniye sürdü.")

