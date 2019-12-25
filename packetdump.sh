#! /bin/bash
figlet -f slant 'tcpdump'
echo '===================================================='
echo 'Enter CTRL +C to stop packet capture'
tcpdump -w output.pcap 

