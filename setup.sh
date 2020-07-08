#! /bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'
user=$(whoami)

wait_func() {
  read -p "PRESS ENTER TO CONTINUE" wait
}

printf ${RED}
read -p "*RUN AS ROOT*" root
printf "${BLUE}[*]Writing File Permissions...${NC}\n"
sudo chmod -R 777 *
printf "${GREEN}[+]Done! ${BLUE} \n[*]Updating and Upgrading Packages...${NC}\n"
sudo apt-get update && sudo apt-get upgrade
printf "${GREEN}[+]Done! ${BLUE} \n[*]Making sure pip & pip3 are installed...${NC}\n"
sudo apt-get install python-pip python3-pip -y
printf "${GREEN}[+]Done! ${BLUE} \n[*]Installing Packages, Libraries, and Repos...\n"
sleep 2
printf " [*]Confirguring apt Installation Sources...${NC}\n"
sudo curl https://pastebin.com/raw/fNL6X8gt > /etc/apt/sources.list
sudo apt-get update
printf "${GREEN} [+]Sources Configured! ${BLUE} \n [*]Installing Linux Packages...${NC}\n"
sudo apt-get install figlet metasploit-framework hydra burpsuite tor beef beef-xss nmap cryptcat netcat unicornscan php maltegoce recon-ng cewl crunch redis tshark tcpdump irssi telnet ftp git apache2 ssh weevely strace gdb radare2 arp-scan dirbuster wfuzz ncrack medusa xxd coreutils exiftool masscan dirb steghide proxychains p7zip macchanger hddtemp lm-sensors postgresql sqlmap logrotate kali-linux-full btscanner bluez bluelog redfang bluesnarfer spooftooph ettercap-graphical ettercap-text-only build-essential ntfs-3g cifs.utils mount reaver aircrack-ng libcurl4-openssl-dev libpcap0.8-dev zlib1g zlib1g-dev libssl-dev john snort fierce openvas nikto wpscan mawk curl dhcpd isc-dhcp-server hostapd lighttpd mdk3 php-cgi pyrit unzip xterm openssl rfkill ufw clamav clamav-daemon kismet bully pixiewps mingw-w64 dumpzilla steghide zip -y
sudo ufw enable
sudo gem install zsteg
sudo apt-get install fail2ban openvpn dialog python3-setuptools rkhunter lynis truecrypt truecrack htop iotop -y
printf " ${BLUE}[*]Starting postgresql Service...${NC}\n"
sudo service postgresql start
printf " ${BLUE}[*]Initiating YAML Database for Metasploit-Framework...${NC}\n"
sudo msfdb init
printf " ${BLUE}[*]Installing python2 and python3 Libraries...${NC}\n"
sudo pip install -U -I pyusb
sudo pip install -U platformio
sudo pip3 install protonvpn-cli
sudo pip install -r requirements2.txt
sudo pip3 install -r requirements3.txt
read -p "[*]Do you want to initialize ProtonVPN[y/N]?: " ptnvpn
if [ $ptnvpn == 'y' -o $ptnvpn == 'Y' ]; then
  printf "${BLUE}[*]Initializing ProtonVPN...${NC}\n"
  sudo protonvpn init
  read -p "[*]Do you want to make a cronjob to start ProtonVPN on boot?[y/N]: " ptncron
  if [ $ptncron == 'y' -o $ptncron == 'Y' ]; then
    sudo crontab -l | { cat; echo "@reboot sudo protonvpn c -f"; } | sudo crontab -
    printf "${GREEN}[+]Cronjob added!${NC}\n"
  else
    printf "${BLUE}[*]Okay!...${NC}\n"
  fi
else
  printf "${BLUE}[*]Use 'sudo protonvpn init' to setup ProtonVPN later...${NC}\n"
