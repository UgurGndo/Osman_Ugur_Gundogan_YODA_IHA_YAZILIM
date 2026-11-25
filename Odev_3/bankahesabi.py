class hesap():                  #class tanımlama

    def __init__(self,bilgiler,numara,bakiye=0):         #attribute ları tanımlama
        self.bilgiler=bilgiler
        self.numara=numara
        self.bakiye=bakiye

    def para_yatirma(self,miktar):              #para yatırma işlemini tanımlama
        if miktar>0:
            self.bakiye=self.bakiye+miktar
            print("{} kadar para yatirildi.Guncel bakiye:{}".format(miktar,self.bakiye))
        else :
            print("Yanlis tutar yazildi.") 

    def para_cekme(self,miktar):            #para çekme işlemini tanımlama
        if miktar > float(self.bakiye) :
            print("Yetersiz bakiye")
        elif miktar <=0 :
            print("Yanlis tutar yazildi.")
        else :
            self.bakiye = float(self.bakiye) - miktar
            print("{} para cekildi.Guncel bakiye {}".format(miktar,self.bakiye))

    def bakiye_goster(self):                                        #bakiye gösterme işlemini tanımlama
        print("{} bakiyeniz mevcut".format(self.bakiye))

sahip=input("Isim soyisim giriniz:")                            #kullanıcıdan bilgileri alma
hesapno=input("Hesap numarasi giriniz:")                                             #kullanıcıdan hesap no alma
baslangic_bakiyesi=input("Ilk yatiracaginiz parayi giriniz:")                #kullanıcıdan bakiye bilgisi alma

hesap1=hesap(sahip,hesapno,baslangic_bakiyesi)              #hesabı oluşturma

while True:                                             #işlem yaptırma 
    
    print("1. Para Yatir")
    print("2. Para Çek")
    print("3. Bakiye ve Hesap Bilgilerini Görüntüle")
    print("4. Cikis")
    secim=input("1.Para yatirma,2.Para cekme,3.Bakiye,4.Cikis:")            #hangi işlemin yapılacağını seçme

    if secim == "1":
        try:
            tutar = float(input("Yatirmak istediğiniz tutar (TL): "))
            hesap1.para_yatirma(tutar)
        except ValueError:
            print("Hata: Lütfen sayisal bir değer girin.")

    elif secim == "2":
        try:
            tutar = float(input("Çekmek istediğiniz tutar (TL): "))
            hesap1.para_cekme(tutar)
        except ValueError:
            print("Hata: Lütfen sayisal bir değer girin.")

    elif secim == "3":
        hesap1.bakiye_goster(self)

    elif secim == "4":
        print("Cikis yapiliyor. İyi günler!")
        break

    else:
        print("Geçersiz seçim! Lütfen 1 ile 4 arasinda bir değer girin.")



