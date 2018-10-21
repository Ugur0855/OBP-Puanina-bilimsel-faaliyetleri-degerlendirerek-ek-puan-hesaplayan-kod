"""İnfo
Created on Frı Oct 19 21:44:38 2018

@author: Ugur
"""

'''Algoritma

-----OBP Puanına, bilimsel faaliyetleri değerlendirerek ek puanı hesaplayan kod-----

Diploma Notu                                             =input();
İlk 3'girildi mi?(Evet/Hayır)                            =input();
Yarışmanın düzeyi(U:Ulusal, D:Uluslararası)              =input();
Yarışmanın türü(O:Bilim Olimpiyatı, P:Proje Yarışması)   =input();
Derece(1/2/3)                                            =input();

-----Diploma Puanı-----
OBP=Diploma Puanı*5

------OBP(Ek puan hesaplamaları)-----
Uluslararası / Bilim Olimpiyatı   / 1 ise = ek_puan=OBP*0.18
Uluslararası / Bilim Olimpiyatı   / 2 ise = ek_puan=OBP*0.17
Uluslararası / Bilim Olimpiyatı   / 3 ise = ek_puan=OBP*0.16

Ulusal       / Bilim Olimpiyatları/ 1 + Uluslararası / Proje/ 1 = ek_puan=OBP*0.155
Ulusal       / Bilim Olimpiyatları/ 1 + Uluslararası / Proje/ 2 = ek_puan=OBP*0.150
Ulusal       / Bilim Olimpiyatları/ 1 + Uluslararası / Proje/ 3 = ek_puan=OBP*0.145

Ulusal       / Proje Yarışması/     1 ise = ek_puan=OBP*0.14
Ulusal       / Proje Yarışması/     2 ise = ek_puan=OBP*0.135
Ulusal       / Proje Yarışması/     3 ise = ek_puan=OBP*0.13

#Ek puan     =yazdır();

'''

import sys
import os

print("-----OBP Puanına, bilimsel faaliyetleri değerlendirerek ek puanı hesaplayan kod-----")


dip_not=0.0
ilk_uc=' '
duzey=' '
tur=' '
derece=0
OBP=0.0
ek_puan=0.0

dip_not= float(input("Diploma notunuzu(100 üzerinden) giriniz: "))
OBP=dip_not*5
ilk_uc =str(input("Bilimsel yarışmalarda ilk üçe girdiniz mi?(E/H): "))

if(ilk_uc=="E"):
    duzey=str(input("Yarışmanın düzeyini giriniz (U:ulusal, D:uluslararası): "))
    tur=str(input("Yarışmanın türünü giriniz (O:bilim olimpiyatı, P:proje yarışması): "))
    derece=int(input("Derecenizi giriniz (1/2/3): "))

if(duzey=="D" and tur=="O"):
    if(derece==1):
       ek_puan=OBP*0.18  
    elif(derece==2):
       ek_puan=OBP*0.17
    elif(derece==3):
       ek_puan=OBP*0.16

if((duzey=="U" and tur=="O") or (duzey=="D" and tur=="P")):
    if(derece==1):
       ek_puan=OBP*0.155
    elif(derece==2):
       ek_puan=OBP*0.150
    elif(derece==3):
        ek_puan=OBP*0.145

if(duzey=="U" and tur=="P"):
    if(derece==1):
       ek_puan=OBP*0.14
    elif(derece==2):
       ek_puan=OBP*0.135
    elif(derece==3):
       ek_puan=OBP*0.130


print("---------------------------------------------------")
print("Kazanacağınız toplam ek puan miktarı: " + format(ek_puan,".5f"))

