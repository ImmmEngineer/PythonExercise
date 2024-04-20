def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    ogrenciAd = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3
    return ogrenciAd + ":" + str(ortalama) + "\n"

def ortalama_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))
def not_gir():

    ad = input('Adiniz : ')
    soyad = input("Soyad : ")
    not1 = input("not1 : ")
    not2 = input("not2 : ")
    not3 = input("not3 : ")
    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad + " " + soyad + ":" + not1 + "," +not2 + ","+not3 + "\n")

def notlari_kaydet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)
while True:
    islem = int(input('1- Notlari Oku\n2- Not Gir\n3- Notlari Kaydet\n4- Cikis\n'))

    if islem==1:
        ortalama_oku()
    elif islem==2:
        not_gir()
    elif islem==3:
        notlari_kaydet()
    else:
        break