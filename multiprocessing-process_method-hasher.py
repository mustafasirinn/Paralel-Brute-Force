# -*- coding: utf-8 -*-

import hashlib
from timeit import default_timer as timer
from multiprocessing import Process

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

if __name__=='__main__':
    arananDeger = "26b1c3e65b82020df69f7401a2c807124ba58a2d"
    a = []

    dosya = input("dosya ismi:")
    kelimeSayisi = kelimeSayar(dosya)
    print("Textlist toplam kelime sayısı:", kelimeSayisi)

    parca = int(input("işlem kaç parçaya bölünsün(1-12): "))
    a.append(kelimeSayisi)
    b = int(kelimeSayisi/parca)
    for i in range(parca):
        a.append(kelimeSayisi - b)
        kelimeSayisi -= b

    print("İşlem parçaları")
    for i in range(parca):
        print(a[i+1],"-",a[i])

    procs = []
    start = timer()
    for i in range(parca):
        proc = Process(target=hasher, args=(dosya, arananDeger, a[i+1], a[i]))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()
    print("işlem", timer() - start, "saniye sürdü.")

