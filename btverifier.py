import os
from colorama import Fore, Style

def main():
  mac = input(Fore.CYAN + '[*]Enter deivce mac to verify here: ' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Verifying Device...Enter ^C or ^Z to Move on to next step' + Style.RESET_ALL)
  os.system('l2ping ' + mac)
  print(Fore.CYAN + '[*]Browsing RfComm Channels on Device...' + Style.RESET_ALL)
  os.system('sdptool browse --tree --l2cap ' + mac + ' > rfcomm_scan.log')
  print(Fore.CYAN + "[*]RfComm Scan Saved to rfcomm_scan.log!" + Style.RESET_ALL)
  print(Fore.GREEN + "[+]You can begin using bluesnarfer with the syntax = bluesnarfer -b mac -C rfcomm channel -s TYPE/ -l/ -i/ -f name" + Style.RESET_ALL)
  exit()

check = input(Fore.CYAN + '[*]Is RfComm configured yet?[y/N]: ' + Style.RESET_ALL)
if check == 'y' or check == 'Y':
  main()
else:
  print(Fore.CYAN + '[*]Configuring RfComm...' + Style.RESET_ALL)
  os.system('mkdir -p /dev/bluetooth/rfcomm')
  os.system('mknod -m 666 /dev/bluetooth/rfcomm/0 c 216 0')
  os.system('mknod --mode=666 /dev/rfcomm0 c 216 0')
  os.system('hciconfig -i hci0 up')
  os.system('hciconfig hci0')
  wait()
  main()
