#! /bin/bash

figlet -f slant "DHCP_RECEIVE"
echo ====================================
read -p "Enter adapter name: " adap
dhclient $adao
echo "DHCP IP Received!"