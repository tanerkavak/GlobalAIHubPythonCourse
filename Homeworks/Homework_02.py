cv1 = {"Ad Soyad":"Erdem Yalçın",
       "Adres":"Çilek Mahallesi / Eskişehir",
       "Telefon":"+905441111110",
       "Eposta":"erdem0001@gmail.com",
       "Unvan":"Proje Sorumlusu",
       "Eğitim":"Anadolu Üniversitesi Bilgisayar Mühendisliği Bölümü",
       "İş Deneyim":"2014-2021 Kısmet Lojistik - Proje Sorumlusu"}

cv2 = {"Ad Soyad":"Yasemin Bulut",
       "Adres":"Düdük Mahallesi / Antalya",
       "Telefon":"+905441114812",
       "Eposta":"yasemin0002@gmail.com",
       "Unvan":"Sınıf Öğretmeni",
       "Eğitim":"Selçuk Üniversitesi Sınıf Öğretmenliği Bölümü",
       "İş Deneyim":"2004-2021 Antalya Susam Eğitim Kurumları - Sınıf Öğretmenliği"}

cv3 = {"Ad Spyad":"Algı Aydın",
       "Adres":"Ertuğrul Mahallesi / Bursa",
       "Telefon":"+905449974812",
       "Eposta":"algıaydın0003@gmail.com",
       "Unvan":"Sosyolog",
       "Eğitim":"Karabük Üniversitesi Sosyoloji Bölümü",
       "İş Deneyim":"2018-2021 Samsun Sosyal Hizmetler Kurumu - Sosyolog"}

cv4 = {"Ad Soyad":"Mustafa Saz",
       "Adres":"Yeni Yüzyıl Mahallesi / Manisa",
       "Telefon":"+9054394714812",
       "Eposta":"mustafasaz0004@gmail.com",
       "Unvan":"İngilizce Öğretmeni",
       "Eğitim":"Gazi Üniversitesi İngiliz Dili ve Edebiyatı Bölümü",
       "İş Deneyim":"2001-2021 Uşak Ticaret Meslek Lisesi - İngilizce Öğretmenliği"}

cv5 = {"Ad Soyad":"Esra Altın",
       "Adres":"Atatürk Mahallesi / İstanbul",
       "Telefon":"+905436514812",
       "Eposta":"esraaltin0005@gmail.com",
       "Unvan":"Grafik Tasarımcı",
       "Eğitim":"Anadolu Üniversitesi Görsel Sanatlar Bölümü",
       "İş Deneyim":"1997-2021 Arnida Bilişim Ve Reklamcılık - Web Yazılım ve Grafik Tasarımcı"}


list_00 = [cv1,cv2,cv3,cv4,cv5]

for i in list_00:
    for key,value in i.items():
        print(f"{key}: {value}")

    print("\n")
