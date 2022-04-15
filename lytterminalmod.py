import platform
import os
import sys
import shutil #pip install shutil
os.system("clear")
print("""\033[92m
 _                __            _     __  __           _ 
| |    ___  __ _ / _|_   _  ___| |_  |  \/  | ___   __| |
| |   / _ \/ _` | |_| | | |/ _ \ __| | |\/| |/ _ \ / _` |
| |__|  __/ (_| |  _| |_| |  __/ |_  | |  | | (_) | (_| |
|_____\___|\__,_|_|  \__, |\___|\__| |_|  |_|\___/ \__,_|
                     |___/      
\033[0m    
""")
leafyetmod=0
while(leafyetmod<1):
	try:
		komut = input("\033[94mlyt:\033[0m")

		if(komut=="sil"):
			silinecekdosya = input("")
			os.remove(silinecekdosya)
		if(komut=="ldizin"):
			dosya = input("")
			os.mkdir(dosya)
		if(komut=="rdizin"):
			dosya = input("")
			shutil.rmtree(dosya)
		if(komut=="lstat"):
			dosya = input("")
			os.stat(dosya)
		if(komut=="lpy"):
			dosya = input("")
			os.system("python3 "+dosya)
		if(komut=="los"):
			print(""+os.name)
			print("Sistem:"+platform.system())
			print("Sistem ismi:"+platform.node())
			print("İşletim sistemi:"+platform.platform())
			print("Bit:"+platform.machine())
		if(komut=="lrname"):
			dosya = input("Dosya ismi ve uzantısını giriniz:")
			hedef=input("Yeni isim ve uzantı giriniz:")
			os.replace(dosya,hedef)
		if(komut=="çık" or komut=="cik"):
			print("\033[92mGörüşmek üzere!")
			leafyetmod+=1
		if(komut=="list"):
			print(os.listdir('.'))
		if(komut=="oku"):
			dosya = input("")
			yazilmis = open(dosya)	
			print(yazilmis.read())
		if(komut=="lcopy"):
			dosya = input("Dosya ismi ve uzantısını giriniz:")
			hedef=input("Kopya için isim ve uzantı giriniz:")
			shutil.copy(dosya,hedef)
		if(komut=="lmove"):
			dosya = input("Dosya ismi ve uzantısını giriniz:")
			hedef=input("Taşınacak yer:")
			shutil.move(dosya,hedef)
		if(komut=="ekle"):
			dosya2 = input("")
			dosya = open(dosya2,"a")
			dosya.close()

	except:
		print("Geçersiz komut!")



