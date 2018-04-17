import sys
# -*- coding: utf-8 -*-
# Yorum satırları '# ' işareti koyularak gerçekleştirilebilir

# Ekrana merhaba Python yazdırmak için print fonksiyonunu kullanıyoruz.

# Programı çaıştırmak için yukarıdaki yeşil run tuşuna basabilir veya sağ tuş ile tıklayarak run diyebiliriz.

print("Hello Python")

# help() yazarak bazı işlemler için bilgi edinebiliriz.

# help()
# help yazısı geldikten sonra console alanından help>modules yazarak var olan modülleri görüntüleyebiliriz.
# help>keywords bize kullanabileceğimiz bazı anahtar kelimeleri teslim eder.
# help>symbols bize kullanabileceğimiz bazı sembolleri gösterecektir.

# -----------------------Temel Veri Yapıları ------------------------------
# 1)Numbers
# 2)String
# 3)List
# 4)Tuple
# 5)Dictionary

# 1)---- Numbers ----

# Numbers => Sayısal değerler saklarlar.
# Örnek atama işlemi
var1 = 1
var2 = 10

print(var1,var2)

# "del" komutu ile sayı objesinin referansını silebiliriz.

# del var1
# print(var1)
#  Bu bize var1 değişkeninin tanımlı olmadığını hata ekranında gösterecektir.

# Birden fazla objeyi aynı anda silmek için virgül ile ayırabiliriz.
# "del var_a,var_b" yazabilirsiniz

# ---Python Sayıları---

# Not => Long ve int python 3.x ile birlikte aynı tip olarak görülmektedir. Bu nedenle sys.maxint komutu kaldırılmıştır.

# int => 10 , 100 , -781 , 232 , 1231 , -0x260
# long => Daha büyük tamsayılardır 534343L , 01231L , 23532357L
# Not : Long tipleri küçük "l" işaretiyle de gösterebiliriz ancak önerilmez çünkü 1 sayısı ile karışabilmektedir.
# float => Ondalıklı sayılardır. => 12.20 , -122,67 , 998,1231
# complex => Bazı matematiksel işlemler için kullanılan kompleks veri tipidir. 21.23j , 23.j , -.123+0J  gibi değerler tutabilir.

print(sys.maxsize) # => platformumuzdaki pointer'ın limitini gösterir. sistemimize bağlı olarak değişebilecek olan bu sayının üstüne çıkıldığı anda değerler donanım tarafında değil yazılım tarafında işleme alınacaktır.


# --Python Stringleri---

param = 'Bilge Adam'

print(param)

print(param[0]) # Ekrana ilk karakteri basacaktır


print(param[0:5]) # Ekrana 0-5 aralığındaki karakterleri basacaktır

print(param * 4) # Ekrana 4 kez Bilge Adam yazacaktır

print(param + " Akademi") # Ekrana Bilge Adam Akademi yazacaktır





# ------------------------Değişken Tanımlamaları--------------------------


# Değişken isimlendirmeleri A-Z ile veya a-z ile başlayabilir. Bunun yanında '_' işareti ile de değişken tanımlamaya başlayabliriz.

# Kullanılamayacak Kelimeler => Bu kelimeler özel tanımlıdırlar ve değişken ismi olamazlar.

# and	exec	not
# assert	finally	or
# break	for	pass
# class	from	print
# continue	global	raise
# def	if	return
# del	import	try
# elif	in	while
# else	is	with
# except	lambda	yield

# Python içerisinde {} 'bracket' sistemi yoktur. Yazılan kod satırlarda bırakılan boşluk miktarı ile belirlenir.

# Aynı miktarda bırakılan boşluklar bir blok oluşturacaktır. Bu nedenle C# gibi dillerden farklı olarak bıraktığımız boşluk miktarına dikkat etmeliyiz.

# Değişkenler memory içerisinde ayrılan alanlardan daha fazlası değildir. değişkenin tipine göre memory içerisinde verileriniz için belli miktar yer ayrılacaktır.

# Python dilinde değişkenleri explicit bir belirtmesi yoktur. İçine bir değer ataması gerçekleştirildiğinde tanımlama otomatik olarak gerçekleştirilir.

counter = 100 # Integer ataması gerçekleşir.
miles = 1000.0 # Float tipinde atama gerçekleşir.
name = "Can" # String ataması gerçekleşir.

print(counter)

print(miles)

print(name)

# Print ile değerleri ekrana bastırıyoruz.

# Bir değeri birçok değişkene tanımlamak için =>

a = b = c = 1
# Üstteki yöntemle integer objesi oluşturulur ve değer 1 olarak atanır.Bu yöntemle üç değişkenimiz de aynı memory lokasyonundadır.

# Farklı değerler atamak için
a,b,c = 1,2,"Can"

print(a,b,c)


