#python3
import os
from colorama import Fore, Style
from gpiozero import LED, Button, OutputDevice

pins = {
  '0': False,
  '1': False,
  '2': False,
  '3': False,
  '4': False,
  '5': False,
  '6': False,
  '7': False,
  '8': False,
  '9': False,
  '10': False,
  '11': False,
  '12': False,
  '13': False,
  '14': False,
  '15': False,
  '16': False,
  '17': False,
  '18': False,
  '19': False,
  '20': False,
  '21': False,
  '22': False,
  '23': False,
  '24': False,
  '25': False,
  '26': False,
  '27': False,
}

pins_sep = {
  '0': OutputDevice(0),
  '1': OutputDevice(1),
  '2': OutputDevice(2),
  '3': OutputDevice(3),
  '4': OutputDevice(4),
  '5': OutputDevice(5),
  '6': OutputDevice(6),
  '7': OutputDevice(7),
  '8': OutputDevice(8),
  '9': OutputDevice(9),
  '10': OutputDevice(10),
  '11': OutputDevice(11),
  '12': OutputDevice(12),
  '13': OutputDevice(13),
  '14': OutputDevice(14),
  '15': OutputDevice(15),
  '16': OutputDevice(16),
  '17': OutputDevice(17),
  '18': OutputDevice(18),
  '19': OutputDevice(19),
  '20': OutputDevice(20),
  '21': OutputDevice(21),
  '22': OutputDevice(22),
  '23': OutputDevice(23),
  '24': OutputDevice(24),
  '25': OutputDevice(25),
  '26': OutputDevice(26),
  '27': OutputDevice(27),
}

pins_lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27']

def wait():
  wait = input("PRESS ENTER TO CONTINUE")

def status(pin):
  y = list(pins.values())
  if str(y[int(pin)]) == 'False':
    stat = Fore.RED + 'Off' + Style.RESET_ALL
  else:
    stat = Fore.GREEN + 'On ' + Style.RESET_ALL
  return stat

def display_pins():
  print('||=================================||')
  print('||' + Fore.CYAN + '3V3' + Style.RESET_ALL + '          (1) (2)  ' + Fore.YELLOW + '5V' + Style.RESET_ALL + '         ||')
  print('||' + Fore.GREEN + 'GPIO2:  ' + Style.RESET_ALL + str(status(2)) + '  (3) (4)  ' + Fore.YELLOW + '5V' + Style.RESET_ALL + '         ||')
  print('||' + Fore.GREEN + 'GPIO3:  ' + Style.RESET_ALL + str(status(3)) + '  (5) (6)  ' + Fore.BLACK + Style.BRIGHT +  'GND' + Style.RESET_ALL + '        ||')
  print('||' + Fore.GREEN + 'GPIO4:  ' + Style.RESET_ALL + str(status(4)) + '  (7) (8)  ' + Fore.GREEN + 'GPIO14: ' + Style.RESET_ALL + str(status(14)) + '||')
  print('||' + Fore.BLACK + Style.BRIGHT + 'GND' + Style.RESET_ALL + '          (9) (10) ' + Fore.GREEN + 'GPIO15: ' + Style.RESET_ALL + str(status(15)) + '||')
  print('||' + Fore.GREEN + 'GPIO17: ' + Style.RESET_ALL + str(status(17)) + ' (11) (12) ' + Fore.GREEN + 'GPIO18: ' + Style.RESET_ALL + str(status(18)) + '||')
  print('||' + Fore.GREEN + 'GPIO27: ' + Style.RESET_ALL + str(status(27)) + ' (13) (14) ' + Fore.BLACK + Style.BRIGHT + 'GND' + Style.RESET_ALL + '        ||')
  print('||' + Fore.GREEN + 'GPIO22: ' + Style.RESET_ALL + str(status(22)) + ' (15) (16) ' + Fore.GREEN + 'GPIO23: ' + Style.RESET_ALL + str(status(23)) + '||')
  print('||' + Fore.CYAN + '3V3' + Style.RESET_ALL + '         (17) (18) ' + Fore.GREEN + 'GPIO24: ' + Style.RESET_ALL + str(status(24)) + '||')
  print('||' + Fore.GREEN + 'GPIO10: ' + Style.RESET_ALL + str(status(10)) + ' (19) (20) ' + Fore.BLACK + Style.BRIGHT + 'GND' + Style.RESET_ALL + '        ||')
  print('||' + Fore.GREEN + 'GPIO9:  ' + Style.RESET_ALL + str(status(9)) + ' (21) (22) ' + Fore.GREEN + 'GPIO25: ' + Style.RESET_ALL + str(status(25)) + '||')
  print('||' + Fore.GREEN + 'GPIO11: ' + Style.RESET_ALL + str(status(11)) + ' (23) (24) ' + Fore.GREEN + 'GPIO8:  ' + Style.RESET_ALL + str(status(8)) + '||')
  print('||' + Fore.BLACK + Style.BRIGHT + 'GND' + Style.RESET_ALL + '         (25) (26) ' + Fore.GREEN + 'GPIO7:  ' + Style.RESET_ALL + str(status(7)) + '||')
  print('||' + Fore.GREEN + 'GPIO0:  ' + Style.RESET_ALL + str(status(0)) + ' (27) (28) ' + Fore.GREEN + 'GPIO1:  ' + Style.RESET_ALL + str(status(1)) + '||')
  print('||' + Fore.GREEN + 'GPIO5:  ' + Style.RESET_ALL + str(status(5)) + ' (29) (30) ' + Fore.BLACK + Style.BRIGHT + 'GND' + Style.RESET_ALL + '        ||')
  print('||' + Fore.GREEN + 'GPIO6:  ' + Style.RESET_ALL + str(status(6)) + ' (31) (32) ' + Fore.GREEN + 'GPIO12: ' + Style.RESET_ALL + str(status(12)) + '||')
  print('||' + Fore.GREEN + 'GPIO13: ' + Style.RESET_ALL + str(status(13)) + ' (33) (34) ' + Fore.BLACK + Style.BRIGHT + 'GND' + Style.RESET_ALL + '        ||')
  print('||' + Fore.GREEN + 'GPIO19: ' + Style.RESET_ALL + str(status(19)) + ' (35) (36) ' + Fore.GREEN + 'GPIO16: ' + Style.RESET_ALL + str(status(16)) + '||')
  print('||' + Fore.GREEN + 'GPIO26: ' + Style.RESET_ALL + str(status(26)) + ' (37) (38) ' + Fore.GREEN + 'GPIO20: ' + Style.RESET_ALL + str(status(20)) + '||')
  print('||' + Fore.BLACK + Style.BRIGHT + 'GND' + Style.RESET_ALL + '         (39) (40) ' + Fore.GREEN + 'GPIO21: ' + Style.RESET_ALL + str(status(21)) + '||')
  print('||=================================||')
display_pins()

def edit_pins():
  pin = input(Fore.CYAN + "[*]Enter pin GPIO# or 'q' to exit: " + Style.RESET_ALL)
  if pin == 'q':
    exit()
  elif pin in pins_lst:
    c = input(Fore.CYAN + "[*][E]nable or [D]isable pin?: " + Style.RESET_ALL)
    if c == 'E' or c == 'e':
      pins[str(pin)] = True
      pins_sep[str(pin)].on()
    elif c == 'D' or 'd':
      pins[str(pin)] = False
      pins_sep[str(pin)].off()
    display_pins()
    edit_pins()
  else:
    print(Fore.RED + '[*]Invalid GPIO Pin!' + Style.RESET_ALL)
    wait()
    display_pins()
    edit_pins()

edit_pins()
