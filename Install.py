import os
hd=lambda: os.system('apt-get install hostapd dnsmasq -y')
print("***********************************")
print("Hostapd ve Dnsmasq Yükleniyor..")
print("***********************************")
hd()
