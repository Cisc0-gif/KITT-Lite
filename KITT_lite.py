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

username = os.getlogin()

print('[*]Current User: ' + username)

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
  print('        -pi, --phone_infoga                  Search for Phone # info')
  print('        -ka, --katana                        Google Dork Scanner')
  print('        -td, --tidos                         WebApp Pentesting Framework')
  print('        -wk, --webkiller                     Domain OSINT Tool')
  print('        -bm, --badmod                        Website Scanner & Auto Exploiter')
  print('        -w3, --w3af                          WebApp Security Scanner')
  print('        -ur, --userrecon                     Social Media Username Search')
  print('        -ti, --th3inspector                  Full Stack OSINT Tool')
  print('        /opt/KITT-Lite/vulnx/                WebApp Bot Auto Shell Injector')
  print('        /opt/KITT-Lite/gitGraber/            Search for Unprotected AWS Tokens')
  print('        /opt/KITT-Lite/deep-explorer/        Tor Browser')
  print('        /opt/KITT-Lite/BlackDir-Framework    WebApp Vulnerability Scanner')
  print('        /opt/KITT-Lite/Konan                 Advanced WebApp Dir Scanner')
  print('        /opt/KITT-Lite/Pompem                Exploit/Vulnerability Search Tool')
  print('      /opt/KITT-Lite/Fast-Google-Dorks-Scan  Website Dork Enumeration Script')
  print('Cracking:')
  print('        -tb, --ftpbruter                     FTP Login Brute Forcer')
  print('        /opt/KITT-Lite/hate_crack/           Automated Hashcat Cracker')
  print('        /opt/KITT-Lite/tangalanga/build      Zoom Token Bruteforcer')
  print('        /opt/KITT-Lite/Zip-Cracker-          Password Protected Zip File Bruteforcer')
  print('Phising:')
  print('        -be, --blackeye                      Tool for Hosting Phishing Sites')
  print('        -st, --set                           Social Engineering Toolkit (SET)')
  print('        -sb, --socialbox                     Social Media Password Bruteforcer')
  print('        -bd, --brutedum                      Common Protocol Bruteforcer')
  print('        -sy, --saycheese                     Takes Webcam shots on link visit')
  print('        -si, --shellphish                    Blackeye w/ Automated Ngrok')
  print('        -np, --nexphisher                    Tool for Hosting Phishing Sites')
  print('        -lp, --lockphish                     Lock Screen Phishing Tool (iPhone/Android Notifications)')
  print('        -sf, --socialfish                    Common Fishing Tool')
  print('        -lc, --locator                       Geolocator and IP Tracker')
  print('        -ep, --evilapp                       MiTM Phishing Attack Using APK')
  print('        -df, --droidfiles                    Android File Downloader Using APK')
  print('        -ci, --cuteit                        IP Obfuscator')
  print('        /opt/KITT-Lite/seeker                Social Engineering IP GeoLocator (Give/Take 30m)')
  print('        /opt/KITT-Lite/trevorc2              Cmd Injection Masked Phishing Site')
  print('Payloads:')
  print('        -ed, --evildroid                     Android APK Payloading & Embedding Framework')
  print('        -cy, --catchyou                      Undetectable Win32 Payload Generator')
  print('        -ws, --winspy                        Win Reverse Shell Generator w/ IP Poisoning')
  print('        -er, --evilreg                       Windows .reg Reverse Shell Generator')
  print('        -bl, --badlnk                        Shortcut (.lnk) Reverse Shell Generator')
  print('        -ea, --enigma                        Multiplatform Payload Dropper')
  print('        -af, --avetfabric                    Windows AV Evasive Payloader')
  print('        -vp, --evilpdf                       Embeds .exe Files into PDF Documents')
  print('        -el, --evildll                       DLL Reverse Shell Generator')
  print('        -dt, --droidtracker                  Android .APK Location Tracker')
  print('        -mc, --hmmcookies                    Grabs Firefox, Chrome, and Opera browser cookies')
  print('        /opt/KITT-Lite/eviloffice            Injects Macro & DDE Code into Excel & Word Documents (WINDOWS)')
  print('Keyloggers: ')
  print('        -hk, --herakeylogger                 Chrome Keylogger Extension')
  print('        /opt/KITT-Lite/KatroLogger           Unix/Linux Keylogger')
  print('PrivEsc:')
  print('        -pe, --escalate                      SimpleHTTPServer w/ PrivEsc scripts on port 80')
  print('        -lv, --leviathan                     System Audit Toolkit')
  print('        -iy, --ispy                          EternalBlue/Bluekeep Scanner/Exploiter')
  print('        -nt, --nekobot                       Auto Exploiter Tool')
  print('        -lt, --lstools                       Lists all tools hosts on --escalate')
  print('Ransomeware:')
  print('        -hc, --hiddencry                     Windows AES 256 Bit Encrypter/Decrypter')
  print('        -cd, --crydroid                      Android Encrypter/Decrypter')
  print('Bots:')
  print('        /opt/KITT-Lite/Idisagree             Trojan Discord Bot')
  print('        /opt/KITT-Lite/ufonet                DDoS 3rd Party Vector Tool')
  print('Network Cracking:')
  print('        -nc, --netcrack                      Network Cracking Tool Suite')
  print('        -ap, --apspoof                       AP Spoofing Tool')
  print('        -pd, --packdump                      Packet Capture Tool')
  print('        -wp, --wifipumpkin                   Network Cracking Framework')
  print('        -pb, --pentbox                       HoneyPot Tool Suite')
  print('        -ps, --pwnstar                       Fake AP Tool Framework')
  print('IoT Exploitation:')
  print('        -hp, --homepwn                       IoT Exploit Tool Suite')
  print('        -bt, --btspoof                       BT Spoofer')
  print('        -bv, --btverify                      Rfcomm Channel Verifier')
  print('        -bs, --bluescan                      BT Port/MAC Scanner')
  print('Hardware Hacking:')
  print('        -mj, --mousejack                     Intel Keyboard/Mice Hijacker')
  print('        -gp, --gpioctl                       GPIO Controller (Only for RPi)')
  print('        -br, --brutal                        RubberDucky Payload Generator (Teensy, Digispark, Ardu Leo, Ardu Pro Micro)')
  print('System Security:')
  print('        -sn, --snort                         Snort NIDS')
  print('        -sp, --sshportrand                   SSH Port Randomizer')
  print('        -sc, --sshautoconfig                 SSHD Config Buff')
  print('        -pc, --proxyconfig                   ProxyChains Config')
  print('        -fb, --fail2ban                      Fail2ban IP Jail Config')
  print('        -di, --dhcpip                        DHCP IP Receiver')
  print('        /opt/KITT-Lite/SysIntegrity          File MD5sum Integrity Analyzer (dont run as root)')
  print('        /opt/KITT-Lite/wotop/                Tunnels Traffic Over HTTP ')
  print('        /opt/KITT-Lite/TorghostNG            Filters All Traffic Through Tor Proxy') 
  print('Update Tool:')
  print('        -up, --update                        Update packages and git source for KITTlite')
  print('        -pf, --ptf                           PenTesting Framework for Installing and Updating Tools')
  print('        -tx, --toolx                         PenTesting Tool Installer')
  print('Example:')
  print('        KITTlite --netcrack')
  sys.exit(1)

