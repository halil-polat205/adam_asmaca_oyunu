import random 
import time
from modul import goster,X

adiniz = input("lütfen adınızı giriniz :")
print("merhaba " + adiniz + " seninle bir oyun oynayacağız")
print(adiniz,"lütfen oyun boyunca harfleri büyük yaz")

resim = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|  |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|  |
  /    |
       |
--------""","""
   +---+
   |   |
   O   |
  /|  |
  /   |
       |
--------"""]


kelimeler = ["ABANMAK" ,"ABARTIK", "ABARTIŞ", "ABARTMA","ABESLİK", "ABİDEVİ", "ABLAKÇA", 
"ABLALIK","ABLATYA", "ABONMAN" ,"ABORJİN","HABEŞİ", "HACKER", "HADEME", "HADİSE", "HAFIZA", "HAFİYE", 
"HAİNCE", "HAKEZA", "HAKİKİ", "HAKKAK", "HAKSIZ","HALEBİ", "HALHAL", "HALICI", "HALİFE", 
"HALİLE", "HALKÇI", "HALLAÇ", "HALSİZ", "HALTER", "HALVET"] 

kelime = random.choice(kelimeler)
tahmin_string = ""

can = 7

while can > 0:
    harf_left = 0

    for karakter in kelime:
        if karakter in tahmin_string:
            print(karakter)
        else:
            print("_")
            harf_left += 1

    if harf_left == 0:
        print("kazandınız")
        q=input("Tekrar oynamak ister misiniz?(E/H) : ")
                    
        if q=="E":
            print("öyleyse üst ok deyip enter a basınız")
            break      
        elif q=="H":
            print("tekrar bekleriz...")
            time.sleep(3)
            quit()
        else:
            print("lütfen e ve h giriniz!!!")
            quit()

    ziyaretci = input("lütfen harf girin :")
    tahmin_string += ziyaretci

    if ziyaretci not in kelime:
        can -= 1
        
        if can == 6:
            goster(resim,can,0)
            X(can,kelime)

        elif can ==5:
            goster(resim,can,1)
            X(can,kelime)

        elif can ==4:
            goster(resim,can,2)
            X(can,kelime)
        elif can ==3:
            goster(resim,can,3)
            X(can,kelime) 

        elif can ==2:
            goster(resim,can,4)
            X(can,kelime)

        elif can ==1:
            goster(resim,can,5)
            X(can,kelime)
        elif can ==0:
            goster(resim,can,6)
            print("Bulmaya çalıştığınız kelime ---> {} ".format(kelime))
            q=input("Tekrar oynamak ister misiniz?(E/H) : ")
            
            if q=="E":
                continue
            elif q=="H":
                print("tekrar bekleriz...")
                time.sleep(3)
                quit()
            else:
                print("lütfen e ve h giriniz!!!")
                quit()