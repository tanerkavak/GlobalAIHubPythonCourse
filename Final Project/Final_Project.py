class Quiz():
    def __init__(self):
        super(Quiz,self).__init__()
        self.point = 0
        self.question_01 = "Soru 1: Gezilerini ‘Seyahatname’ adlı eserde toplayan Türk gezgin kimdir?"
        self.question_02 = "Soru 2: 1071’de yapılan Malazgirt Savaşıyla Anadolu’nun kapılarını\nTürklere açan Selçuklu Sultanı kimdir?"
        self.question_03 = "Soru 3: Çinlilerin Hun, Tunguz ve Moğol akımlarını durdurmak için inşa\nettiği yapı hangisidir?"
        self.question_04 = "Soru 4: Milli mücadele döneminde işgallere karşı direnen düzensiz\nbirliklerin adı nedir?"
        self.question_05 = "Soru 5: Rumeli hisarını hangi padişah yaptırmıştır?"
        self.question_06 = "Soru 6: Türk hanlarının yaşadığı çerge olarak da bilinen büyük ve\nsüslü çadırın adı nedir?"
        self.question_07 = "Soru 7: İlk evcilleştirilmiş hayvan aşağıdakilerden hangisidir?"
        self.question_08 = "Soru 8: İstanbul hangi coğrafi bölgemizde yer almaktadır?"
        self.question_09 = "Soru 9: Köylülerin el birliği ile köyün işini birlikte yapmalarına ne\nad verilir?"
        self.question_10 = "Soru 10: Gabon ülkesinin başkenti nedir?"

    def Guestion001(self):
        print("-"*50)
        print(self.question_01)
        print("-"*50)
        self.reply = input("Cevap: ")
        self.reply = self.reply.replace("I", "ı").replace("İ", "i").lower()
        if self.reply == "evliya çelebi":
            print("-"*50)
            print("Doğru Cevap...")
            self.point += 10
        else:
            print("-"*50)
            print("Yanlış Cavap...")

    def Guestion002(self):
        print("-"*50)
        print(self.question_02)
        print("-"*50)
        self.reply = input("Cevap: ")
        self.reply = self.reply.replace("I", "ı").replace("İ", "i").lower()
        if self.reply == "sultan alparslan":
            print("Doğru Cevap...")
            self.point += 10
        else:
            print("Yanlış Cavap...")

    def Guestion003(self):
        print("-"*50)
        print(self.question_03)
        print("-"*50)
        self.reply = input("Cevap: ")
        self.reply = self.reply.replace("I", "ı").replace("İ", "i").lower()
        if self.reply == "çin seddi":
            print("-"*50)
            print("Doğru Cevap...")
            self.point += 10
        else:
            print("-"*50)
            print("Yanlış Cavap...")

    def Guestion004(self):
        print("-"*50)
        print(self.question_04)
        print("-"*50)
        self.reply = input("Cevap: ")
        self.reply = self.reply.replace("I", "ı").replace("İ", "i").lower()
        if self.reply == "kuvayi milliye":
            print("-"*50)
            print("Doğru Cevap...")
            self.point += 10
        else:
            print("-"*50)
            print("Yanlış Cavap...")

    def Guestion005(self):
        print("-"*50)
        print(self.question_05)
        print("-"*50)
        self.reply = input("Cevap: ")
        self.reply = self.reply.replace("I", "ı").replace("İ", "i").lower()
        if self.reply == "fatih sultan mehmet" or "fatih" or "fatih sultan":
            print("-"*50)
            print("Doğru Cevap...")
            self.point += 10
        else:
            print("-"*50)
            print("Yanlış Cavap...")

    def Guestion006(self):
        print("-"*50)
        print(self.question_06)
        print("-"*50)
        self.reply = input("Cevap: ")
        self.reply = self.reply.replace("Ğ", "ğ").replace("G", "ğ").lower()
        if self.reply == "otağ":
            print("-"*50)
            print("Doğru Cevap...")
            self.point += 10
        else:
            print("-"*50)
            print("Yanlış Cavap...")

    def Guestion007(self):
        print("-"*50)
        print(self.question_07)
        print("-"*50)
        self.reply = input("Cevap: ")
        self.reply = self.reply.replace("Ö", "ö").replace("İ", "i").lower()
        if self.reply == "köpek":
            print("-"*50)
            print("Doğru Cevap...")
            self.point += 10
        else:
            print("-"*50)
            print("Yanlış Cavap...")

    def Guestion008(self):
        print("-"*50)
        print(self.question_08)
        print("-"*50)
        self.reply = input("Cevap: ")
        self.reply = self.reply.replace("G", "g").replace("İ", "i").lower()
        if self.reply == "marmara bölgesi" or "marmara":
            print("-"*50)
            print("Doğru Cevap...")
            self.point += 10
        else:
            print("-"*50)
            print("Yanlış Cavap...")

    def Guestion009(self):
        print("-"*50)
        print(self.question_09)
        print("-"*50)
        self.reply = input("Cevap: ")
        self.reply = self.reply.replace("I", "ı").replace("İ", "i").lower()
        if self.reply == "imece":
            print("-"*50)
            print("Doğru Cevap...")
            self.point += 10
        else:
            print("-"*50)
            print("Yanlış Cavap...")

    def Guestion010(self):
        print("-"*50)
        print(self.question_10)
        print("-"*50)
        self.reply = input("Cevap: ")
        self.reply = self.reply.replace("I", "ı").replace("İ", "i").lower()
        if self.reply == "klibrevil":
            print("-"*50)
            print("Doğru Cevap...")
            self.point += 10
        else:
            print("-"*50)
            print("Yanlış Cavap...")
            print("-"*50)

        if self.point <= 50:
            print("""Üzgünüz Yarışmayı Kazanamadınız.\nToplam Puanınız: {}""".format(self.point))
        else:
            print("""Teprikler Yarışmayı Geçtiniz\nToplam Puanınız: {}""".format(self.point))

if __name__ == "__main__":
    while True:
        print("-"*50)
        print(" "*6 , "...BİLGİ YARIŞMASINA HOŞGELDİNİZ..."," "*7)
        print("-"*50)
        print("Bilgi Yarışmasına Başlamak İçin Lütfen 'Başla' diyiniz.")
        print("-"*50)
        Start = input("Cevap (Çıkış için 'q'): ")
        Start = Start.replace("Ş", "ş").replace("L", "l").lower()
        if Start == "q":
            break
        if Start == "başla":
            Quiz = Quiz()
            Quiz.Guestion001()
            Quiz.Guestion002()
            Quiz.Guestion003()
            Quiz.Guestion004()
            Quiz.Guestion005()
            Quiz.Guestion006()
            Quiz.Guestion007()
            Quiz.Guestion008()
            Quiz.Guestion009()
            Quiz.Guestion010()