short = ['-ds', '-sh', '-pi', '-pe', '-nc', '-ap', '-pd', '-hp', '-pb', '-bt', '-bv', '-bs', '-mj', '-gp', '-sp', '-sc', '-pc', '-fb', '-di', '-up', '-be', '-st', '-ka', '-sb', '-td', '-pf', '-ps', '-bd', '-tx', '-br', '-wk', '-ed', '-cy', '-sy', '-bm', '-si', '-lt', '-np', '-w3', '-ur', '-ws', '-ti', '-wp', '-lp', '-er', '-bl', '-sf', '-hk', '-lc', '-ep', '-lv', '-hc', '-df', '-af', '-sn', '-iy', '-nt', '-ci', '-tb', '-cd', '-vp', '-el', '-dt', '-mc']
long = ['--domainsticate', '--shodan_search', '--phone_infoga', '--escalate', '--netcrack', '--apspoof', '--packdump', '--homepwn', '--pentbox', '--btspoof', '--btverify', '--bluescan', '--mousejack', '--gpioctl', '--sshportrand', '--sshautoconfig', '--proxyconfig', '--fail2ban', '--dhcpip', '--update', '--blackeye', '--set', '--katana', '--socialbox', '--tidos', '--ptf', '--pwnstar', '--brutedum', '--toolx', '--brutal', '--webkiller', '--evildroid', '--catchyou', '--saycheese', '--badmod', '--shellphish', '--lstools', '--nexphisher', '--w3af', '--userrecon', '--winspy', '--th3inspector', '--wifipumpkin', '--lockphish', '--evilreg', '--badlnk', '--socialfish', '--herakeylogger', '--locator', '--evilapp', '--leviathan', '--hiddencry', '--droidfiles', '--avetfabric', '--snort', '--ispy', '--nekobot', '--cuteit', '--ftpbruter', '--crydroid', '--evilpdf', '--evilpdf', '--droidtracker', '--hmmcookies']

