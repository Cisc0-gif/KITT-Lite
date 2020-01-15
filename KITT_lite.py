#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# @name   : KITT Lite - Lite Version of KITT Framework
# @url    : https://github.com/Cisc0-gif
# @author : Cisc0-gif
import os
import time
import socket
import requests
import sys
import random

def wait():
  wait = input('PRESS ENTER TO CONTINUE')

def runtimecheck(): #returns current runtime
  global check
  check = time.time()
  msg = str(check - start)
  return msg

def timecheck(): #returns current local time
  return time.ctime()

def logwrite(msg): #writes input to RUNTIME.log
  with open('/opt/KITT-Lite/RUNTIME.log', 'a+') as f:
    f.write(msg + '\n')
    f.close()

if len(sys.argv) != 2 or '--help' in sys.argv:
  print('KITT Lite v1.0 Python-Based Pentesting Framework')
  print('Sourced on Github and created by Cisc0-gif, Ecorp7@protonmail.com\n')
  print('        ./KITT_lite.py --help for this menu')
  print('OSINT:')
  print('        -ds, --domainsticate                 Extensive Domain Enumeration')
  print('        -sh, --shodan_search                 Search for IP info on shodan')
  print('        -pi, --phone_infoga                  Search for Phone # info ')
  print('PrivEsc:')
  print('        -pe, --escalate                      SimpleHTTPServer w/ PrivEsc scripts on port 80')
  print('Network Cracking:')
  print('        -nc, --netcrack                      Network Cracking Tool Suite')
  print('        -ap, --apspoof                       AP Spoofing Tool')
  print('        -pd, --packdump                      Packet Capture Tool')
  print('IoT Exploitation:')
  print('        -hp, --homepwn                       IoT Exploit Tool Suite')
  print('        -pb, --pentbox                       HoneyPot Tool Suite')
  print('        -st, --btspoof                       BT Spoofer')
  print('        -bv, --btverify                      Rfcomm Channel Verifier')
  print('        -bs, --bluescan                      BT Port/MAC Scanner')
  print('Hardware Hacking:')
  print('        -mj, --mousejack                     Intel Keyboard/Mice Hijacker')
  print('        -gp, --gpioctl                       GPIO Controller (Only for RPi)')
  print('System Security:')
  print('        -sp, --sshportrand                   SSH Port Randomizer')
  print('        -sc, --sshautoconfig                 SSHD Config Buff')
  print('        -pc, --proxyconfig                   ProxyChains Config')
  print('        -fb, --fail2ban                      Fail2ban IP Jail Config')
  print('        -di, --dhcpip                        DHCP IP Receiver')
  print('Update Tool:')
  print('        -up, --update                        Update packages and git source for KITTlite')
  print('Example:')
  print('        KITTlite --netcrack')
  sys.exit(1)

short = ['-ds', '-sh', '-pi', '-pe', '-nc', '-ap', '-pd', '-hp', '-pb', '-st', '-bv', '-bs', '-mj', '-gp', '-sp', '-sc', '-pc', '-fb', '-di', '-up']
long = ['--domainsticate', '--shodan_search', '--phone_infoga', '--escalate', '--netcrack', '--apspoof', '--packdump', '--homepwn', '--pentbox', '--btspoof', '--btverify', '--bluescan', '--mousejack', '--gpioctl', '--sshportrand', '--sshautoconfig', '--proxyconfig', '--fail2ban', '--dhcpip', '--update']

tool = sys.argv[1]

os.chdir('/opt/KITT-Lite')
  
def gohome():
  os.chdir('/opt/KITT-Lite')
  
