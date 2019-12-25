#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# @name   : KITT Lite - Lite Version of KITT Framework
# @url    : https://github.com/Cisc0-gif
# @author : Cisc0-gif
import os
root = os.getcwd() #sets root as current directory for access to all tools
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
  with open(root + '/RUNTIME.log', 'a+') as f:
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
  print('Example:')
  print('        KITTlite --netcrack')
  sys.exit(1)

short = ['-ds', '-sh', '-pi', '-pe', '-nc', '-ap', '-pd', '-hp', '-pb', '-st', '-bv', '-bs', '-mj', '-gp', '-sp', '-sc', '-pc', '-fb', '-di']
long = ['--domainsticate', '--shodan_search', '--phone_infoga', '--escalate', '--netcrack', '--apspoof', '--packdump', '--homepwn', '--pentbox', '--btspoof', '--btverify', '--bluescan', '--mousejack', '--gpioctl', '--sshportrand', '--sshautoconfig', '--proxyconfig', '--fail2ban', '--dhcpip']

tool = sys.argv[1]

def gohome():
  global root
  wait()
  os.chdir(root)

if tool == '-ds' or tool == '--domainsticate':
  try:
    os.chdir('hg')
    os.system('python3 domain_sticate.py')
    logwrite('--[+]Successfully ran domainsticate @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running domainsticate @ ' + timecheck() + '--')
  gohome()

if tool == '-sh' or tool == '--shodan_search':
  try:
    os.system('python3 shodan_search.py')
    logwrite('--[+]Successfully ran shodan_search @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running shodan_search @ ' + timecheck() + '--')
  gohome()

if tool == '-pi' or tool == '--phone_infoga':
  try:
    os.chdir('PhoneInfoga')
    os.system('python3 phoneinfoga.py')
    logwrite('--[+]Successfully ran phone_infoga @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error runnning phone_infoga @ ' + timecheck() + '--')
  gohome()

if tool == '-pe' or tool == '--escalate':
  os.chdir('escalate')
  try:
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

if tool == '-nc' or tool == '--netcrack':
  try:
    os.system('python3 network_crack.py')
    logwrite('--[+]Successfully ran network_crack @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running network_crack @ ' + timecheck() + '--')
  gohome()

if tool == '-ap' or tool == '--apspoof':
  try:
    os.chdir('AP_Spoof')
    os.system('./setup.sh')
    logwrite('--[+]Successfully ran AP_Spoof setup.sh @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running AP_Spoof setup.sh @ ' + timecheck() + '--')
  gohome()

if tool == '-pd' or tool == '--packdump':
  try:
    os.system('./packetdump.sh')
    logwrite('--[+]Successfully ran packetdump.sh @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running packetdump.sh @ ' + timecheck() + '--')
  gohome()

if tool == '-hp' or tool == '--homepwn':
  try:
    os.chdir('HomePWN')
    os.system('python3 homePwn.py')
    logwrite('--[+]Successfully ran HomePWN @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running HomePWN @ ' + timecheck() + '--')
  gohome()

if tool == '-pb' or tool == '--pentbox':
  try:
    os.chdir('pentbox/pentbox-1.8')
    os.system('ruby pentbox.rb')
    logwrite('--[+]Successfully ran pentbox @ ' + timecheck() + '--')
  except:
    logwrite('--[+]Error running pentbox @ ' + timecheck() + '--')
  gohome()

if tool == '-st' or tool == '--btspoof':
  try:
    os.system('./bluespoof.sh')
    logwrite('--[+]Successfully ran bluespoof @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running bluespoof @ ' + timecheck() + '--')
  gohome()

if tool == '-bv' or tool == '--btverify':
  try:
    os.system('python3 btverifier.py')
    logwrite('--[+]Successfully ran btverifier @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running btverifier @ ' + timecheck() + '--')
  gohome()

if tool == '-bs' or tool == '--bluescan':
  try:
    os.system('./BlueScan.sh')
    logwrite('--[+]Successfully ran BlueScan @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running BlueScan @ ' + timecheck() + '--')
  gohome()

