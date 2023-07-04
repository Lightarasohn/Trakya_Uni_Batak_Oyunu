# ödev içerisinde hepsinde olmasa da değiştirilen veya yeni eklenen kod veya kod bloklarının yanında # DEĞİŞTİRİLDİ yazmaktadır.

import random

A = ['♠', '♣', '♥', '♦']
B = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

genel_skor = {} # DEĞİŞTİRİLDİ turlar arası her oyuncunun toplam puanını tutmak için



for i in range(int(input("Toplam Kaç Tur Oynanacak Yaziniz\n"))): # DEĞİŞTİRİLDİ her tur için deste oluşturulmalı ve her oyuncuya kartlar yeniden dağıtılmalıdır.
    # bu yüzden bu değerler ve oyunun kendisi turun for döngüsü içerisinde bulunmalıdır
    deste = []
    for i in A:
        for j in B:
            deste.append(i+j)

    oyuncular = {}
    oyuncu_sira = ['oyuncu1', 'oyuncu2', 'oyuncu3', 'oyuncu4']  # oyuncu isimleri girilecek ise boş liste olmalı
    # print("OYUNCULARIN İSİMLERİNİ GİRİN:") # oyuncu isimleri girilecek ise bu satır açılmalı
    for i in range(4):
        # oyuncular.setdefault(input("Oyuncu " + str(i+1) + ": "), {}.fromkeys(A))
        oyuncular.setdefault(oyuncu_sira[i], {}.fromkeys(A)) # isimler girilecek ise bu kapatılmalı, üstteki açılmalı

    for oyuncu in oyuncular:
        # oyuncu_sira.append(oyuncu)  # oyuncu isimleri girilecek ise bu satır açılmalı
        for i in A:
            oyuncular[oyuncu][i] = []
        for i in range(13):
            kart = random.choice(deste)
            oyuncular[oyuncu][kart[0]].append(kart[1:])
            deste.remove(kart)

    def oynanan_kart_siralama(kart_tipi):# DEĞİŞTİRİLDİ
        # o elde istenilen kart tipindeki atılan kartları gösteren bir fonksiyon
        kart_kontrol = []
        for kartlar in oynanan_kartlar:
            if kartlar[1] == kart_tipi:
                kart_kontrol.append(str(kartlar[2]))
                kart_kontrol.sort(key=B.index)
        return kart_kontrol[len(kart_kontrol)-1]

    print("\nDAĞITILAN KARTLAR:")
    for oyuncu in oyuncular:
        print(oyuncu + ":")
        oyuncu_tahmini = 0
        for karttip in oyuncular[oyuncu]:
            oyuncular[oyuncu][karttip].sort(key=B.index)  # kartlar B listesindeki sıraya göre dizilir
            print(karttip, oyuncular[oyuncu][karttip]) 
            """
            oyuncular elindeki kartlara göre kaç el kazanabileceklerini tahmin etmeleri için A dışındaki diğer tüm kartların
            toplamlarına veya maça sayılarına bakmalıdır. Kart tipi maça ise maça sayısı kadar, değil ise kartların toplam değerlerinin
            belli aralıklarda ya 1 ya da 0.5 kadar tahmin sayısı arttırılmıştır.
            """
            kart_değer_toplamlari = 0
            if karttip != '♠':
                for kartlar in oyuncular[oyuncu][karttip]:
                    kart_değer_toplamlari += B.index(kartlar)
                if kart_değer_toplamlari >= 63:
                    oyuncu_tahmini += 1
                elif kart_değer_toplamlari <= 63 and kart_değer_toplamlari >= 45:
                    oyuncu_tahmini += 0.5
            else:
                oyuncu_tahmini += len(oyuncular[oyuncu][karttip])
        oyuncular[oyuncu]["tahmin"] = round(oyuncu_tahmini)
    
    print("\nOYUN BAŞLADI...")  # Oyun sadece 1 tur (13 el) oynanacak
    kazanilan_eller = dict() # Değiştirildi: oyuncuların kart atımlarında mantıklı seçimler yapmaları ve puanlama sistemi için değiştirildi.
    macaAtildi = False
    sira = random.randrange(4)  # oyuna başlayacak oyuncu rastgele belirleniyor
    for el in range(13):  # 13 el oynanacak
        print(str(el+1) + ". el:")
        oynayan = 0
        oynanan_kartlar = []  # bu liste içine kimin hangi kartı attığı yazılacak
        while oynayan < 4:
            oyuncu = oyuncu_sira[sira]
            if oynayan == 0:  # ilk kart atacak oyuncu ise kart tipi belirlenecek (rastgele)
                while True:
                    if macaAtildi:  # Maça önceki bir elde koz olarak kullanıldı ise oyuncu Maça ile başlayabilir
                        kart_tipi = random.choice(A)
                    else:  # Maça önceki bir elde koz olarak kullanılmadı ise diğer üç kart tipinden atabilir
                        kart_tipi = random.choice(A[1:])
                    if len(oyuncular[oyuncu_sira[sira]][kart_tipi]):  # o tipte kartı yoksa döngü devam edecek
                        break
                oyuncu_kart = (oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi].pop())  # o tipteki en büyük kartı atıyor
                """
                elin başlangıcında atılan ilk kart için gerekli olan kararı kendim oynarken de çözemediğim ve
                bu konuda pek de bir fikrim olmadığı için başlangıçta atılacak en büyük kartı aynı şeklinde bıraktım.
                Fakat diğer kartlar konusunda mantıklı kararlar verildiği için bu kodu değiştirmediğim halde oyun mantıklı ilerliyor.
                """
            else:  # diğer oyuncular ilk oyuncunun belirlediği kart tipinde kart atacak
                if len(oyuncular[oyuncu][kart_tipi]):# DEĞİŞTİRİLDİ
                        for oyuncu_karti in oyuncular[oyuncu][kart_tipi]:
                            if B.index(oyuncu_karti)>B.index(en_buyuk[2]): # DEĞİŞTİRİLDİ: oyuncuların atılan önceki kartlara göre karar vermesini sağlar.
                                oyuncu_kart = (oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi].pop(oyuncular[oyuncu][kart_tipi].index(oyuncu_karti)))
                                break
                        else:
                            oyuncu_kart = (oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi].pop(0))
                elif len(oyuncular[oyuncu]['♠']):# o kart tipinde kartı yoksa en küçük maça kartını atacak
                    if en_buyuk[1] == '♠': # DEĞİŞTİRİLDİ: eğer daha önceden maça atılmış ise o maçadan daha yüksek bir maça atabilmek için bir kontrol noktası.
                        for oyuncu_karti in oyuncular[oyuncu]['♠']:
                            if B.index(oyuncu_karti) > B.index(en_buyuk[2]): # DEĞİŞTİRİLDİ: oyuncuların atılan önceki kartlara göre karar vermesini sağlar.
                                oyuncu_kart = (oyuncu, '♠', oyuncular[oyuncu]['♠'].pop(oyuncular[oyuncu]['♠'].index(oyuncu_karti)))
                                break
                    else:# DEĞİŞTİRİLDİ: daha önceden maça atılmamış ise oyuncu elindeki en küçük maçayı atar.
                        oyuncu_kart = (oyuncu, '♠', oyuncular[oyuncu]['♠'].pop(0))
                    macaAtildi = True  # Maça koz olarak oynandığı için sonraki ellerde doğrudan Maça atılabilecek
                else:  # maça kartı da yoksa, diğer tiplerin birinden en küçük kartı atacak
                    kart_tipleri = A[1:].copy()  # maça hariç diğer 3 kart tipi kopyalandı
                    for tip in kart_tipleri:
                        if len(oyuncular[oyuncu][tip]):
                            oyuncu_kart = (oyuncu, tip, oyuncular[oyuncu][tip].pop(0))
                            break
            print(oyuncu_kart[0], oyuncu_kart[1] + oyuncu_kart[2])
            oynanan_kartlar.append(oyuncu_kart)
            oynayan += 1
            sira += 1
            if sira >= 4:
                sira -= 4
            
            en_buyuk = oynanan_kartlar[0]   # ilk atılanı en büyük kart kabul et
            for kart in oynanan_kartlar[1:]:
                if kart[1] == en_buyuk[1] and B.index(kart[2]) > B.index(en_buyuk[2]):
                    en_buyuk = kart  # en büyük ile aynı kart tipinde daha büyük atıldı ise en büyük kart kabul et
                elif en_buyuk[1] != '♠' and kart[1] == '♠':
                    en_buyuk = kart  # en büyük maça değilken maça atıldı ise en büyük kart kabul et
        print("eli kazanan:", en_buyuk[0])
        sira = oyuncu_sira.index(en_buyuk[0])
        kazanilan_eller[en_buyuk[0]] = kazanilan_eller.setdefault(en_buyuk[0], 0) + 1 # DEĞİŞTİRİLDİ: artık oyuncuların kaç el kazandığını tutar


    """
    oyuncuların kazandıkları el sayılarına göre puanlama sistemi yapılmalıdır.
    burada ayrı bir skor sözlüğü oluşturulup her oyuncuya göre farklı skorlar kazandıkları el sayısına göre tutulmaktadır.
    """
    skor = {} # DEĞİŞTİRİLDİ
    for oyuncu in oyuncular: # DEĞİŞTİRİLDİ
        if not oyuncu in kazanilan_eller:
            """
            bu kontrol yapılmaz ise sistem hata verir.
            çünkü kazanilan_eller sözlüğü sadece el kazanan oyuncuları tutmaktadır.
            el kazanmayan oyuncular bu sözlüğün içerisine giremez.
            bu yüzden sistem aşağıdaki karşılaştırmalara geldiğinde KEY ERROR verir.
            normalde try-except bloklarıyla bu iş çözülebilir fakat derslerde henüz görmediğimiz için bu sorun if bloğu ile çözülmüştür.
            """
            kazanilan_eller[oyuncu] = 0
        else: 
            if kazanilan_eller[oyuncu] >= oyuncular[oyuncu]["tahmin"]: # DEĞİŞTİRİLDİ: kazanılan eller oyuncu tahminine eşit ya da büyük olması durumundaki skor
                skor[oyuncu] = oyuncular[oyuncu]["tahmin"]*(10) + kazanilan_eller[oyuncu] - oyuncular[oyuncu]["tahmin"]
            else: # DEĞİŞTİRİLDİ: kazanılan eller oyuncu tahmininden az olması durumundaki skor
                skor[oyuncu] = oyuncular[oyuncu]["tahmin"]*(-10)
            if genel_skor.setdefault(oyuncu, 0): # DEĞİŞTİRİLDİ: burada setdefault kullanılmasının nedeni oyunun ilk turunda henüz genel_skor sözlüğünde oyuncu KEY'lerinin bulunmaması.
                genel_skor[oyuncu] += skor[oyuncu] # oyuncu çoktan oluşturulmuş ise oyuncunun o tur içindeki skoru genel skoruna ekler
            else:
                genel_skor[oyuncu] = 0 # oyuncu oluşturulmamış ise önce oyuncu KEY ve VALUE değerini oluşturur daha sonra ilk turdaki skorunu VALUE değerine atar
                genel_skor[oyuncu] = skor[oyuncu]
            
    print("Kazanilan eller:", kazanilan_eller) # DEĞİŞTİRİLDİ: testler sırasında oluşturuldu istenilirse kapatılınabilir
    print("SKOR:", skor) # bir turluk skoru gösterir
    for oyuncu in oyuncular: # DEĞİŞTİRİLDİ: testler sırasında oyuncuların tahmin sayısını göstermek için oluşturuldu istenilirse kapatılınabilir
        print(oyuncu, "tahmin sayisi:" ,oyuncular[oyuncu]["tahmin"])
        
print("GENEL SKOR:", genel_skor) # DEĞİŞTİRİLDİ: genel skoru gösterir