fi
wait_func
read -p "[*]Do you want to setup a samba server?[y/N]?: " smbserv
if [ $smbserv == 'y' -o $smbserv == 'Y' ]; then
  printf "${BLUE}Installing samba...${NC}\n"
  sudo apt-get install samba samba-common-bin -y
  sudo mkdir /home/$user/INTERNAL
  echo "[INTERNAL]" | sudo tee -a /etc/samba/smb.conf
  echo "comment = SMB Share" | sudo tee -a /etc/samba/smb.conf
  echo "browseable = yes" | sudo tee -a /etc/samba/smb.conf
  echo "path = /home/$user/INTERNAL" | sudo tee -a /etc/samba/smb.conf
  echo "writeable = Yes" | sudo tee -a /etc/samba/smb.conf
  echo "create mask = 0777" | sudo tee -a /etc/samba/smb.conf
  echo "directory mask = 0777" | sudo tee -a /etc/samba/smb.conf
  echo "browseable = Yes" | sudo tee -a /etc/samba/smb.conf
  echo "public = yes" | sudo tee -a /etc/samba/smb.conf
  sudo smbpasswd -a $user
  printf "${GREEN}[+]Samba Server Configured! Use 'sudo service smbd start/stop' to start the SMB Server!${NC}\n"
  wait_func
else
  printf "${BLUE}[*]Samba Server wasn't installed!${NC}\n"
