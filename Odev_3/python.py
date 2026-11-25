
## IF conditional exercise 
"""liste = ['a','b','c']
hedef_harf = 'd'
if hedef_harf in liste and (hedef_harf == liste[0]):
    print('Buldum ve ilk indexte.')
elif hedef_harf in liste:
    ('Buldum ama ilk indexte değil')
else :
    liste.append(hedef_harf)
    print('Hedef harfi listeye ekledim.') """

##For döngüsü
"""yorum_birakanlar = ["Ismail Aydemir", "Uygar Aydin","Naz Yagccioglu","Ferhat Ibrik","Ulas Acil","Bilal Kurucay"]
moderator="Ferhat Ibrik"
kullanici_sayisi=0
moderator_sayisi=0
for kullanici in yorum_birakanlar:
    ad=kullanici.split()[0]
    soyad=kullanici.split()[1]
    if (kullanici==moderator):
        moderator_sayisi = moderator_sayisi+1
        print("{0}.Moderatorun adi {1} ve Soyadi {2}".format(moderator_sayisi,ad,soyad))
    else :
        kullanici_sayisi= kullanici_sayisi+1
        print("{0}.Kullanicinin adi {1} ve Soyadi {2}".format(kullanici_sayisi,ad,soyad))"""

##While Döngüsü ile faktöriyel hesaplama
"""sayi=6
sonuc=1
while sayi > 0 :
    sonuc=sonuc*sayi
    sayi = sayi - 1
print("Sonuç={}".format(sonuc))"""

##Fonksiyon ve input örneği 
"""def uygulama():
    girdi=input("Bir sayi giriniz:")
    islem=input("Verinin tek mi cift mi oldugunu sorgula:")
    if islem=="cift":
        if (int(girdi)%2==0):
            return "Bu bir cift sayidir"
        else:
            return "Bu bir tek sayidir"
    elif islem=="tek":
        if (int(girdi)%2==1):
            return "Bu bir tek sayidir"
        else :
            return "Bu bir cift sayidir"
"""

##Fonksiyon,döngü,input örnek
"""def eposta_kontrol():
    girdi=input("Gecerli bir eposta girin:")
    while not(("."in girdi) and ("@" in girdi)):
        print("Gercersiz bir eposta girdiniz.")
        girdi=input("Gecerli bir eposta girin:")
    else :
        print("Gecerli bir eposta girdiniz.")
eposta_kontrol()"""
#Try except, fonk örnek
"""def tam_sayiya_cevir():
    girdi=input("Bir ondalik sayi giriniz:")
    try:
        girdi=float(girdi)
        print("Islemin sonucu={}".format(round(girdi)))
        status="basarili"
    except :
        print("{} girdisi ondalik sayiya cevrilmiyor.".format(girdi))
        status="basarisiz"
    finally:
        print("Islem {} olarak tamamlandi.".format(status))

tam_sayiya_cevir()"""

##Class yapısı
"""class Ucus():
    havayolu= "THY"

    def __init__(self,kod,kalkis,varis,sure,kapasite,yolcu):
        self.kod=kod
        self.kalkis=kalkis
        self.varis=varis
        self.sure=sure
        self.kapasite=kapasite
        self.yolcu=yolcu

    def anons_yap(self):
        return print("{} sefer sayili, {}-{} ucusumuz  {} dakika surecektir.".format(self.kod,self.kalkis,self.varis,self.sure))
ucus3=Ucus("TK223","BOD","ANT",30,40,50)
ucus3.anons_yap()"""


