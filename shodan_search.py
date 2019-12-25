import os

def wait():
  wait = input('PRESS ENTER TO CONTINUE')

def main():
  os.system("figlet -f slant 'Shodan_Search'")
  print('=============================================================')
  term = input('Search[E to exit]: ')
  if term == 'e' or term == 'E':
    exit()
  else:
    os.system('shodan search --fields ip_str,port,org,hostnames ' + term  + ' > ShodanSearch_' + term + '.txt')
    print('Shodan search saved to ShodanSearch_' + term + '.txt...')
    wait()
    main()

def ins():
  ins = input('Did you already install shodan with pip?[y/N]: ')
  if ins == 'y' or ins == 'Y':
    main()
  else:
    os.system('pip3 install shodan')
    wait()
    main()

op = input('Did you already upload an api_key?[y/N]: ')
if op == 'y' or op == 'Y':
  ins()
else:
  key = input('API_KEY: ')
  os.system('shodan init ' + key)
  wait()
  ins()