tool = sys.argv[1]

os.chdir('/opt/KITT-Lite')

def gohome():
  os.chdir('/opt/KITT-Lite')
  
if tool == '-ds' or tool == '--domainsticate':
  try:
    os.chdir('hg')
    os.system('sudo python3 domain_sticate.py')
    logwrite('--[+]Successfully ran domainsticate @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running domainsticate @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-sh' or tool == '--shodan_search':
  try:
    os.system('sudo python3 shodan_search.py')
    logwrite('--[+]Successfully ran shodan_search @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running shodan_search @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-pi' or tool == '--phone_infoga':
  try:
    os.chdir('PhoneInfoga')
    os.system('sudo python3 phoneinfoga.py')
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
    os.system("sudo python -m SimpleHTTPServer 80")
    s.close()
    logwrite('--[*]Successfully ended SimpleHTTPServer @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running SimpleHTTPServer @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-nc' or tool == '--netcrack':
  try:
    os.system('sudo python3 network_crack.py')
    logwrite('--[+]Successfully ran network_crack @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running network_crack @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-ap' or tool == '--apspoof':
  try:
    os.chdir('AP_Spoof')
    os.system('sudo bash setup.sh')
    logwrite('--[+]Successfully ran AP_Spoof setup.sh @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running AP_Spoof setup.sh @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-pd' or tool == '--packdump':
  try:
    os.system('sudo bash packetdump.sh')
    logwrite('--[+]Successfully ran packetdump.sh @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running packetdump.sh @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-hp' or tool == '--homepwn':
  try:
    os.chdir('HomePWN')
    os.system('sudo python3 homePwn.py')
    logwrite('--[+]Successfully ran HomePWN @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running HomePWN @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-pb' or tool == '--pentbox':
  try:
    os.chdir('pentbox/pentbox-1.8')
    os.system('sudo ruby pentbox.rb')
    logwrite('--[+]Successfully ran pentbox @ ' + timecheck() + '--')
  except:
    logwrite('--[+]Error running pentbox @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-bt' or tool == '--btspoof':
  try:
    os.system('sudo bash bluespoof.sh')
    logwrite('--[+]Successfully ran bluespoof @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running bluespoof @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-bv' or tool == '--btverify':
  try:
    os.system('sudo python3 btverifier.py')
    logwrite('--[+]Successfully ran btverifier @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running btverifier @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-bs' or tool == '--bluescan':
  try:
    os.system('sudo bash BlueScan.sh')
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
      os.system('sudo dmesg')
      print("[+]Firmware Uploaded!")
      logwrite('--[+]Successfully uploaded mousejack firmware to CrazyRadio PA @ ' + timecheck() + '--')
    except:
      print("[*]Failed to upload Firmware!")
      logwrite('--[*]Failed to upload mouesjack firmware to CrazyRadio PA @ ' + timecheck() + '--')
  elif moj == 'J' or moj == 'j':
    try:
      print("[*]Insert CrazyRadio PA device w/ mousejack firmware...")
      wait()
      os.system('sudo jackit')
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
    os.system('sudo python3 GPIO_CTL.py')
    logwrite('--[+]Successfully ran GPIO_CTL @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running GPIO_CTL @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-sp' or tool == '--sshportrand':
  try:
    os.chdir('sdefense')
    os.system('sudo bash ssh_randomizer.sh')
    logwrite('--[+]Successfully ran ssh_randomizer @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running ssh_randomizer @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-sc' or tool == '--sshautoconfig':
  try:
    os.chdir('sdefense')
    os.system('sudo bash ssh_encr7pt.sh')
    logwrite('--[+]Successfully ran ssh_encr7pt @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running ssh_encr7pt @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-pc' or tool == '--proxyconfig':
  try:
    os.chdir('sdefense')
    os.system('sudo bash proxy_config.sh')
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
    os.system('sudo bash dh_recv.sh')
    logwrite('--[+]Successfully ran dh_recv @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running dh_recv @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-be' or tool == '--blackeye':
  try:
    os.chdir('phishing/blackeye')
    os.system('sudo bash blackeye.sh')
    logwrite('--[+]Successfully ran blackeye @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running blackeye @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-st' or tool == '--set':
  try:
    os.chdir('phishing/SET')
    os.system('sudo python3 setoolkit')
    logwrite('--[+]Successfully ran SET @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running SET @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-ka' or tool == '--katana':
  try:
    os.chdir('Katana')
    os.system('sudo python3 kds.py')
    logwrite('--[+]Successfully ran Katana @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running Katana @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-sb' or tool == '--socialbox':
  try:
    os.chdir('SocialBox')
    os.system('sudo ./SocialBox.sh')
    logwrite('--[+]Successfully ran SocialBox @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running SocialBox @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-td' or tool == '--tidos':
  try:
    os.chdir("TIDoS-Framework")
    os.system("sudo tidos")
    logwrite("--[+]Successfully ran Tidos-Framework @ " + timecheck() + '--')
  except:
    logwrite("--[*]Error running Tidos-Framework @ " + timecheck() + '--')
  gohome()
  exit()

if tool == '-up' or tool == '--update':
  try:
    print('Updating and Upgrading Packages...')
    os.system('sudo apt-get update && sudo apt-get upgrade')
    print('Updating git source for KITTlite...')
    os.system('sudo git pull origin master')
    print('Making sure all repos are caught up...')
    os.system('sudo ./catchup.sh')
    wait()
    logwrite('--[+]Successfully updated packages and git source @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error updating packages and git source @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-pf' or tool == '--ptf':
  try:
    os.chdir('ptf')
    os.system('sudo ./ptf')
    logwrite('--[+]Successfully ran ptf @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running ptf @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-ps' or tool == '--pwnstar':
  try:
    os.chdir('PwnSTAR')
    os.system('sudo ./pwnstar')
    logwrite("--[+]Successfully ran pwnstar @ " + timecheck() + '--')
  except:
    logwrite('--[*]Error running pwnstar @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-bd' or tool == '--brutedum':
  try:
    os.chdir('BruteDum')
    os.system('sudo python3 brutedum.py')
    logwrite("--[+]Successfully ran brutedum @ " + timecheck() + '--')
  except:
    logwrite('--[*]Error running brutedum @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-tx' or tool == '--toolx':
  try:
    os.chdir('Tool-X')
    os.system('sudo toolx')
    logwrite("--[+]Successfully ran toolx @ " + timecheck() + '--')
  except:
    logwrite('--[*]Error running toolx @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-br' or tool == '--brutal':
  try:
    os.chdir('Brutal')
    os.system('sudo ./Brutal.sh')
    logwrite("--[+]Successfully ran brutal @ " + timecheck() + '--')
  except:
    logwrite("--[*]Error running brutal @ " + timecheck() + '--')
  gohome()
  exit()

if tool == '-wk' or tool == '--webkiller':
  try:
    os.chdir('webkiller')
    os.system('sudo python3 webkiller.py')
    logwrite("--[+]Successfully ran webkiller @ " + timecheck() + '--')
  except:
    logwrite("--[*]Error running brutal @ " + timecheck() + '--')
  gohome()
  exit()

if tool == '-ed' or tool == '--evildroid':
  try:
    os.chdir('Evil-Droid')
    os.system('sudo ./evil-droid')
    logwrite("--[+]Successfully ran evil-droid @ " + timecheck() + '--')
  except:
    logwrite("--[*]Error running evil-droid @ " + timecheck() + '--')
  gohome()
  exit()

if tool == '-cy' or tool == '--catchyou':
  try:
    os.chdir('catchyou')
    os.system('sudo ./catchyou.sh')
    logwrite("--[+]Successfully ran catchyou @ " + timecheck() + '--')
  except:
    logwrite("--[*]Error running catchyou @ " + timecheck() + '--')
  gohome()
  exit()

if tool == '-sy' or tool == '--saycheese':
  try:
    os.chdir('saycheese')
    os.system('sudo ./saycheese.sh')
    logwrite("--[+]Successfully ran saycheese @ " + timecheck() + '--')
  except:
    logwrite("--[*]Error running saycheese @ " + timecheck() + '--')
  gohome()
  exit()

if tool == '-bm' or tool == '--badmod':
  try:
    os.system('sudo badmod')
    logwrite("--[+]Successfully ran badmod @ " + timecheck() + '--')
  except:
    logwrite("--[*]Error running badmod @ " + timechcek() + '--')
  gohome()
  exit()

if tool == '-si' or tool == '--shellphish':
  try:
    os.chdir('shellphish')
    os.system('sudo ./shellphish.sh')
    logwrite("--[+]Successfully ran shellphish @ " + timecheck() + '--')
  except:
    logwrite("--[*]Error running shellphish @ " + timecheck() + '--')
  gohome()
  exit()

if tool == '-np' or tool == '--nexphisher':
  try:
    os.chdir('nexphisher')
    os.system('sudo ./nexphisher')
    logwrite("--[+]Successfully ran nexphisher @ " + timecheck() + '--')
  except:
    logwrite("--[*]Error running nexphisher @ " + timecheck() + '--')
  gohome()
  exit()

if tool == '-w3' or tool == '--w3af':
  try:
    os.chdir('w3af')
    os.system('sudo ./w3af_console')
    logwrite("--[+]Successfully ran w3af @ " + timecheck() + '--')
  except:
    logwrite("--[*]Error running w3af @ " + timecheck() + '--')
  gohome()
  exit()

if tool == '-ur' or tool == '--userrecon':
  try:
    os.chdir('userrecon')
    os.system('sudo ./userrecon.sh')
    logwrite('--[+]Successfully ran userrecon @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running userrecon @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-ws' or tool == '--winspy':
  try:
    os.chdir('winspy')
    os.system('sudo ./winspy.sh')
    logwrite('--[+]Successfully ran winspy @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running winspy @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-ti' or tool == '--th3inspector':
  try:
    os.system('Th3inspector')
    logwrite('--[+]Successfully ran th3inspector @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running th3inspector @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-wp' or tool == '--wifipumpkin':
  try:
    os.system('sudo wifipumpkin3')
    logwrite('--[+]Successfully ran wifipumpkin3 @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running wifipumpkin3 @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-lp' or tool == '--lockphish':
  try:
    os.chdir('lockphish')
    os.system('sudo ./lockphish.sh')
    logwrite('--[+]Successfully ran lockphish @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running lockphish @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-er' or tool == '--evilreg':
  try:
    os.chdir('evilreg')
    os.system('sudo ./evilreg.sh')
    logwrite('--[+]Successfully ran evilreg @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running evilreg @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-bl' or tool == '--badlnk':
  try:
    os.chdir('badlnk')
    os.system('sudo ./badlnk.sh')
    logwrite('--[+]Successfully ran badlnk @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running badlnk @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-sf' or tool == '--socialfish':
  try:
    os.chdir('SocialFish')
    os.system('sudo python3 SocialFish.py')
    logwrite('--[+]Successfully ran SocialFish @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running SocialFish @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-hk' or tool == '--herakeylogger':
  try:
    os.chdir('HeraKeylogger')
    os.system('sudo python3 hera.py')
    logwrite('--[+]Successfully ran HeraKeylogger @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running HeraKeylogger @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-ea' or tool == '--enigma':
  try:
    os.chdir('Enigma')
    os.system('sudo python enigma.py')
    logwrite('--[+]Successfully ran Enigma @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running Enigma @ '+ timecheck() + '--')
  gohome()
  exit()

if tool == '-lc' or tool == '--locator':
  try:
    os.chdir('locator')
    os.system('sudo ./locator.sh')
    logwrite('--[+]Successfully ran Locator @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running Locator @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-ep' or tool == '--evilapp':
  try:
    os.chdir('EvilApp')
    os.system('sudo ./evilapp.sh')
    logwrite('--[+]Successfully ran EvilApp @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running EvilApp @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-lv' or tool == '--leviathan':
  try:
    os.chdir('leviathan')
    os.system('sudo python leviathan.py')
    logwrite('--[+]Successfully ran leviathan @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running leviathan @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-hc' or tool == '--hiddencry':
  try:
    os.chdir('hidden-cry')
    os.system('sudo ./hidden-cry')
    logwrite('--[+]Successfully ran hidden-cry @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running hidden-cry @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-df' or tool == '--droidfiles':
  try:
    os.chdir('droidfiles')
    os.system('sudo ./droidfiles.sh')
    logwrite('--[+]Successfully ran droidfiles @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running droidfiles @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-af' or tool == '--avetfabric':
  try:
    os.chdir('avet')
    os.system('sudo python3 avet.py')
    logwrite('--[+]Successfully ran avet_fabric @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running avet_fabric @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-sn' or tool == '--snort':
  try:
    ipnet = input('[*]Enter IP net (ex. 192.168.1.0/24): ')
    print('[*]Putting Snort in NIDS Mode, Enter ^Z to exit...')
    os.system("sudo snort -d -l snortlogs/ -h " + ipnet + " -A console -c /etc/snort/snort.conf")
    logwrite('--[+]Successfully ran snort @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running snort @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-iy' or tool == '--ispy':
  try:
    os.chdir('ispy')
    os.system('sudo ./ispy')
    logwrite('--[+]Successfully ran ispy @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running ispy @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-nt' or tool == '--nekobot':
  try:
    os.chdir('NekoBotV1')
    os.system('sudo python NekoBot.py')
    logwrite('--[+]Successfully ran NekoBotV1 @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running NekoBotV1 @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-ci' or tool == '--cuteit':
  try:
    ip = input('[*]Enter host IP: ')
    os.chdir('Cuteit')
    os.system('sudo python3 Cuteit.py ' + ip)
    logwrite('--[+]Successfully ran Cuteit @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running Cuteit @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-tb' or tool == '--ftpbruter':
  try:
    os.chdir('FTPBruter')
    os.system('sudo python3 ftpbruter.py')
    logwrite('--[+]Successfully ran ftpbruter @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running Cuteit @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-cd' or tool == '--crydroid':
  try:
    os.chdir('crydroid')
    os.system('sudo ./crydroid.sh')
    logwrite('--[+]Successfully ran crydroid @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running crydroid @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-vp' or tool == '--evilpdf':
  try:
    os.chdir('evilpdf')
    os.system('sudo python3 evilpdf.py')
    logwrite('--[+]Successfully ran evilpdf @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running evilpdf @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-el' or tool == '--evildll':
  try:
    os.chdir('evildll')
    os.system('sudo ./evildll.sh')
    logwrite('--[+]Successfully ran evilddl @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running evildll @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-dt' or tool == '--droidtracker':
  try:
    os.chdir('DroidTracker')
    os.system('sudo ./droidtracker.sh')
    logwrite('--[+]Successfully ran droidtracker @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running droidtracker @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-mc' or tool == '--hmmcookies':
  try:
    os.chdir('hmmcookies')
    os.system('sudo ./hmmcookies.sh')
    logwrite('--[+]Successfully ran hmmcookies @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running hmmcookies @ ' + timecheck() + '--')
  gohome()
  exit()

if tool == '-lt' or tool == '--lstools':
  print('[*]BIOS_UBTU_Rooter.sh - Ubuntu BIOS USB Boot Exploit')
  print('[*]LinEnum - Linux Shell Enumeration Tool')
  print('[*]Linux - Linux Exploits & Enumeration Scripts')
  print('[*]Mimikatz_trunk - Windows Post Exploitation Tool')
  print('[*]mysql - SQL Exploits & Enumeration Scripts')
  print('[*]passwd_backdoor.sh - Post Exploit /etc/passwd backdoor user inserter')
  print('[*]pspy - Process Scanner for Linux')
  print('[*]windows-privesc-check - Windows Privelege Escalation Scripts')
  print('[*]Windows-Privelege-Escalation - Windows Privelege Escalation Scripts')
  print('[*]Chrompass - AV-Undetectable Chrome Login Extraction Tool')
  print('[*]htbenum - Offline Local Enum Server (Mainly for HTB)')
  print('[*]PeekABoo - Enables RDP Service (WinRM/WinServer only')
  print('[*]firefox_decrypt - Mozilla Browser Saved Login Extractor')
  print('[*]Powershell-reverse-tcp - Reverse TCP Powershell Payload w/ Obfuscation')
  print('[*]Invoker - Post Windows Non-GUI Shell Utility')
  print('[*]HiveJack - Windows SAM Dump Tool')
  print('[*]Win-Brute-Logon - Post Tool For Cracking User Passwords (XP -> 10)')
  print('[*]Covermyass - Covers Your Tracks on UNIX Systems')
  print('[*]GhostShell - AV Bypass, Anti VM, Anti Disassembly Payload Encoder')
  print('[*]gtfo - Unix Binary Search Tool')
  print('[*]Grok-backdoor - Python-Based Backdoor with Ngrok Tunneling')
  print('[*]Mimikatz - Windows Password, Hash, PIN, and kerberos ticket extraction tool')
  gohome()
  exit()

if tool not in short or tool not in long:
  print(sys.argv[1] + ' not an option!')
