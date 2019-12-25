#! /bin/bash

figlet -f slant 'BlueSp00f'
echo =====================================
sudo hciconfig hci0 down
sudo hciconfig hci0 up
sudo btscanner
read -p 'Enter device MAC to spoof: ' mac
read -p 'Enter device name to spoof: ' name
spooftooph -i hci0 -a $mac -n $name
