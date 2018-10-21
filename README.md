OBP Puanına, bilimsel faaliyetleri değerlendirerek ek puanı hesaplayan kod

Algoritma--

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
