#! python3
import os
import sys
from colorama import Fore, Back, Style

def wait():
  wait = input("PRESS ENTER TO CONTINUE")

domain = input(Fore.CYAN + '[*]Enter domain to scan (ip/url): ' + Style.RESET_ALL)

def main():
  os.system("figlet -f slant 'domain_sticate'")
  print('=========================================================================')
  print(Fore.CYAN + '[*]Domain: ' + Style.RESET_ALL + domain)
  print(Fore.CYAN + '[*]Pinging domain...' + Style.RESET_ALL)
  try:
    os.system('ping -c 4 ' + domain + ' > report.txt')
    print(Fore.GREEN + '[+]Domain reached!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Domain not responding!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of Ping directed to report.txt!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Running full nmap scan of domain...' + Style.RESET_ALL)
  try:
    os.system('nmap -sV -A -p 0-65535 ' + domain + ' >> report.txt')
    print(Fore.GREEN + '[+]Scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + "[*]Scan incomplete!" + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of nmap scan directed to report.txt!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Running dig nameserver scan on domain...' + Style.RESET_ALL)
  try:
    os.system('dig ' + domain + ' ns >> report.txt')
    print(Fore.GREEN + '[+]Nameserver scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Nameserver scan incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of dig scan directed to report.txt!' + Style.RESET_ALL)
  print(Fore.RED +'[*]:WARNING: Once you run this, google will read your pings as a DDoS attack and block your IP temporarily!' + Style.RESET_ALL)
  wait()
  harv = input(Fore.CYAN + "[*]Do you want to run a harvester scan?[y/N]: " + Style.RESET_ALL)
  if harv == 'y' or harv == 'Y':
    print(Fore.CYAN + "[*]Running harvester scan..." + Style.RESET_ALL)
    try:
      os.system('theHarvester -d ' + domain + ' -l 200 -b google -s -p -f ../harvester.html > ../harvest.txt')
      print(Fore.GREEN + '[+]Harvester scan complete!')
    except:
      print(Fore.RED + '[*]Harvester scan incomplete!')
    print(Fore.CYAN + '[*]Output of theHarvester directed to report.txt!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Running cewl wordlist scan...' + Style.RESET_ALL)
  try:
    os.system('cewl -w ../cewl.lst -d 7 -m 5 https://www.' + domain)
    print(Fore.GREEN + '[+]Cewl wordlist scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Cewl wordlist scan incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of Cewl directed to cewl.lst!')
  print('[*]Running nikto scan...' + Style.RESET_ALL)
  try:
    http = input(Fore.CYAN + '[*]HTT(P) or HTTP(S)?: ' + Style.RESET_ALL)
    if http == 'P':
      os.system('nikto -h http://' + domain + ' >> report.txt')
      print(Fore.GREEN + '[+]nikto scan complete!' + Style.RESET_ALL)
    else:
      os.system('nikto -h https://' + domain + ' >> report.txt')
      print(Fore.GREEN + '[+]nikto scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Nikto scan incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of nikto directed to report.txt' + Style.RESET_ALL)
  print('[*]Running sublist3r scan...' + Style.RESET_ALL)
  try:
    os.chdir('../Sublist3r')
    os.system('python sublist3r.py -d ' + domain + ' >> ../report.txt')
    print(Fore.GREEN + '[+]sublist3r scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]sublist3r scan incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of sublist3r directed to report.txt' + Style.RESET_ALL)
  os.chdir('../JoomlaScan')
  print(Fore.CYAN + '[*]Running joomlascan...' + Style.RESET_ALL)
  try:
    os.system('python joomlascan.py -u https://www.' + domain + ' >> ../report.txt')
    print(Fore.GREEN + '[+]Joomla Scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Joomla Scan incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of JoomlaScan directed to report.txt!' + Style.RESET_ALL)
  os.chdir('..')
  print(Fore.CYAN + '[*]Running email index on domain...' + Style.RESET_ALL)
  try:
    os.system('./goog-mail.py ' + domain + ' >> report.txt')
    print(Fore.GREEN + '[+]Email index complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Email index incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of goog-mail scan directed to report.txt!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Running shodan search on domain...' + Style.RESET_ALL)
  try:
    os.system('shodan search --fields ip_str,port,org,hostnames ' + domain  + ' >> report.txt')
    print(Fore.GREEN + '[+]Shodan search complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Shodan search incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of shodan scan directed to report.txt!' + Style.RESET_ALL)
  drupal = input(Fore.CYAN + '[*]Do you want to run DrupalGeddon2 to attempt a shell?[y/N]: ' + Style.RESET_ALL)
  os.chdir('Drupalgeddon2')
  if drupal == 'y' or drupal == 'Y':
    try:
      http = input(Fore.CYAN + '[*]HTT(P) or HTTP(S)?: ' + Style.RESET_ALL)
      if http == 'P':
        os.system('ruby drupalgeddon2.rb http://' + domain + ' >> report.txt')
        print(Fore.GREEN + '[+]Drupalgeddon2 attempt complete!' + Style.RESET_ALL)
      else:
        os.system('ruby drupalgeddon2.rb https://' + domain + ' >> report.txt')
        print(Fore.GREEN + '[+]Drupalgeddon2 attempt complete!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Drupalgeddon2 attemp failed!' + Style.RESET_ALL)
  os.chdir('..')
  print(Fore.CYAN + '[*]Running sqlmap scan on domain...' + Style.RESET_ALL)
  try:
    os.system('sqlmap -u ' + domain  + ' >> report.txt')
    print(Fore.GREEN + '[+]Sqlmap scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Sqlmap scan incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Running dirb scan on domain...' + Style.RESET_ALL)
  try:
    http = input(Fore.CYAN + '[*]HTT(P) or HTTP(S)?: ' + Style.RESET_ALL)
    if http == 'P':
      os.system('dirb http://' + domain  + ' >> report.txt')
    else:
      os.system('dirb https://' + domain + ' >> report.txt')
    print(Fore.GREEN + '[+]dirb scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]dirb scan incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Running XSStrike scan on domain...' + Style.RESET_ALL)
  try:
    os.chdir('XSStrike')
    http = input(Fore.CYAN + '[*]HTT(P) or HTTP(S)?: ' + Style.RESET_ALL)
    if http == 'P':
      print(Fore.CYAN + '[*]Scan: BASIC' + Style.RESET_ALL)
      os.system('python3 xsstrike.py -u http://' + domain  + ' >> report.txt')
      print(Fore.CYAN + '[*]Scan: CRAWLER' + Style.RESET_ALL)
      os.system('python3 xsstrike.py -u http://' + domain + ' --crawl -l 3 -t 30 >> report.txt')
      print(Fore.CYAN + '[*]Scan: FUZZER' + Style.RESET_ALL)
      os.system('python3 xsstrike.py -u http://' + domain + ' --fuzzer -t 30 -d 1 >> report.txt')
      print(Fore.CYAN + '[*]Scan: PARAMS' + Style.RESET_ALL)
      os.system('python3 xsstrike.py -u http://' + domain + ' --params -t 30 >> report.txt')
      print(Fore.CYAN + '[*]Scan: PATH INJ' + Style.RESET_ALL)
      os.system('python3 xsstrike.py -u http://' + domain + ' --path -t 30 >> report.txt')
    else:
      print(Fore.CYAN + '[*]Scan: BASIC' + Style.RESET_ALL)
      os.system('python3 xsstrike.py -u https://' + domain  + ' >> report.txt')
      print(Fore.CYAN + '[*]Scan: CRAWLER' + Style.RESET_ALL)
      os.system('python3 xsstrike.py -u https://' + domain + ' --crawl -l 3 -t 30 >> report.txt')
      print(Fore.CYAN + '[*]Scan: FUZZER' + Style.RESET_ALL)
      os.system('python3 xsstrike.py -u https://' + domain + ' --fuzzer -t 30 -d 1 >> report.txt')
      print(Fore.CYAN + '[*]Scan: PARAMS' + Style.RESET_ALL)
      os.system('python3 xsstrike.py -u https://' + domain + ' --params -t 30 >> report.txt')
      print(Fore.CYAN + '[*]Scan: PATH INJ' + Style.RESET_ALL)
      os.system('python3 xsstrike.py -u https://' + domain + ' --path -t 30 >> report.txt')
    print(Fore.GREEN + '[+]XSStrike scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]XSStrike scan incomplete!' + Style.RESET_ALL)
  print('=========================================================================')
  print(Fore.GREEN + '[+]Domainstication Complete!' + Style.RESET_ALL)
  wait()

ins = input(Fore.CYAN + '[*]Did you run lib_install.sh?[y/N]: ' + Style.RESET_ALL)
if ins == 'y' or ins == 'Y':
  wait()
  main()
else:
  print(Fore.RED + '[*]Please run lib_install.py or KITT_INSTALLER.sh first...' + Style.RESET_ALL)
  wait()
  exit()
