#! /bin/bash

sudo sysctl -w net.ipv4.ip_forward=0
sudo iptables -P FORWARD DROP
sudo iptables --table nat -A POSTROUTING -o wlan0 -j MASQUERADE
sudo service dnsmasq stop
sudo service hostapd stop
sudo service sshd restart
ps aux | grep dnsmasq
echo '[*]Kill dnsmasq ps if still running'