if tool == '-ds' or tool == '--domainsticate':
  try:
    os.chdir('hg')
    os.system('python3 domain_sticate.py')
    logwrite('--[+]Successfully ran domainsticate @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running domainsticate @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-sh' or tool == '--shodan_search':
  try:
    os.system('python3 shodan_search.py')
    logwrite('--[+]Successfully ran shodan_search @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running shodan_search @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-pi' or tool == '--phone_infoga':
  try:
    os.chdir('PhoneInfoga')
    os.system('python3 phoneinfoga.py')
    logwrite('--[+]Successfully ran phone_infoga @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error runnning phone_infoga @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-pe' or tool == '--escalate':
  try:
    os.chdir('escalate')
    print('[*]Starting python SimpleHTTPServer on Port 80 to curl payloads')
    print('[*]Enter ^C or ^Z To Stop HTTP Server...')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    r = requests.get("http://ifconfig.me").text
    print('[*]Private IP: ' + str(s.getsockname()[0]))
    print('[*]Public IP: ' + str(r))
    os.system("python -m SimpleHTTPServer 80")
    s.close()
    logwrite('--[*]Successfully ended SimpleHTTPServer @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running SimpleHTTPServer @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-nc' or tool == '--netcrack':
  try:
    os.system('python3 network_crack.py')
    logwrite('--[+]Successfully ran network_crack @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running network_crack @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-ap' or tool == '--apspoof':
  try:
    os.chdir('AP_Spoof')
    os.system('bash setup.sh')
    logwrite('--[+]Successfully ran AP_Spoof setup.sh @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running AP_Spoof setup.sh @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-pd' or tool == '--packdump':
  try:
    os.system('bash packetdump.sh')
    logwrite('--[+]Successfully ran packetdump.sh @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running packetdump.sh @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-hp' or tool == '--homepwn':
  try:
    os.chdir('HomePWN')
    os.system('python3 homePwn.py')
    logwrite('--[+]Successfully ran HomePWN @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running HomePWN @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-pb' or tool == '--pentbox':
  try:
    os.chdir('pentbox/pentbox-1.8')
    os.system('ruby pentbox.rb')
    logwrite('--[+]Successfully ran pentbox @ ' + timecheck() + '--')
  except:
    logwrite('--[+]Error running pentbox @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-st' or tool == '--btspoof':
  try:
    os.system('bash bluespoof.sh')
    logwrite('--[+]Successfully ran bluespoof @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running bluespoof @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-bv' or tool == '--btverify':
  try:
    os.system('python3 btverifier.py')
    logwrite('--[+]Successfully ran btverifier @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running btverifier @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-bs' or tool == '--bluescan':
  try:
    os.system('bash BlueScan.sh')
    logwrite('--[+]Successfully ran BlueScan @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running BlueScan @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-mj' or tool == '--mousejack':
  moj = input("[*]Do you want to initialize a [m]ousejack device or scan with [j]ackit?: ")
  if moj == 'M' or moj == 'm':
    try:
      print("[*]Insert CrazyRadio PA device...")
      wait()
      os.chdir('mousejack/nrf-research-firmware')
      os.system('sudo make')
      os.system('sudo make install')
      os.system('dmesg')
      print("[+]Firmware Uploaded!")
      logwrite('--[+]Successfully uploaded mousejack firmware to CrazyRadio PA @ ' + timecheck() + '--')
    except:
      print("[*]Failed to upload Firmware!")
      logwrite('--[*]Failed to upload mouesjack firmware to CrazyRadio PA @ ' + timecheck() + '--')
  elif moj == 'J' or moj == 'j':
    try:
      print("[*]Insert CrazyRadio PA device w/ mousejack firmware...")
      wait()
      os.system('jackit')
      print('[+]Scan complete!')
      logwrite('--[+]Successfully ended jackit scan @ ' + timecheck() + '--')
    except:
      print("[*]Error scanning with jackit")
      logwrite('--[*]Error scanning with jackit @ ' + timecheck() + '--')
      wait()
  else:
    print("[*]Not an option!")
    time.sleep(2)
  gohome()
  exit()

if tool == '-gp' or tool == '--gpioctl':
  try:
    os.system('python3 GPIO_CTL.py')
    logwrite('--[+]Successfully ran GPIO_CTL @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running GPIO_CTL @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-sp' or tool == '--sshportrand':
  try:
    os.chdir('sdefense')
    os.system('bash ssh_randomizer.sh')
    logwrite('--[+]Successfully ran ssh_randomizer @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running ssh_randomizer @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-sc' or tool == '--sshautoconfig':
  try:
    os.chdir('sdefense')
    os.system('bash ssh_encr7pt.sh')
    logwrite('--[+]Successfully ran ssh_encr7pt @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running ssh_encr7pt @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-pc' or tool == '--proxyconfig':
  try:
    os.chdir('sdefense')
    os.system('bash proxy_config.sh')
    logwrite('--[+]Successfully ran proxy_config @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running proxy_config @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-fb' or tool == '--fail2ban':
  try:
    ipbu = input('[*]Are you going to [B]an or [U]nban an IP?: ')
    if ipbu == 'B' or ipbu == 'b':
      ip = input('[*]Enter IP: ')
      os.system('sudo fail2ban-client set sshd banip ' + ip)
      print('[+]Banned IP ' + ip + '!')
      logwrite('--[+]Banned IP ' + ip + ' @ ' + timecheck() + '--')
    else:
      ip = input('[*]Enter IP: ')
      os.system('sudo fail2ban-client set sshd unbanip ' + ip)
      print('[+]Unbanned IP ' + ip + '!')
      logwrite('--[+]Unbanned IP ' + ip + ' @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error configuring fail2ban @ ' + timecheck() + '--')
    print('[*]Error configuring fail2ban')
  gohome()
  exit()

if tool == '-di' or tool == '--dhcpip':
  try:
    os.chdir('sdefense')
    os.system('bash dh_recv.sh')
    logwrite('--[+]Successfully ran dh_recv @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running dh_recv @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-up' or tool == '--update':
  try:
    print('Updating and Upgrading Packages...')
    os.system('sudo apt-get update && sudo apt-get upgrade')
    print('Updating git source for KITTlite')
    os.system('sudo git pull origin master')
    logwrite('--[+]Successfully updated packages and git source @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error updating packages and git source @ ' + timecheck() + '--')
  gohome()
  exit()

if tool not in short or tool not in long:
  print(sys.argv[1] + ' not an option!')