fi
printf " ${BLUE}[*]Setting Up Snort...${NC}\n"
sudo mkdir snortlogs
sudo apt-get install snort -y
printf " ${BLUE}[*]Installing OSINT Libraries...${NC}\n"
cd hg
sudo git clone https://github.com/NullArray/AutoSploit.git
cd AutoSploit
sudo chmod +x install.sh
sudo ./install.sh
cd ..
sudo git clone https://github.com/dreadlocked/Drupalgeddon2.git
cd ..
printf " ${BLUE}[*]Installing and Initializing MouseJack...${NC}\n"
sudo git clone https://github.com/BastilleResearch/mousejack.git
cd mousejack
sudo git submodule init
sudo git submodule update
cd ..
sudo git clone https://github.com/insecurityofthings/jackit.git
cd jackit
sudo pip install -r requirements.txt
sudo pip install -e .
cd ..
printf " ${BLUE}[*]Installing WifiPumpkin3...${NC}\n"
sudo systemctl stop systemd-resolved
sudo curl https://pastebin.com/raw/QEHM8UJb > /etc/systemd/resolved.conf
sudo ln -sf /run/systemd/resolve/resolv.conf /etc/resolv.conf
sudo systemctl start systemd-resolved
sudo apt-get install python3 libssl-dev libffi-dev build-essential python3-pyqt5 -y
sudo git clone https://github.com/P0cL4bs/wifipumpkin3.git
cd wifipumpkin3
sudo python3 setup.py install
cd ..
printf " ${BLUE}[*]Installing w3af...${NC}\n"
sudo git clone https://github.com/andresriancho/w3af.git
cd w3af
sudo python w3af_console
sudo bash /tmp/w3af_dependency_install.sh
cd ..
printf " ${BLUE}[*]Installing gitGraber...${NC}\n"
sudo git clone https://github.com/hisxo/gitGraber.git
cd gitGraber
sudo pip3 install -r requirements.txt
cd ..
printf " ${BLUE}[*]Installing SocialBox...${NC}\n"
sudo git clone https://github.com/TunisianEagles/SocialBox.git
cd SocialBox
sudo chmod 777 *
sudo ./install-sb.sh
cd ..
printf " ${BLUE}[*]Installing TIDoS-Framework...${NC}\n"
sudo git clone https://github.com/0xInfection/TIDoS-Framework.git
cd TIDoS-Framework
sudo chmod 777 install
sudo ./install
cd ..
printf " ${BLUE}[*]Installing Katana...${NC}\n"
sudo git clone https://github.com/adnane-X-tebbaa/Katana.git
cd Katana
sudo pip3 install -r requirements.txt
cd ..
printf " ${BLUE}[*]Installing gitHound...${NC}\n"
sudo mkdir git-hound
cd git-hound
sudo wget https://github.com/tillson/git-hound/releases/download/v1.1/git-hound_1.1_Linux_x86_64.tar.gz
sudo gunzip git-hound_1.1_Linux_x86_64.tar.gz
sudo tar xvf git-hound_1.1_Linux_x86_64.tar
sudo rm git-hound_1.1_Linux_x86_64.tar
echo "github_username: username" > config.yml
echo "github_password: password" >> config.yml
printf " ${BLUE}[*]Input your GitHub Username and Password to config.yml...${NC}\n"
cd ..
wait_func
printf " ${BLUE}[*]Installing GitRob...${NC}\n"
sudo mkdir gitrob
cd gitrob
sudo wget https://github.com/michenriksen/gitrob/releases/download/v2.0.0-beta/gitrob_linux_amd64_2.0.0-beta.zip
sudo unzip gitrob_linux_amd64_2.0.0-beta.zip
sudo rm gitrob_linux_amd64_2.0.0-beta.zip
printf " ${BLUE}[*]Input your GitHub API Token using: export GITROB_ACCESS_TOKEN='deadbeefdeadbeefdeadbeefdeadbeef' >> ~/.bashrc${NC}\n"
cd ..
wait_func
printf " ${BLUE}[*]Installing Python3 Libraries for Chromepass...${NC}\n"
cd escalate/chromepass
sudo pip3 install -r requirements.txt
cd ../..
printf " ${BLUE}[*]Installing PTF...${NC}\n"
sudo git clone https://github.com/trustedsec/ptf.git
printf " ${BLUE}[*]Installing domained...${NC}\n"
sudo git clone https://github.com/TypeError/domained.git
cd domained
sudo pip3 install -r ./ext/requirements.txt
sudo python3 domained.py --install
cd ..
printf " ${BLUE}[*]Installing Seeker...${NC}\n"
sudo git clone https://github.com/thewhiteh4t/seeker.git
cd seeker
sudo chmod 777 install.sh
sudo ./install.sh
sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
sudo unzip ngrok-stable-linux-amd64.zip
sudo rm ngrok-stable-linux-amd64.zip
cd ..
printf " ${BLUE}[*]Installing Pwnstar...${NC}\n"
sudo git clone https://github.com/SilverFoxx/PwnSTAR.git
cd PwnSTAR
sudo chmod 777 installer.sh
sudo ./installer.sh
cd ..
printf " ${BLUE}[*]Installing hate_crack...${NC}\n"
sudo git clone https://github.com/trustedsec/hate_crack.git
cd hate_crack
sudo python hate_crack.py
printf " ${RED}[!]config.json file generated! User configuration needed in /opt/KITT-Lite/hate_crack/config.json...${NC}\n"
wait_func
cd ..
printf " ${BLUE}[*]Installing Wotop...${NC}\n"
sudo git clone https://github.com/nishitm/wotop
cd wotop
sudo make
cd ..
printf " ${BLUE}[*]Installing TorghostNG...${NC}\n"
sudo git clone https://github.com/githacktools/TorghostNG.git
cd TorghostNG
sudo chmod 777 *
sudo python3 install.py
cd ..
printf " ${BLUE}[*]Installing Vulnx...${NC}\n"
sudo git clone https://github.com/anouarbensaad/vulnx.git
cd vulnx
sudo chmod 777 install.sh
sudo ./install.sh
cd ..
printf " ${BLUE}[*]Installing Brutedum...${NC}\n"
sudo git clone https://github.com/GitHackTools/BruteDum.git
printf " ${BLUE}[*]Installing Tool-X...${NC}\n"
sudo git clone https://github.com/Rajkumrdusad/Tool-X.git
cd Tool-X
sudo chmod 777 install.aex
sudo ./install.aex
cd ..
printf " ${BLUE}[*]Installing Brutal...${NC}\n"
sudo git clone https://github.com/Screetsec/Brutal.git
cd Brutal
sudo chmod 777 Brutal.sh
sudo apt-get install zenity -y
cd ..
printf " ${BLUE}[*]Installing PeekABoo & PeekABoo.exe...${NC}\n"
cd escalate
sudo git clone https://github.com/Viralmaniar/PeekABoo.git
cd PeekABoo
sudo chmod 777 peekaboo.py
cd ..
sudo mkdir PeekABoo_Portable
cd PeekABoo_Portable
sudo wget https://github.com/Viralmaniar/PeekABoo/releases/download/v1.0/peekaboo.exe
sudo wget https://github.com/Viralmaniar/PeekABoo/releases/download/v1.0/rdpd.ps1
sudo wget https://github.com/Viralmaniar/PeekABoo/releases/download/v1.0/rdpe.ps1
sudo wget https://github.com/Viralmaniar/PeekABoo/releases/download/v1.0/testconnection.ps1
cd ../..
printf " ${BLUE}[*]Installing webkiller...${NC}\n"
sudo git clone https://github.com/ultrasecurity/webkiller.git
cd webkiller
sudo pip3 install -r requirements.txt
sudo chmod 777 webkiller.py
cd ..
printf " ${BLUE}[*]Installing evil-droid...${NC}\n"
sudo git clone https://github.com/M4sc3r4n0/Evil-Droid.git
cd Evil-Droid
sudo chmod 777 evil-droid
cd ..
printf " ${BLUE}[*]Installing catchyou...${NC}\n"
sudo git clone https://github.com/thelinuxchoice/catchyou.git
cd catchyou
sudo chmod 777 catchyou.sh
cd ..
printf " ${BLUE}[*]Installing saycheese...${NC}\n"
sudo git clone https://github.com/hangetzzu/saycheese
cd saycheese
sudo chmod 777 *
cd ..
printf " ${BLUE}[*]Installing firefox_decrypt...${NC}\n"
cd escalate
sudo git clone https://github.com/Unode/firefox_decrypt.git
printf " ${BLUE}[*]Installing invoker...${NC}\n"
sudo git clone https://github.com/ivan-sincek/invoker.git
cd ..
printf " ${BLUE}[*]Installing badmod...${NC}\n"
sudo git clone https://github.com/MrSqar-Ye/BadMod.git
cd BadMod
sudo chmod 777 -R *
sudo ./INSTALL
cd ..
printf " ${BLUE}[*]Installing shellphish...${NC}\n"
sudo git clone https://github.com/thelinuxchoice/shellphish.git
cd shellphish
sudo chmod 777 shellphish.sh
cd ..
printf " ${BLUE}[*]Installing deep-explorer...${NC}\n"
sudo git clone https://github.com/blueudp/deep-explorer.git
cd deep-explorer
sudo chmod 777 *
sudo pip3 install -r requirements.txt
cd ..
printf " ${BLUE}[*]Installing hivejack...${NC}\n"
cd escalate
sudo wget https://github.com/Viralmaniar/HiveJack/releases/download/v1.0/HiveJack.exe
cd ..
printf " ${BLUE}[*]Installing nexphisher...${NC}\n"
sudo git clone https://github.com/htr-tech/nexphisher.git
cd nexphisher
sudo chmod 777 nexphisher
sudo ./setup
cd ..
printf " ${BLUE}[*]Installing userrecon...${NC}\n"
sudo git clone https://github.com/thelinuxchoice/userrecon.git
cd userrecon
sudo chmod 777 userrecon.sh
cd ..
printf " ${BLUE}[*]Installing winspy...${NC}\n"
sudo git clone https://github.com/Cyb0r9/winspy.git
cd winspy
sudo chmod 777 setup.sh
sudo chmod 777 winspy.sh
sudo ./setup.sh
cd ..
printf " ${BLUE}[*]Installing impackt Tools...${NC}\n"
cd escalate
sudo git clone https://github.com/SecureAuthCorp/impacket.git
cd impacket
sudo pip install -r requirements.txt
sudo chmod 777 setup.py
sudo ./setup.py install
cd ../..
printf " ${BLUE}[*]Installing Th3inspector...${NC}\n"
printf " ${RED}[!]Enter any number other than 1-14 to exit Th3inspector...${NC}\n"
wait_func
sudo git clone https://github.com/Moham3dRiahi/Th3inspector.git
cd Th3inspector
sudo chmod 777 install.sh
sudo ./install.sh
cd ..
printf " ${BLUE}[*]Installing win-brute-logon...${NC}\n"
cd escalate
sudo git clone https://github.com/DarkCoderSc/win-brute-logon.git
cd ..
printf " ${BLUE}[*]Installing lockphish...${NC}\n"
sudo git clone https://github.com/thelinuxchoice/lockphish.git
cd lockphish
sudo chmod 777 lockphish.sh
cd ..
printf " ${BLUE}[*]Installing evilreg...${NC}\n"
sudo git clone https://github.com/thelinuxchoice/evilreg.git
cd evilreg
sudo chmod 777 evilreg.sh
cd ..
printf " ${BLUE}[*]Installing badlnk...${NC}\n"
sudo git clone https://github.com/thelinuxchoice/badlnk.git
cd badlnk
sudo chmod 777 badlnk.sh
cd ..
printf " ${BLUE}[*]Installing BlackDir-Framework...${NC}\n"
sudo git clone https://github.com/RedVirus0/BlackDir-Framework.git
cd BlackDir-Framework
sudo pip3 install -r requirements.txt
sudo chmod 777 *
cd ..
printf " ${BLUE}[*]Installing SocialFish...${NC}\n"
sudo git clone https://github.com/UndeadSec/SocialFish.git
cd SocialFish
sudo apt-get install python3-dev -y
sudo pip3 install -r requirements.txt
printf " ${RED}[!]Set your APP_SECRET_KEY...${NC}\n"
wait_func
sudo nano core/config.py
cd ..
printf " ${BLUE}[*]Installing HeraKeylogger...${NC}\n"
sudo git clone https://github.com/UndeadSec/HeraKeylogger.git
cd HeraKeylogger
sudo pip3 install -r requirements.txt
sudo chmod 777 hera.py
cd ..
printf " ${BLUE}[*]Installing Enigma...${NC}\n"
sudo git clone https://github.com/UndeadSec/Enigma.git
cd Enigma
sudo chmod 777 enigma.py
cd ..
printf " ${BLUE}[*]Installing Idisagree Discord Bot...${NC}\n"
sudo git clone https://github.com/UndeadSec/Idisagree.git
printf " ${BLUE}[*]Installing Locator...${NC}\n"
sudo git clone https://github.com/thelinuxchoice/locator.git
cd locator
sudo chmod 777 locator.sh
cd ..
printf " ${BLUE}[*]Installing EvilApp...${NC}\n"
sudo git clone https://github.com/thelinuxchoice/EvilApp.git
cd EvilApp
sudo chmod 777 evilapp.sh
cd ..
#printf " ${BLUE}[*]Installing Skiptracer...${NC}\n"
#sudo git clone https://github.com/xillwillx/skiptracer.git
#cd skiptracer
#sudo pip install -r requirements.txt
#cd ..
printf " ${BLUE}[*]Installing covermyass...${NC}\n"
cd escalate
sudo git clone https://github.com/sundowndev/covermyass.git
cd covermyass
sudo chmod 777 covermyass
cd ../..
printf " ${BLUE}[*]Installing Leviathan...${NC}\n"
sudo git clone https://github.com/leviathan-framework/leviathan.git
cd leviathan
sudo pip install -r requirements.txt
cd ..
printf " ${BLUE}[*]Installing linset...${NC}\n"
sudo git clone https://github.com/vk496/linset.git
cd linset
sudo chmod 777 linset
cd ..
printf " ${BLUE}[*]Installing hidden-cry...${NC}\n"
sudo git clone https://github.com/sivazozo/hidden-cry.git
cd hidden-cry
sudo chmod 777 hidden-cry
sudo apt-get install mingw-w64 -y
cd ..
printf " ${BLUE}[*]Installing droidfiles...${NC}\n"
sudo git clone https://github.com/thelinuxchoice/droidfiles.git
cd droidfiles
sudo chmod 777 droidfiles.sh
cd ..
printf " ${BLUE}[*]Installing avet_fabric...${NC}\n"
sudo git clone https://github.com/govolution/avet.git
cd avet
sudo chmod 777 avet.py
sudo ./setup.sh
cd ..
printf " ${BLUE}[*]Installing Konan...${NC}\n"
sudo git clone https://github.com/m4ll0k/Konan.git
printf " ${BLUE}[*]Installing ispy...${NC}\n"
sudo git clone https://github.com/Cyb0r9/ispy.git
cd ispy
sudo chmod 777 setup.sh
sudo ./setup.sh
cd ..
printf " ${BLUE}[*]Installing ufonet...${NC}\n"
sudo git clone https://github.com/epsylon/ufonet.git
cd ufonet
sudo python3 setup.py build
cd ..
printf " ${BLUE}[*]Installing nekobot...${NC}\n"
sudo git clone https://github.com/tegal1337/NekoBotV1.git
cd NekoBotV1
sudo chmod 777 NekoBot.py
cd ..
printf " ${BLUE}[*]Installing GhostShell...${NC}\n"
sudo git clone https://github.com/ReddyyZ/GhostShell.git
printf " ${BLUE}[*]Installing Cuteit...${NC}\n"
sudo git clone https://github.com/D4Vinci/Cuteit.git
cd Cuteit
sudo chmod 777 Cuteit.py
cd ..
printf " ${BLUE}[*]Installing HomePWN...${NC}\n"
sudo git clone https://github.com/ElevenPaths/HomePWN.git
cd HomePWN
sudo ./install.sh
cd ..
printf " ${BLUE}[*]Installing Social-Engineers-Toolkit...${NC}\n"
cd phishing/SET
sudo pip3 install -r requirements.txt
sudo python3 setup.py
cd ../..
printf " ${BLUE}[*]Installing eviloffice...${NC}\n"
sudo git clone https://github.com/thelinuxchoice/eviloffice.git
printf " ${BLUE}[*]Installing FTPBruter...${NC}\n"
sudo git clone https://github.com/GitHackTools/FTPBruter.git
printf " ${BLUE}[*]Installing Gtfo...${NC}\n"
sudo git clone https://github.com/t0thkr1s/gtfo.git
printf " ${BLUE}[*]Installing TrevorC2...${NC}\n"
sudo git clone https://github.com/trustedsec/trevorc2.git
cd trevorc2
sudo pip install -r requirements.txt
cd ..
printf " ${BLUE}[*]Installing TangaLanga...${NC}\n"
sudo git clone https://github.com/elcuervo/tangalanga.git
cd tangalanga
sudo make
cd ..
printf " ${BLUE}[*]Installing CryDroid...${NC}\n"
sudo git clone https://github.com/thelinuxchoice/crydroid.git
cd crydroid
sudo chmod 777 crydroid.sh
cd ..
printf " ${BLUE}[*]Installing KatroLogger...${NC}\n"
sudo git clone https://github.com/Katrovisch/KatroLogger.git
printf " ${BLUE}[*]Installing Fast-Google-Dork-Scan...${NC}\n"
sudo git clone https://github.com/IvanGlinkin/Fast-Google-Dorks-Scan.git
cd Fast-Google-Dorks-Scan
sudo chmod 777 FGDS.sh
cd ..
printf " ${BLUE}[*]Installing EvilDLL...${NC}\n"
sudo git clone https://github.com/thelinuxchoice/evildll.git
cd evildll
sudo chmod 777 evildll.sh
cd ..
printf " ${BLUE}[*]Installing SysIntegrity...${NC}\n"
sudo git clone https://github.com/Cisc0-gif/SysIntegrity.git
printf " ${BLUE}[*]Installing Grok-Backdoor...${NC}\n"
cd escalate
sudo git clone https://github.com/deepzec/Grok-backdoor.git
cd ..
printf " ${BLUE}[*]Installing DroidTracker...${NC}\n"
sudo git clone https://github.com/thelinuxchoice/DroidTracker.git
cd DroidTracker
sudo bash install.sh
sudo chmod 777 droidtracker.sh
cd ..
printf " ${BLUE}[*]Installing OWASP-ZSC...${NC}\n"
sudo git clone https://github.com/zscproject/OWASP-ZSC.git
cd OWASP-ZSC
sudo chmod 777 installer.py
sudo ./installer.py
cd ..
printf " ${BLUE}[*]Installing ZipCracker...${NC}\n"
sudo git clone https://github.com/priyankvadaliya/Zip-Cracker-
printf " ${BLUE}[*]Installing Pompem...${NC}\n"
sudo git clone https://github.com/rfunix/Pompem.git
cd Pompem
sudo pip3 install -r requirements.txt
cd ..
printf " ${BLUE}[*]Installing hmmcookies...${NC}\n"
sudo git clone https://github.com/thelinuxchoice/hmmcookies
cd hmmcookies
sudo chmod 777 hmmcookies.sh
cd ..
printf " ${BLUE}[*]Installing mimikatz_trunk...${NC}\n"
cd escalate
sudo mkdir mimikatz_trunk
cd mimikatz_trunk
sudo wget https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20200519/mimikatz_trunk.zip
sudo unzip mimikatz_trunk.zip
sudo rm mimikatz_trunk.zip
cd ../..
printf " ${BLUE}[*]Installing Espionage...${NC}\n"
sudo git clone https://github.com/josh0xA/Espionage
cd Espionage
sudo pip3 install -r requirments.txt
cd ..
printf " ${BLUE}[*]Installing EvilNet...${NC}\n"
sudo git clone https://github.com/Matrix07ksa/EvilNet
cd EvilNet
sudo pip3 install -r requirements.txt
cd ..
printf " ${BLUE}[*]Installing SayHello...${NC}\n"
sudo git clone https://github.com/d093w1z/sayhello
cd sayhello
sudo curl https://pastebin.com/raw/RPFM5Uqn > sayhello.sh
sudo chmod 777 sayhello.sh
cd ..
printf " ${BLUE}[*]Installing Striker...${NC}\n"
sudo git clone https://github.com/s0md3v/Striker
cd Striker
sudo chmod 777 *
cd ..
printf " ${BLUE}[*]Writing Fail2Ban Configs...${NC}\n"
sudo curl https://pastebin.com/raw/gYr9pn0w > /etc/fail2ban/jail.local
sudo service fail2ban restart
printf " ${BLUE}[*]Witing Dynamic Proxychain to Proxychains Config...${NC}\n"
sudo curl https://pastebin.com/raw/PBvHvauT > /etc/proxychains.conf
printf "${GREEN}[+]Done! ${BLUE} \n[*]Updating & Upgrading Packages...${NC}\n"
sudo apt-get update && sudo apt-get upgrade
sudo apt autoremove
printf "${GREEN}[+]Done! ${BLUE} \n[*]Moving KITT-Lite Directory To /opt...${NC}\n"
sudo mkdir /opt
cd ..
sudo mv KITT-Lite /opt
printf "${GREEN}[+]Done! ${BLUE} \n[*]Writing KITT_lite.py to alias...${NC}\n"
echo "alias kittlite='sudo python3 /opt/KITT-Lite/KITT_lite.py'" >> /home/$user/.bashrc
printf "${GREEN}[+]Done! \n[+]Execute ${BLUE} 'kittlite' ${GREEN} to run KITT Lite Framework\n"
