
paragraf=input("Lutfen bir paragraf veya kelime giriniz:")      #kullanıcıdan metnimi aldım
toplamkarakter=len(paragraf)          #toplam karakter sayımı hesapladım
kucultulmus_paragraf=paragraf.lower()  #tüm harfleri küçük olarak ayarladım
kelimeler=kucultulmus_paragraf.split() #kelimeleri tek tek ayırıp listeledim
toplamkelime=len(kelimeler)       #kaç kelime olduğunu buldum
en_uzun_kelime=0           #en uzun kelimenin uzunluğunun başlangıç değeri
kelimetekrari={}            #kelimelerin tekrar sayılarının tutulacağı yer
for kelime in kelimeler:
    if len(kelime)>en_uzun_kelime:
        en_uzun_kelime=len(kelime)

    if kelime in kelimetekrari:
        kelimetekrari[kelime] += kelimetekrari
    else :
        kelimetekrari[kelime] = 1

print(" Paragraf {0} kelimedir. Paragraf {1} karakterdir. En uzun kelime {2} harftir. Kelime tekrar sayilari {3}'tür.".format(toplamkelime,toplamkarakter,en_uzun_kelime,kelimetekrari))
        
