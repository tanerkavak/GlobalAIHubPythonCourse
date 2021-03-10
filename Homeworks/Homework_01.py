import random

list_cift = [i for i in range(0,2021) if i%2 == 0] #Çift Sayı Dizisi
list_tek = [i for i in range(0,2021) if i%2 == 1]  #Tek Sayı Dizisi


#Her Listeden Rasgele 10 Tane Sayı Alınır ve Birleştirilir.
merge_list = random.sample(list_cift,10) + random.sample(list_tek,10)


#Listedeki Her Sayı 2 İle Çarpılır ve my_list'ye Ekler.
my_list = []
for crp in merge_list:
    my_list.append(crp * 2)


#Listedeki Her Sayı, Tipiyle Birlikte Yazılır.
for i in my_list:
    print(f"{i} değerinin tipi: {type(i)}")
