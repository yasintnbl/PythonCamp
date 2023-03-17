ogrenciListesi=["Yasin Tonbul", "Selim Yıldız"]
  
while True:
  
    print("*     Öğrenci Sistemi                       *")
    print("*     1: Öğrenci Listeleme                  *")
    print("*     2: Öğrenci Ekleme                     *")
    print("*     3: Öğrenci Silme                      *")
    print("*     4: Çoklu Ekleme                       *")
    print("*     5: Öğrencileri Sıralı Listeleme       *")
    print("*     6: Öğrencileri Numarası Öğrenme       *")
    print("*     7: Çoklu Silme                        *")



    sonuc=input("Yapmak İstediğiniz İşlemi Seçiniz:  ")
    

    def ogrenciListeleme():
        print(ogrenciListesi)
    def ogrenciEkleme():
        ogrenciAdi=input("Adınızı Giriniz:  ")
        ogrenciSoyadı=input("Soyadınızı Giriniz:  ")
        yeniOgrenci=(ogrenciAdi+" "+ogrenciSoyadı)
        ogrenciListesi.append(yeniOgrenci)
        print(ogrenciListesi)
    def ogrenciSilme():
        ogrenciAdi=input("Adınızı Giriniz:  ")
        ogrenciSoyadı=input("Soyadınızı Giriniz:  ")
        silinecekOgrenci=(ogrenciAdi+ " "+ ogrenciSoyadı)
        ogrenciListesi.remove(silinecekOgrenci)
        print(ogrenciListesi)
    def birdenFazlaEkleme():
        kayitSayisi=int(input("Eklemek İstediğiniz Kayıt Sayısını Giriniz:  "))                    
        for i in range(kayitSayisi):
                ogrenciAdi=input("Adınızı Giriniz:  ")
                ogrenciSoyadı=input("Soyadınızı Giriniz:  ")
                eklenecekOgrenci=(ogrenciAdi+ " "+ ogrenciSoyadı)
                ogrenciListesi.append(eklenecekOgrenci)
                print(ogrenciListesi)
        print("Ekleme İşlemleri Tamamlandı")
    def tekTekYazdırma():
        for i in ogrenciListesi:
            print(i)
    def ogrenciNumarasi():
        for ogrenci in ogrenciListesi:
            print(f"Öğrenci Numarası: {ogrenciListesi.index(ogrenci)}, Öğrenci Adı-Soyadı:{ogrenci} ")
    def birdenFazlaSilme():
        kayitSayisi=int(input("Silmek İstediğiniz Kayıt Sayısını Giriniz:  "))                    
        for i in range(kayitSayisi):
                ogrenciAdi=input("Adınızı Giriniz:  ")
                ogrenciSoyadı=input("Soyadınızı Giriniz:  ")
                silinecekOgrenci=(ogrenciAdi+ " "+ ogrenciSoyadı)
                ogrenciListesi.remove(silinecekOgrenci)
                print(ogrenciListesi)
        print("Silme İşlemleri Tamamlandı")
    if sonuc=="1":
        ogrenciListeleme()
    elif sonuc=="2":
        ogrenciEkleme()
    elif sonuc=="3":
        ogrenciSilme()
    elif sonuc=="4":
        birdenFazlaEkleme()
    elif sonuc=="5":
        tekTekYazdırma()
    elif sonuc=="6":
        ogrenciNumarasi()
    elif sonuc=="7":
        birdenFazlaSilme()
    else:
        print("Hatalı Giriş")
           