if tool == '-mj' or tool == '--mousejack':
  moj = input(Fore.CYAN + "[*]Do you want to initialize a [m]ousejack device or scan with [j]ackit?: " + Style.RESET_ALL)
  if moj == 'M' or moj == 'm':
    try:
      print(Fore.CYAN + "[*]Insert CrazyRadio PA device..." + Style.RESET_ALL)
      wait()
      os.chdir('mousejack/nrf-research-firmware')
      os.system('sudo make')
      os.system('sudo make install')
      os.system('dmesg')
      print(Fore.GREEN + "[+]Firmware Uploaded!" + Style.RESET_ALL)
      logwrite('--[+]Successfully uploaded mousejack firmware to CrazyRadio PA @ ' + timecheck() + '--')
    except:
      print(Fore.RED + "[*]Failed to upload Firmware!" + Style.RESET_ALL)
      logwrite('--[*]Failed to upload mouesjack firmware to CrazyRadio PA @ ' + timecheck() + '--')
  elif moj == 'J' or moj == 'j':
    try:
      print(Fore.CYAN + "[*]Insert CrazyRadio PA device w/ mousejack firmware..." + Style.RES>
      wait()
      os.system('jackit')
      print(Fore.GREEN + '[+]Scan complete!' + Style.RESET_ALL)
      logwrite('--[+]Successfully ended jackit scan @ ' + timecheck() + '--')
    except:
      print(Fore.RED + "[*]Error scanning with jackit" + Style.RESET_ALL)
      logwrite('--[*]Error scanning with jackit @ ' + timecheck() + '--')
      wait()
  else:
    print(Fore.RED + "[*]Not an option!" + Style.RESET_ALL)
    time.sleep(2)
  gohome()

if tool == '-gp' or tool == '--gpioctl':
  try:
    os.system('python3 GPIO_CTL.py')
    logwrite('--[+]Successfully ran GPIO_CTL @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running GPIO_CTL @ ' + timecheck() + '--')
  gohome()

if tool == '-sp' or tool == '--sshportrand':
  try:
    os.chdir('sdefense')
    os.system('./ssh_randomizer.sh')
    logwrite('--[+]Successfully ran ssh_randomizer @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running ssh_randomizer @ ' + timecheck() + '--')
  gohome()

if tool == '-sc' or tool == '--sshautoconfig':
  try:
    os.chdir('sdefense')
    os.system('./ssh_encr7pt.sh')
    logwrite('--[+]Successfully ran ssh_encr7pt @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running ssh_encr7pt @ ' + timecheck() + '--')
  gohome()

if tool == '-pc' or tool == '--proxyconfig':
  try:
    os.chdir('sdefense')
    os.system('./proxy_config.sh')
    logwrite('--[+]Successfully ran proxy_config @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running proxy_config @ ' + timecheck() + '--')
  gohome()

if tool == '-fb' or tool == '--fail2ban':
  try:
    ipbu = input(Fore.CYAN + '[*]Are you going to [B]an or [U]nban an IP?: ' + Style.RESET_AL>
    if ipbu == 'B' or ipbu == 'b':
      ip = input(Fore.CYAN + '[*]Enter IP: ' + Style.RESET_ALL)
      os.system('sudo fail2ban-client set sshd banip ' + ip)
      print(Fore.GREEN + '[+]Banned IP ' + ip + '!' + Style.RESET_ALL)
      logwrite('--[+]Banned IP ' + ip + ' @ ' + timecheck() + '--')
    else:
      ip = input(Fore.CYAN + '[*]Enter IP: ' + Style.RESET_ALL)
      os.system('sudo fail2ban-client set sshd unbanip ' + ip)
      print(Fore.GREEN + '[+]Unbanned IP ' + ip + '!' + Style.RESET_ALL)
      logwrite('--[+]Unbanned IP ' + ip + ' @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error configuring fail2ban @ ' + timecheck() + '--')
    print(Fore.RED + '[*]Error configuring fail2ban' + Style.RESET_ALL)
  gohome()

if tool == '-di' or tool == '--dhcpip':
  try:
    os.chdir('sdefense')
    os.system('./dh_recv.sh')
    logwrite('--[+]Successfully ran dh_recv @ ' + timecheck() + '--')
  except:
    logwrite('--[*]Error running dh_recv @ ' + timecheck() + '--')
  gohome()

if tool not in short or tool not in long:
  print(sys.argv[1] + ' not an option!')
"""
def home():
  global root
  os.chdir(root)
  os.system("figlet -f slant '   K I T T 2.0'")
  print('================================================================')
  print(' ' + Fore.YELLOW + '[R] README' + Style.RESET_ALL + '   | ' + time.ctime() + ' |   ' + Fore.YELLOW + '[L] CHANGELOG' + Style.RESET_ALL)
  print('                      ' + Fore.YELLOW + '[U]Update' + Style.RESET_ALL)
  print('================================================================')
  print(Fore.WHITE + '*' + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + '[1] OSINT - Open Source Intelligence Gathering                ' + Fore.WHITE + '*' + Style.RESET_ALL)
  print('*                                                              *')
  print(Fore.WHITE + '*' + Style.RESET_ALL + Fore.GREEN + '[2] Exploitation - Metasploit, Payloads, Exploits             ' + Fore.WHITE + '*' + Style.RESET_ALL)
  print('*                                                              *')
  print(Fore.WHITE + '*' + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + '[3] Enumeration - Win & Lin HTTP Hosted Enumeration Scripts   ' + Fore.WHITE + '*' + Style.RESET_ALL)
  print('*                                                              *')
  print(Fore.WHITE + '*' + Style.RESET_ALL + Fore.CYAN + '[4] Password Cracking - Bruteforcing and Cracking Tools       ' + Fore.WHITE + '*' + Style.RESET_ALL)
  print('*                                                              *')
  print(Fore.WHITE + '*' + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + '[5] Network Cracking - MiTM, Packet Tracing, WPA/WPA2 Cracking' + Fore.WHITE + '*' + Style.RESET_ALL)
  print('*                                                              *')
  print(Fore.WHITE + '*' + Style.RESET_ALL + Fore.BLUE + '[6] IoT Exploitation - HomePwn, HoneyPot, Bluetooth, etc      ' + Fore.WHITE + '*' + Style.RESET_ALL)
  print('*                                                              *')
  print(Fore.WHITE + '*' + Style.RESET_ALL + Fore.RED + Style.BRIGHT + '[7] Hardware Hacking - RubberDuckies, Keyloggers, MouseJack   ' + Fore.WHITE + '*' + Style.RESET_ALL)
  print('*                                                              *')
  print(Fore.WHITE + '*' + Style.RESET_ALL + Fore.RED + '[8] System Security - MAC Spoofing, Proxychains, SSH Encrypt  ' + Fore.WHITE + '*' + Style.RESET_ALL)
  print('*                                                              *')
  print(Fore.WHITE + '*' + Style.RESET_ALL + Fore.RED + Style.DIM + '[9] Misc.                                                     ' + Fore.WHITE + '*' + Style.RESET_ALL)
  print('*                                                              *')
  print(Fore.WHITE + '*' + Style.RESET_ALL + Fore.YELLOW + '[X] Exit' + '                                                      ' + Fore.WHITE + '*' + Style.RESET_ALL)
  print('================================================================')
  in_put = input(Fore.CYAN + os.getcwd() + ': ' + Style.RESET_ALL)
  nums = ['X', 'R', 'L', 'U', 'x', 'r', 'l', 'u'] #creates list of letters for options from menu
  for i in range(1,11): #creates range of numbers as options from menu
    nums.append(str(i))
  if in_put not in nums:
    print(Fore.RED + '[*]Invalid Option' + Style.RESET_ALL)
    time.sleep(2)
    home()
  elif in_put == '1':
    print(Fore.CYAN + '[*]OSINT' + Style.RESET_ALL)
    print('  [1] Info Gathering Tools')
    print('  [2] Domainsticate - Domain Enumeration')
    print('  [3] Shodan Search')
    print('  [4] PhoneInfoga')
    print('  [5] Phishing Tools')
    print('  [6] go home')
    osint = input(Fore.CYAN + '[*]Select OSINT Tool: ' + Style.RESET_ALL)
    if osint == '1':
      os.chdir('hg')
      print('Welcome to 2/3 of you life...')
      print('  [1] FOCA - Windows')
      print('  [2] g00gle dorks')
      print('  [3] r#con-ng')
      print('  [4] fbi_master')
      print('  [5] Aut0Sp!oit')
      print('  [6] Net-Creds SNiffer')
      print('  [7] go home')
      hg = input(os.getcwd() + ': ')
      if hg == '1':
        try:
          os.system('cp -R FOCA ~')
          print(Fore.GREEN + '[+]FOCA copied to home dir!' + Style.RESET_ALL)
          logwrite('--[+]Successfully copied FOCA to home dir! @ ' + timecheck() + '--')
        except:
          print(Fore.RED + '[*]FOCA not found!' + Style.RESET_ALL)
          logwrite('--[*]Error copying FOCA @ ' + timecheck() + '--')
        wait()
      elif hg == '2':
        logwrite('--[*]Reading dorks.md @ ' + timecheck() + '--')
        try:
          with open('dorks.md', 'r') as f:
            contents = f.read()
          print(contents)
        except:
          logwrite('--[*]Error reading dorks.md @ ' + timecheck() + '--')
          print(Fore.RED + '[*]dorks not found!' + Style.RESET_ALL)
        wait()
      elif hg == '3':
        try:
          print(Fore.CYAN + '[*]Starting recon-ng...' + Style.RESET_ALL)
          logwrite('--[*]Starting recon-ng @ ' + timecheck() + '--')
          os.system('recon-ng')
          print(Fore.GREEN + '[+]Successfully ended recon-ng!' + Style.RESET_ALL)
          logwrite('--[*]Successfully ended recon-ng @ ' + timecheck() + '--')
        except:
          print(Fore.RED + '[*]Error running recon-ng!' + Style.RESET_ALL)
          logwrite('--[*]Error running recon-ng @ ' + timecheck() + '--')
        wait()
      elif hg == '4':
        try:
          os.chdir('fbi-master')
          print(Fore.CYAN + '[*]Running fbi.py...' + Style.RESET_ALL)
          logwrite('--[*]Running fbi.py @ ' + timecheck() + '--')
          os.system('python fbi.py')
          print(Fore.GREEN + '[+]Successfully ended fbi.py!' + Style.RESET_ALL)
          logwrite('--[*]Successfully ended fbi.py @ ' + timecheck() + '--')
        except:
          print(Fore.RED + '[*]Error in running fbi.py!' + Style.RESET_ALL)
          logwrite('--[*]Error in running fbi.py @ ' + timecheck() + '--')
        wait()
      elif hg == '5':
        try:
          os.chdir('AutoSploit')
          print(Fore.CYAN + '[*]Running autosploit.py...' + Style.RESET_ALL)
          logwrite('--[*]Running autosploit.py @ ' + timecheck() + '--')
          os.system('python autosploit.py')
          print(Fore.GREEN + '[+]Successfully ended autosploit.py!' + Style.RESET_ALL)
          logwrite('--[*]Successfully ended autosploit.py @ ' + timecheck() + '--')
        except:
          print(Fore.RED + '[*]Error running autosploit.py!' + Style.RESET_ALL)
          logwrite('--[*]Error running autosploit.py @ ' + timecheck() + '--')
        wait()
      elif hg == '6':
        print(Fore.CYAN + '[*]Running net-creds.py packet sniffer...' + Style.RESET_ALL)
        logwrite('--[*]Running net-creds.py @ ' + timecheck() + '--')
        try:
          print(Fore.CYAN + '[*]Enter ^C or ^Z to stop packet sniffer' + Style.RESET_ALL)
          os.system('python net-creds.py')
          print(Fore.GREEN + '[+]Output directed to credentials.txt!' + Style.RESET_ALL)
          logwrite('--[*]Successfully ended net-creds.py @ ' + timecheck() + '--')
        except:
          print(Fore.RED + '[*]Packet Sniffer ended prematurely!' + Style.RESET_ALL)
          logwrite('--[*]Error running net-creds.py @ ' + timecheck() + '--')
        wait()
      elif hg == '7':
        wait()
    elif osint == '2':
      os.chdir('hg')
      try:
        print(Fore.CYAN + '[*]Running domain_sticate.py...' + Style.RESET_ALL)
        domain = input('Enter domain here (domain.ext or 0.0.0.0): ')
        os.system('python3 domain_sticate.py ' + domain)
        print(Fore.GREEN + '[+]Successfully ended domain_sticate.py' + Style.RESET_ALL)
        logwrite('--[+]Successfully ended domain_sticate.py @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error in file domain_sticate.sh' + Style.RESET_ALL)
        logwrite('--[*]Error running domain_sticate.py @ ' + timecheck() + '--')
      wait()
    elif osint == '3':
      try:
        print(Fore.CYAN + '[*]Running shodan_search.py...' + Style.RESET_ALL)
        os.system('python3 shodan_search.py')
        print(Fore.GREEN + '[+]Successfully ended shodan_search.py!' + Style.RESET_ALL)
        logwrite('--[*]Successfully ended shodan_search.py @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error running shodan_search.py @ ' + timecheck() + '--')
        print(Fore.RED + '[*]Error running shodan_search.py!' + Style.RESET_ALL)
      wait()
    elif osint == '4':
      try:
        os.chdir('PhoneInfoga')
        n = input(Fore.CYAN + '[*]Enter phone number 1##########: ' + Style.RESET_ALL)
        os.system('python3 phoneinfoga.py -n ' + str(n))
        print(Fore.GREEN + '[+]Completed PhoneInfoga Scan!' + Style.RESET_ALL)
        logwrite('--[+]Completed PhoneInfoga Scan @ ' + timecheck() + '--')
      except:
        print(Fore.RED + "[*]Error running PhoneInfoga Scan!" + Style.RESET_ALL)
        logwrite('--[*]Error running PhoneInfoga Scan @ ' + timecheck() + '--')
      wait()
    elif osint == '5':
      os.chdir('phishing')
      print('  [1] sonar.py - batch email sender')
      print('  [2] blackeye - webpage phishing generator')
      print('  [3] SET - Social Engineer Toolkit')
      print('  [4] go home')
      phish = input(': ')
      if phish == '1':
        try:
          os.system('python3 sonar.py')
          print(Fore.GREEN + '[+]Ended sonar.py!')
          logwrite('--[*]Successfully ended sonar.py @ ' + timecheck() + '--')
        except:
          print(Fore.RED + '[*]sonar.py not found!' + Style.RESET_ALL)
          logwrite('--[*]Error running sonar.py @ ' + timecheck() + '--')
        wait()
      elif phish == '2':
        os.chdir('blackeye')
        try:
          os.system('bash blackeye.sh')
          print(Fore.GREEN + '[+]Ended blackeye.sh!')
          logwrite('--[*]Successfully ended blackeye.sh @ ' + timecheck() + '--')
        except:
          print(Fore.RED + '[*]blackeye.sh not found!' + Style.RESET_ALL)
          logwrite('--[*]Error running blackeye.sh @ ' + timecheck() + '--')
        wait()
      elif phish == '3':
        os.chdir('SET')
        try:
          os.system('python setoolkit')
          print(Fore.GREEN + '[+]Ended SET!')
          logwrite('--[*]Successfully ended SET @ ' + timecheck() + '--')
        except:
          print(Fore.RED + '[*]SET not found!' + Style.RESET_ALL)
          logwrite('--[*]Error running SET @ ' + timecheck() + '--')
        wait()
      elif phish == '4':
        wait()
    elif osint == '6':
      wait()
  elif in_put == '2':
    print(Fore.CYAN + '[*]Exploitation' + Style.RESET_ALL)
    print('  [1] Metasploit')
    print('  [2] Non-Metasploit Vulns')
    print('  [3] Payloads - PHP-webshells, P4wnP1 ALOA')
    print('  [4] OWASP-ZSC - Payload Encoder')
    print('  [5] go home')
    xplt = input(Fore.CYAN + '[*]Select Exploit Tool: ' + Style.RESET_ALL)
    if xplt == '1':
      try:
        logwrite("--[*]Started Msfconsole @ " + timecheck() + '--')
        print(Fore.CYAN + '[*]Starting Metasploit-Framework...')
        os.system('service postgresql start')
        os.system('msfconsole')
        print(Fore.GREEN + '[+]Metasploit-Framework Ran Successfully!' + Style.RESET_ALL)
        logwrite("--[+]Msfconsole ended @ " + timecheck() + '--')
      except:
        logwrite("--[*]Error starting postgresql or msfconsole @ " + timecheck() + '--')
        print(Fore.RED + '[*]Error starting postgresql or msfconsole!' + Style.RESET_ALL)
      wait()
    elif xplt == '2':
      os.chdir('exploits')
      print('[*]Custom Exploits')
      print('  [1] LM_expl0it_WIN.sh')
      print('  [2] Unp!ug.sh')
      print('  [3] Cisco_E4200_vuln.py')
      print('  [4] Redis-Server-Exploit.py')
      print('  [5] go home')
      exploit = input(os.getcwd() + ': ')
      if exploit == '1':
        try:
          os.system('cp -R LM_exploit_WIN.sh ~')
          print(Fore.GREEN + '[+]exploit copied to home dir!' + Style.RESET_ALL)
          logwrite('--[+]Successfully copied exploit @ ' + timecheck() + '--')
        except:
          logwrite('--[*]Error copying exploit @ ' + timecheck() + '--')
          print(Fore.RED + '[*]exploit not found!' + Style.RESET_ALL)
        wait()
      elif exploit == '2':
        try:
          os.system('cp -R unplug.sh ~')
          print(Fore.GREEN + '[+]exploit copied to homr dir!' + Style.RESET_ALL)
          logwrite('--[+]Successfully copied exploit @ ' + timecheck() + '--')
        except:
          logwrite('--[*]Error copying exploit @ ' + timecheck() + '--')
          print(Fore.RED + '[*]exploit not found!' + Style.RESET_ALL)
        wait()
      elif exploit == '3':
        try:
          os.system('cp -R Cisco_E4200_vuln.py ~')
          print(Fore.GREEN + '[+]exploit copied to home dir!' + Style.RESET_ALL)
          logwrite('--[+]Successfully copied exploit @ ' + timecheck() + '--')
        except:
          logwrite('--[*]Error copying exploit @ ' + timecheck() + '--')
          print(Fore.RED + '[*]exploit not found!' + Style.RESET_ALL)
        wait()
      elif exploit == '4':
        try:
          os.system('cp -R redis.py ~')
          print(Fore.GREEN + '[+]exploit copied to home dir!' + Style.RESET_ALL)
          logwrite('--[+]Successfully copied exploit @ ' + timecheck() + '--')
        except:
          logwrite('--[*]Error copying exploit @ ' + timecheck() + '--')
          print(Fore.RED + '[*]exploit not found!' + Style.RESET_ALL)
        wait()
      elif exploit == '5':
        wait()
    elif xplt == '3':
      os.chdir('payloads')
      print('  [1]DDoS')
      print('  [2]P4wnP1')
      print('  [3]PHP')
      print('  [4]Exit')
      pyld = input(os.getcwd() + ': ')
      if pyld == '1':
        try:
          os.chdir('ddos')
          os.system('ls')
          file = input(Fore.CYAN + "[*]Enter filename to copy to home dir or 'q' to quit: " + Style.RESET_ALL)
          if file == 'q' or file == 'Q':
            wait()
          else:
            os.chdir('cp ' + file + ' ~')
            print(Fore.GREEN + '[+]DDoS payload copied to home dir!' + Style.RESET_ALL)
            logwrite('--[+]DDoS payload copied to home dir @ ' + timecheck() + '--')
        except:
          print(Fore.RED + '[*]DDoS payload failed to copy to home dir!' + Style.RESET_ALL)
          logwrite('--[*]DDoS payload failed to copy to home dir @ ' + timecheck() + '--')
      elif pyld == '2':
        try:
          os.chdir('p4wnp1')
          os.system('ls')
          file = input(Fore.CYAN + "[*]Enter filename to copy to home dir or 'q' to quit: " + Style.RESET_ALL)
          if file == 'q' or file == 'Q':
            wait()
          else:
            os.chdir('cp ' + file + ' ~')
            print(Fore.GREEN + '[+]P4wnP1 payload copied to home dir!' + Style.RESET_ALL)
            logwrite('--[+]P4wnP1 payload copied to home dir @ ' + timecheck() + '--')
        except:
          print(Fore.RED + '[*]P4wnP1 payload failed to copy to home dir!' + Style.RESET_ALL)
          logwrite('--[*]P4wnP1 payload failed to copy to home dir @ ' + timecheck() + '--')
      elif pyld == '3':
        try:
          os.chdir('php-webshells')
          os.system('ls')
          file = input(Fore.CYAN + '[*]Enter filename to copy to home dir: ' + Style.RESET_ALL)
          if file == 'q' or file == 'Q':
            wait()
          else:
            os.chdir('cp ' + file + ' ~')
            print(Fore.GREEN + '[+]PHP payload copied to home dir!' + Style.RESET_ALL)
            logwrite('--[+]PHP payload copied to home dir @ ' + timecheck() + '--')
        except:
          print(Fore.RED + '[*]PHP payload failed to copy to home dir!' + Style.RESET_ALL)
          logwrite('--[*]PHP payload failed to copy to home dir @ ' + timecheck() + '--')
      elif pyld == '4':
        wait()
    elif xplt == '4':
      try:
        os.chdir('OWASP-ZSC')
        os.system('python3 zsc.py')
        print(Fore.GREEN + '[+]OWASP-ZSC shutdown successfully!' + Style.RESET_ALL)
        logwrite('--[+]OWASP-ZSC shutdown successfully @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]OWASP-ZSC failed to start!' + Style.RESET_ALL)
        logwrite('--[*]OWASP-ZSC failed to start @ ' + timecheck() + '--')
    elif xplt == '5':
      wait()
  elif in_put == '3':
    os.chdir('escalate')
    try:
      print(Fore.CYAN + '[*]Starting python SimpleHTTPServer on Port 80 to curl payloads...')
      print(Fore.CYAN + '[*]Enter ^C or ^Z To Stop HTTP Server...')
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.connect(("8.8.8.8", 80))
      r = requests.get("http://ifconfig.me").text
      print(Fore.CYAN + '[*]Private IP: ' + Style.RESET_ALL + str(s.getsockname()[0]))
      print(Fore.CYAN + '[*]Public IP: ' + Style.RESET_ALL + str(r))
      os.system("python -m SimpleHTTPServer 80")
      s.close()
      print(Fore.GREEN + '[+]Successfully ended SimpleHTTPServer!' + Style.RESET_ALL)
      logwrite('--[*]Successfully ended SimpleHTTPServer @ ' + timecheck() + '--')
    except:
      print(Fore.RED + '[*]Error running SimpleHTTPServer!' + Style.RESET_ALL)
      logwrite('--[*]Error running SimpleHTTPServer @ ' + timecheck() + '--')
    wait()
  elif in_put == '4':
    os.chdir('crackers')
    print(Fore.CYAN + '[*] Passwd Cracking' + Style.RESET_ALL)
    print('  [1] append_num')
    print('  [2] burpsuite')
    print('  [3] dec0ders')
    print('  [4] R0T_decrypt - :WARNING: Due to extensive wordlist, KITT may crash under this!')
    print('  [5] go home' + Style.RESET_ALL)
    crack = input(Fore.CYAN + '[*]Select Passwd Cracking Tool: ' + Style.RESET_ALL)
    if crack == '1':
      logwrite('--[*]Starting append_num.py @ ' + timecheck() + '--')
      os.system('python3 append_num.py')
      wait()
    elif crack == '2':
      logwrite('--[*]Starting burpsuite @ ' + timecheck() + '--')
      print(Fore.CYAN + "[*]Running Burpsuite..." + Style.RESET_ALL)
      os.system("burpsuite")
      wait()
    elif crack == '3':
      logwrite('--[*]Reading decoders.md @ ' + timecheck() + '--')
      with open('decoders.md', 'r') as f:
        contents = f.read()
      print(contents)
      wait()
    elif crack == '4':
      logwrite('--[*]Running ROT Bruteforcer @ ' + timecheck() + '--')
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      def recursion():
        message = input("[*]ROT Cipher Text: " + Style.RESET_ALL).lower().split(' ')
        if message == 'q':
          wait()
          home()
        else:
          LETTERS = 'abcdefghijklmnopqrstuvwxyz'
          l = []
          for word in list(message):
            for key in range(len(LETTERS)):
              translated = ''
              for symbol in word:
                if symbol in LETTERS:
                  num = LETTERS.find(symbol)
                  num = num - key
                  if num < 0:
                    num = num + len(LETTERS)
                  translated = translated + LETTERS[num]
                else:
                  translated = translated + symbol
              l.append(translated)
          with open('Edictionary.txt', 'r') as f:
            wordlist = f.read().splitlines()
            for i in l:
              if i in wordlist:
                print(Fore.GREEN + '[+]Decrypted Ciphertext: "' + i + '"' + Style.RESET_ALL)
          wait()
          recursion()
      recursion()
    elif crack == '5':
      wait()
  elif in_put == '5':
    print('[*]Network Cracking')
    print('  [1]Network Cracking Tools - aircrack-ng, MiTM, Pixie-Dust, Wash')
    print('  [2]Network Packet Dump')
    print('  [3]AP_Spoofer')
    print('  [4]go home')
    net = input(Fore.CYAN + '[*]Select Network Cracking Tool: ' + Style.RESET_ALL)
    if net == '1':
      try:
        print(Fore.CYAN + '[*]Running network_crack.py...' + Style.RESET_ALL)
        os.system('python3 network_crack.py')
        print(Fore.GREEN + '[*]Successfully ended network_crack.py!' + Style.RESET_ALL)
        logwrite('--[*]Successfully ended network_crack.py @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error running network_crack.py!' + Style.RESET_ALL)
        logwrite('--[*]Error running network_crack.py @ ' + timecheck() + '--')
      wait()
    elif net == '2':
      try:
        print(Fore.CYAN + '[*]Running packetdump.sh...' + Style.RESET_ALL)
        os.system('sudo ./packetdump.sh')
        os.system('mv output.pcap ~')
        logwrite('--[+]Packetdump.sh output directed to home dir @ ' + timecheck() + '--')
        print(Fore.GREEN + '[+]copied packet capture to home dir!' + Style.RESET_ALL)
      except:
        logwrite('--[*]Error writing output to home dir @ ' + timecheck() + '--')
        print(Fore.RED + '[*]packet capture not found!' + Style.RESET_ALL)
      wait()
    elif net == '3':
      try:
        os.chdir('AP_Spoof')
        hd = input(Fore.CYAN + '[*]Plug in AP Enabled Network Adapter Now...' + Style.RESET_ALL)
        os.system('./setup.sh')
        wait()
        print(Fore.GREEN + '[+]AP_Spoofer setup successfully!' + Style.RESET_ALL)
        logwrite('--[+]AP_Spoofer setup successfully @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]AP_Spoofer setup failed!' + Style.RESET_ALL)
        logwrite('--[*]AP_Spoofer setup failed @ ' + timecheck() + '--')
      wait()
    elif net == '4':
      wait()
  elif in_put == '6':
    print('[*]IoT Exploitation')
    print('  [1]HomePwn - IoT Exploit Tool')
    print('  [2]PentBox - HoneyPot Tool')
    print('  [3]Spooftooph - BT Spoofing')
    print('  [4]BtVerifier - Rfcomm Channel Verifier')
    print('  [5]BlueScan - BT Class and MAC Scanner')
    print('  [6]go home')
    iot = input(Fore.CYAN + '[*]Select IoT Exploit Tool: ' + Style.RESET_ALL)
    if iot == '1':
      os.chdir('HomePWN')
      print(Fore.CYAN + '[*]Running HomePWN framework...' + Style.RESET_ALL)
      try:
        os.system('python3 homePwn.py')
        logwrite('--[+]Successfully ended HomePWN @ ' + timecheck() + '--')
        print(Fore.GREEN + '[+]Successfully ended HomePWN' + Style.RESET_ALL)
      except:
        logwrite('--[*]Error running HomePWN @ ' + timecheck() + '--')
        print(Fore.RED + '[*]Error running HomePWN!' + Style.RESET_ALL)
      wait()
    elif iot == '2':
      os.chdir('pentbox/pentbox-1.8')
      print(Fore.CYAN + '[*]Running Pentbox1.8...' + Style.RESET_ALL)
      try:
        os.system('./pentbox.rb')
        logwrite('--[+]Successfully ended Pentbox1.8 @ ' + timecheck() + '--')
        print(Fore.GREEN + '[+]Successfully ended Pentbox1.8!' + Style.RESET_ALL)
      except:
        logwrite('--[*]Error running Pentbox1.8 @ ' + timecheck() + '--')
        print(Fore.RED + '[*]Error running Pentbox1.8!' + Style.RESET_ALL)
      wait()
    elif iot == '3':
      print(Fore.CYAN + '[*]Running bluespoof.sh...' + Style.RESET_ALL)
      try:
        os.system('./bluespoof.sh')
        print(Fore.GREEN + '[+]Successfully ended bluespoof.sh!' + Style.RESET_ALL)
        logwrite('--[+]Successfully ended bluespoof.sh @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error running bluespoof.sh @ ' + timecheck() + '--')
        print(Fore.RED + '[*]Error running bluespoof.sh!' + Style.RESET_ALL)
      wait()
    elif iot == '4':
      print(Fore.CYAN + '[*]Running btverifier.py...' + Style.RESET_ALL)
      try:
        os.system('python3 btverifier.py')
        print(Fore.GREEN + '[+]Successfully ended btverifier.py!' + Style.RESET_ALL)
        logwrite('--[*]Successfully ended btverifier.py @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error running btverifier.py!' + Style.RESET_ALL)
        logwrite('--[*]Error running btverifier.py @ ' + timecheck() + '--')
      wait()
    elif iot == '5':
      print(Fore.CYAN + '[*]Running BlueScan.sh...' + Style.RESET_ALL)
      try:
        os.system('./BlueScan.sh')
        print(Fore.GREEN + '[+]Successfully ended BlueScan.sh!' + Style.RESET_ALL)
        logwrite('--[*]Successfully ended BlueScan.sh @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error running BlueScan.sh!' + Style.RESET_ALL)
        logwrite('--[*]Error running BlueScan.sh @ ' + timecheck() + '--')
      wait()
    elif iot == '6':
      wait()
  elif in_put == '7':
    print('[*]Hardware Hacking')
    print('  [1]Android Rootkits')
    print('  [2]MouseJack')
    print('  [3]Keyloggers')
    print('  [4]RubberDucky Tools - Digispark')
    print('  [5]GPIO_CTL - RPI GPIO controller')
    print('  [6]go home')
    hh = input(Fore.CYAN + '[*]Select Hardware Hacking Tool: ' + Style.RESET_ALL)
    if hh == '1':
      try:
        os.chdir('rooters')
        os.system('ls')
        dev_rooter = input(Fore.CYAN + '[*]Select a dev_rooter for use: ' + Style.RESET_ALL)
        os.system('cp ' + dev_rooter + ' ~')
        print(Fore.GREEN + '[+]dev_rooter copied to home dir!' + Style.RESET_ALL)
        logwrite('--[+]Successfully copied dev_rooter to home dir @ ' + timecheck() + '--')
      except:
        logwrite("--[*]Error copying dev_rooter @ " + timecheck() + '--')
        print(Fore.RED + '[*]dev_rooter not found!' + Style.RESET_ALL)
      wait()
    elif hh == '2':
      moj = input(Fore.CYAN + "[*]Do you want to initialize a [m]ousejack device or scan with [j]ackit?[m/j]: " + Style.RESET_ALL)
      if moj == 'M' or moj == 'm':
        try:
          print(Fore.CYAN + "[*]Insert CrazyRadio PA device..." + Style.RESET_ALL)
          wait()
          os.chdir('mousejack/nrf-research-firmware')
          os.system('sudo make')
          os.system('sudo make install')
          os.system('dmesg')
          print(Fore.GREEN + "[+]Firmware Uploaded!" + Style.RESET_ALL)
          logwrite('--[+]Successfully uploaded mousejack firmware to CrazyRadio PA @ ' + timecheck() + '--')
        except:
          print(Fore.RED + "[*]Failed to upload Firmware!" + Style.RESET_ALL)
          logwrite('--[*]Failed to upload mouesjack firmware to CrazyRadio PA @ ' + timecheck() + '--')
        wait()
      elif moj == 'J' or moj == 'j':
        try:
          print(Fore.CYAN + "[*]Insert CrazyRadio PA device w/ mousejack firmware..." + Style.RESET_ALL)
          wait()
          os.system('jackit')
          print(Fore.GREEN + '[+]Scan complete!' + Style.RESET_ALL)
          logwrite('--[+]Successfully ended jackit scan @ ' + timecheck() + '--')
        except:
          print(Fore.RED + "[*]Error scanning with jackit" + Style.RESET_ALL)
          logwrite('--[*]Error scanning with jackit @ ' + timecheck() + '--')
        wait()
      else:
        print(Fore.RED + "[*]Not an option!" + Style.RESET_ALL)
        time.sleep(2)
    elif hh == '3':
      os.chdir('keyloggers')
      print('  [1] Winupdate')
      print('  [2] kidlogger(win)')
      print('  [3] staffcounter(lin)')
      print('  [4] go home')
      keylog = input(os.getcwd() + ': ')
      if keylog == '1':
        try:
          os.system('cp -R Winupdate ~')
          print(Fore.GREEN + '[+]keylogger copied to home dir!' + Style.RESET_ALL)
          logwrite('--[+]Successfully copied keylogger @ ' + timecheck() + '--')
        except:
          logwrite('--[*]Error copying keylogger @ ' + timecheck() + '--')
          print(Fore.RED + '[*]keylogger not found!' + Style.RESET_ALL)
        wait()
      elif keylog == '2':
        try:
          os.system('cp -R KidLogger-setupwin26-11-2017 ~')
          print(Fore.GREEN + '[+]keylogger copied to home dir!' + Style.RESET_ALL)
          logwrite('--[+]Successfully copied keylogger @ ' + timecheck() + '--')
        except:
          logwrite('--[*]Error copying keylogger @ ' + timecheck() + '--')
          print(Fore.RED + '[*]keylogger not found!' + Style.RESET_ALL)
        wait()
      elif keylog == '3':
        try:
          os.system('cp -R staffcounter_install ~')
          print(Fore.GREEN + '[+]keylogger copied to home dir!' + Style.RESET_ALL)
          logwrite('--[+]Successfully copied keylogger @ ' + timecheck() + '--')
        except:
          logwrite('--[*]Error copying keylogger @ ' + timecheck() + '--')
          print(Fore.RED + '[*]keylogger not found!' + Style.RESET_ALL)
        wait()
      elif keylog == '4':
        wait()
    elif hh == '4':
      os.chdir('digis')
      print(Fore.CYAN + '[*]Running duck2spark converter...' + Style.RESET_ALL)
      logwrite('--[*]Running duck2spark converter @ ' + timecheck() + '--')
      print(Fore.CYAN + '[*[Your current directory: ' + Style.RESET_ALL + os.getcwd())
      try:
        os.system('sudo ./convert.sh')
        print(Fore.GREEN + '[+]Successfully converted ducky script to spark!' + Style.RESET_ALL)
        logwrite('--[+]Successfully converted script @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error running duck2spark...' + Style.RESET_ALL)
        logwrite('--[*]Error runnnig duck2spark @ ' + timecheck() + '--')
      wait()
    elif hh == '5':
      print(Fore.CYAN + '[*]Running GPIO_CTL.py...' + Style.RESET_ALL)
      logwrite('--[*]Running GPIO_CTL.py @ ' + timecheck() + '--')
      try:
        os.system('python3 GPIO_CTL.py')
        print(Fore.GREEN + '[+]Successfully ended GPIO_CTL.py!' + Style.RESET_ALL)
        logwrite('--[+]Successfully ended GPIO_CTL.py @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error running GPIO_CTL.py' + Style.RESET_ALL)
        logwrite('--[+]Successfully ended GPIO_CTL.py @ ' + timecheck() + '--')
    elif hh == '6':
      wait()
  elif in_put == '8':
    os.chdir('sdefense')
    print('[*]System Security')
    print('  [1] MAC_changer')
    print('  [2] ssh_p0Rt_r@andomizer')
    print('  [3] ssh rsa_key generator')
    print('  [4] pr0xy router')
    print('  [5] ssh_encr7tion')
    print('  [6] st@tic IP')
    print('  [7] Fail2ban Configurations')
    print('  [8] DHCP IP Reception')
    print('  [9] go home')
    rdefense = input(Fore.CYAN + '[*]Select Security Tool: ' + Style.RESET_ALL)
    if rdefense == '1':
      try:
        logwrite('--[*]Running macchanger.sh @ ' + timecheck() + '--')
        print(Fore.CYAN + '[*]Running macchanger.sh...' + Style.RESET_ALL)
        os.system('./macchanger.sh')
        print(Fore.GREEN + '[+]Successfully ended macchanger.sh!' + Style.RESET_ALL)
        logwrite('--[+]Successfully ended macchanger @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error in changing mac address!' + Style.RESET_ALL)
        logwrite('--[*]Error running macchanger.sh @ ' + timecheck() + '--')
      wait()
    elif rdefense == '2':
      try:
        logwrite('--[*]Running ssh_randomizer.sh @ ' + timecheck() + '--')
        print(Fore.CYAN + '[*]Running ssh_randomizer.sh...' + Style.RESET_ALL)
        os.system('./ssh_randomizer.sh')
        print(Fore.GREEN + '[+]Successfully ended ssh_randomizer.sh!' + Style.RESET_ALL)
        logwrite('--[+]Successfully ended ssh_randomizer.sh @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error in changing ssh port' + Style.RESET_ALL)
        logwrite('--[*]Error running ssh_randomizer.sh @ ' + timecheck() + '--')
      wait()
    elif rdefense == '3':
      try:
        print(Fore.CYAN + '[*]Beginning RSA Key Generation Process...' + Style.RESET_ALL)
        os.system('sudo service ssh start')
        print(Fore.GREEN + '[+]ssh daemon started...' + Style.RESET_ALL)
        os.system('mkdir ~/.ssh')
        print(Fore.GREEN + '[+]key directory generated...' + Style.RESET_ALL)
        uname = input('Enter username for ssh: ')
        port = input('Enter local ssh port: ')
        print('Leave filepath for keys blank for default')
        os.system('ssh-keygen')
        print(Fore.GREEN + '[+]ssh rsa keys generated...' + Style.RESET_ALL)
        os.system('ssh-copy-id -i ~/.ssh/id_rsa ' + uname + '@localhost -p ' + port)
        print(Fore.GREEN + '[+]ssh keys copied to ssh server...' + Style.RESET_ALL)
        os.system('ssh ' + uname + '@localhost -p ' + port)
        os.system('exit')
        print(Fore.GREEN + '[+]ssh connection test successful...' + Style.RESET_ALL)
        os.system('cp ~/.ssh/id_rsa ~/')
        print(Fore.GREEN + '[+]private key copied to homed dir...' + Style.RESET_ALL)
        print(Fore.GREEN + '[+]SSH RSA Key Login Setup Complete!')
        logwrite('--[+]SSH RSA Key Login Setup Complete @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error Running SSH RSA Login Setup!' + Style.RESET_ALL)
        logwrite('--[*]Error running ssh rsa key login setup @ ' + timecheck() + '--')
      wait()
    elif rdefense == '4':
      try:
        print(Fore.CYAN + '[*]Running proxy_config.sh' + Style.RESET_ALL)
        os.system('./proxy_config.sh')
        print(Fore.GREEN + '[+]Successfully ended proxy_config.sh!' + Style.RESET_ALL)
        logwrite('--[+]Successfully ended proxy_config.sh @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error in running proxy_config.sh!' + Style.RESET_ALL)
        logwrite('--[*]Error running proxy_config.sh @ ' + timecheck() + '--')
      wait()
    elif rdefense == '5':
      try:
        print(Fore.CYAN + '[*]Running ssh_encr7pt.sh...' + Style.RESET_ALL)
        os.system('./ssh_encr7pt.sh')
        print(Fore.GREEN + '[+]Successfully ended ssh_encr7pt.sh!' + Style.RESET_ALL)
        logwrite('--[+]Successfully ended ssh_encr7pt.sh @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error running ssh_encr7pt.sh @ ' + timecheck() + '--')
        print(Fore.RED + '[*]Error in running ssh_encr7pt.sh!' + Style.RESET_ALL)
      wait()
    elif rdefense == '6':
      try:
        print(Fore.CYAN + '[*]Running static_ip.sh...' + Style.RESET_ALL)
        os.system('./static_ip.sh')
        print(Fore.GREEN + '[+]Successfully ended static_ip.sh!' + Style.RESET_ALL)
        logwrite('--[+]Successfully ended static_ip.sh @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error running static_ip.sh @ ' + timecheck() + '--')
        print(Fore.RED + '[*]Error running static_ip.sh!' + Style.RESET_ALL)
      wait()
    elif rdefense == '7':
      try:
        ipbu = input(Fore.CYAN + '[*]Are you going to [B]an or [U]nban an IP?: ' + Style.RESET_ALL)
        if ipbu == 'B' or ipbu == 'b':
          ip = input(Fore.CYAN + '[*]Enter IP: ' + Style.RESET_ALL)
          os.system('sudo fail2ban-client set sshd banip ' + ip)
          print(Fore.GREEN + '[+]Banned IP ' + ip + '!' + Style.RESET_ALL)
          logwrite('--[+]Banned IP ' + ip + ' @ ' + timecheck() + '--')
        else:
          ip = input(Fore.CYAN + '[*]Enter IP: ' + Style.RESET_ALL)
          os.system('sudo fail2ban-client set sshd unbanip ' + ip)
          print(Fore.GREEN + '[+]Unbanned IP ' + ip + '!' + Style.RESET_ALL)
          logwrite('--[+]Unbanned IP ' + ip + ' @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error configuring fail2ban @ ' + timecheck() + '--')
        print(Fore.RED + '[*]Error configuring fail2ban' + Style.RESET_ALL)
      wait()
    elif rdefense == '8':
      try:
        print(Fore.CYAN + '[*]Running dh_recv.sh...' + Style.RESET_ALL)
        os.system('./dh_recv.sh')
        print(Fore.GREEN + '[+]Successfully ran dh_recv.dh!' + Style.RESET_ALL)
        logwrite('--[+]Successfully ran dh_recv.dh @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error running dh_recv.sh!' + Style.RESET_ALL)
        logwrite('--[*]Error running dh_recv.sh @ ' + timecheck() + '--')
      wait()
    elif rdefense == '9':
      wait()
  elif in_put == '9':
    print('[*]Miscellaneous')
    print('  [1]File Backup')
    print('  [2]IRCssi')
    print('  [3]go home')
    misc = input(os.getcwd() + ': ')
    if misc == '1':
      try:
        print(Fore.CYAN + '[*]Running backup.sh...' + Style.RESET_ALL)
        os.system('sudo ./backup.sh')
        logwrite('--[*]Successfully ended backup.sh @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error running backup.sh @ ' + timecheck() + '--')
        print(Fore.RED + '[*]Error running backup.sh' + Style.RESET_ALL)
      wait()
    elif misc == '2':
      try:
        print(Fore.CYAN + '[*]Running irssi...' + Style.RESET_ALL)
        os.system('irssi')
        print(Fore.GREEN + '[+]Successfully ended irssi' + Style.RESET_ALL)
        logwrite('--[+]Successfully ended irssi @ ' + Style.RESET_ALL)
      except:
        logwrite('--[*]Error running irssi @ ' + timecheck() + '--')
        print(Fore.RED + '[*]Error running irssi!' + Style.RESET_ALL)
      wait()
    elif misc == '3':
      wait()
  elif in_put == 'R' or in_put == 'r':
    os.chdir(root)
    print(Fore.CYAN + '[*]Reading README.md...' + Style.RESET_ALL)
    logwrite('--[*]Reading README.md @ ' + timecheck() + '--')
    os.system('more README.md')
    wait()
  elif in_put == 'U' or in_put == 'u':
    try:
      print(Fore.CYAN + '[*]Updating System Libs...' + Style.RESET_ALL)
      os.system('sudo apt update')
      print(Fore.GREEN + '[+]Done!' + Style.RESET_ALL)
      print(Fore.CYAN + '[*]Upgrading Packages & Dependencies...' + Style.RESET_ALL)
      os.system('sudo apt upgrade')
      print(Fore.GREEN + '[+]Done!' + Style.RESET_ALL)
      print(Fore.CYAN + '[*]Removing Deprecated Packages...' + Style.RESET_ALL)
      os.system('sudo apt autoremove')
      print(Fore.GREEN + '[+]Done!' + Style.RESET_ALL)
      print(Fore.CYAN + '[*]Updating Local Git Clone...' + Style.RESET_ALL)
      os.system('git pull origin master')
      print(Fore.GREEN + '[+]Done!' + Style.RESET_ALL)
      logwrite('--[*]Successfully Updated Packages @ ' + timecheck() + '--')
    except:
      print(Fore.RED + '[*]Error Updating Packages...' + Style.RESET_ALL)
      logwrite('--[*]Error Updating Packages @ ' + timecheck() + '--')
    wait()
  elif in_put == 'L' or in_put == 'l':
    os.chdir(root)
    print(Fore.CYAN + '[*]Reading CHANGELOG.md...' + Style.RESET_ALL)
    logwrite('--[*]Reading CHANGELOG.md @ ' + timecheck() + Style.RESET_ALL)
    os.system('more CHANGELOG.md')
    wait()
  elif in_put == 'X' or in_put == 'x':
    print(Fore.CYAN + '[*]Killing KITT...' + Style.RESET_ALL)
    print(Fore.RED + '[*]Bye Bye!' + Style.RESET_ALL)
    logwrite('--[*]Log Closed @ ' + timecheck() + '--')
    exit()
  home()

home()
"""
