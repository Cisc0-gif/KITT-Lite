#! /bin/bash

#repo updated every couple of days so check your RUNTIME.log from it's latest update to make sure you have the latest tools!

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'
user=$(whoami)

wait_func() {
  read -p "PRESS ENTER TO CONTINUE" wait
}

cd /opt/KITT-Lite/hg

printf "${BLUE}[*] Installing New Repos...${NC}\n"
if [ -d "AutoSploit" ]; then
  printf "${GREEN}[+] AutoSploit Installed${NC}\n"
else
  sudo git clone https://github.com/NullArray/AutoSploit.git
  cd AutoSploit
  sudo chmod +x install.sh
  sudo ./install.sh
  cd ..
fi
if [ -d "Drupalgeddon2" ]; then
  printf "${GREEN}[+] Drupalgeddon2 Installed${NC}\n"
else
  sudo git clone https://github.com/dreadlocked/Drupalgeddon2.git
fi
cd ..
if [ -d "mousejack" ]; then
  printf "${GREEN}[+] Mousejack Installed${NC}\n"
else
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
fi
if [ -d "wifipumpkin3" ]; then
  printf "${GREEN}[+] Wifipumpkin3 Installed${NC}\n"
else
  sudo systemctl stop systemd-resolved
  sudo curl https://pastebin.com/raw/QEHM8UJb > /etc/systemd/resolved.conf
  sudo ln -sf /run/systemd/resolve/resolv.conf /etc/resolv.conf
  sudo systemctl start systemd-resolved
  sudo apt-get install python3 libssl-dev libffi-dev build-essential python3-pyqt5 -y
  sudo git clone https://github.com/P0cL4bs/wifipumpkin3.git
  cd wifipumpkin3
  sudo python3 setup.py install
  cd ..
fi
if [ -d "w3af" ]; then
  printf "${GREEN}[+] w3af Installed${NC}\n"
else
  cd w3af
  sudo python w3af_console
  sudo bash /tmp/w3af_dependency_install.sh
  cd ..
fi
if [ -d "gitGraber" ]; then
  printf "${GREEN}[+] gitGraber Installed${NC}\n"
else
  sudo git clone https://github.com/hisxo/gitGraber.git
  cd gitGraber
  sudo pip3 install -r requirements.txt
  cd ..
fi
if [ -d "SocialBox" ]; then
  printf "${GREEN}[+] SocialBox Installed${NC}\n"
else
  sudo git clone https://github.com/TunisianEagles/SocialBox.git
  cd SocialBox
  sudo chmod 777 *
  sudo ./install-sb.sh
  cd ..
fi
if [ -d "TIDoS-Framework" ]; then
  printf "${GREEN}[+] TIDoS-Framework Installed${NC}\n"
else
  sudo git clone https://github.com/0xInfection/TIDoS-Framework.git
  cd TIDoS-Framework
  sudo chmod 777 install
  sudo ./install
  cd ..
fi
if [ -d "Katana" ]; then
  printf "${GREEN}[+] Katana Installed${NC}\n"
else
  sudo git clone https://github.com/adnane-X-tebbaa/Katana.git
  cd Katana
  sudo pip3 install -r requirements.txt
  cd ..
fi
if [ -d "git-hound" ]; then
  printf "${GREEN}[+] git-hound Installed${NC}\n"
else
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
fi
if [ -d "gitrob" ]; then
  printf "${GREEN}[+] GitRob Installed${NC}\n"
else
  sudo mkdir gitrob
  cd gitrob
  sudo wget https://github.com/michenriksen/gitrob/releases/download/v2.0.0-beta/gitrob_linux_amd64_2.0.0-beta.zip
  sudo unzip gitrob_linux_amd64_2.0.0-beta.zip
  sudo rm gitrob_linux_amd64_2.0.0-beta.zip
  printf " ${BLUE}[*]Input your GitHub API Token using: export GITROB_ACCESS_TOKEN='deadbeefdeadbeefdeadbeefdeadbeef' >> ~/.bashrc${NC}\n"
  cd ..
fi
if [ -d "ptf" ]; then
  printf "${GREEN}[+]PTF Installed${NC}\n"
else
  sudo git clone https://github.com/trustedsec/ptf.git
fi
if [ -d "domained" ]; then
  printf "${GREEN}[+] Domained Installed${NC}\n"
else
  sudo git clone https://github.com/TypeError/domained.git
  cd domained
  sudo pip3 install -r ./ext/requirements.txt
  sudo python3 domained.py --install
  cd ..
fi
if [ -d "seeker" ]; then
  printf "${GREEN}[+] Seeker Installed${NC}\n"
else
  sudo git clone https://github.com/thewhiteh4t/seeker.git
  cd seeker
  sudo chmod 777 install.sh
  sudo ./install.sh
  sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
  sudo unzip ngrok-stable-linux-amd64.zip
  sudo rm ngrok-stable-linux-amd64.zip
  cd ..
fi
if [ -d "PwnSTAR" ]; then
  printf "${GREEN}[+] PwnSTAR Installed${NC}\n"
else
  sudo git clone https://github.com/SilverFoxx/PwnSTAR.git
  cd PwnSTAR
  sudo chmod 777 installer.sh
  sudo ./installer.sh
  cd ..
fi
if [ -d "hate_crack" ]; then
  printf "${GREEN}[+] Hate_Crack Installed${NC}\n"
else
  sudo git clone https://github.com/trustedsec/hate_crack.git
  cd hate_crack
  sudo python hate_crack.py
  printf " ${RED}[!]config.json file generated! User configuration needed in /opt/KITT-Lite/hate_crack/config.json...${NC}\n"
  wait_func
  cd ..
fi
if [ -d "wotop" ]; then
  printf "${GREEN}[+] Wotop Installed${NC}\n"
else
  sudo git clone https://github.com/nishitm/wotop
  cd wotop
  sudo make
  cd ..
fi
if [ -d "TorghostNG" ]; then
  printf "${GREEN}[+] TorghostNG Installed${NC}\n"
else
  sudo git clone https://github.com/githacktools/TorghostNG.git
  cd TorghostNG
  sudo chmod 777 *
  sudo python3 install.py
  cd ..
fi
if [ -d "vulnx" ]; then
  printf "${GREEN}[+] VulnX Installed${NC}\n"
else
  sudo git clone https://github.com/anouarbensaad/vulnx.git
  cd vulnx
  sudo chmod 777 install.sh
  sudo ./install.sh
  cd ..
fi
if [ -d "BruteDum" ]; then
  printf "${GREEN}[+] BruteDum Installed${NC}\n"
else
  sudo git clone https://github.com/GitHackTools/BruteDum.git
fi
if [ -d "Tool-X" ]; then
  printf "${GREEN}[+] Tool-X Installed${NC}\n"
else
  sudo git clone https://github.com/Rajkumrdusad/Tool-X.git
  cd Tool-X
  sudo chmod 777 install.aex
  sudo ./install.aex
  cd ..
fi
if [ -d "Brutal" ]; then
  printf "${GREEN}[+] Brutal Installed${NC}\n"
else
  sudo git clone https://github.com/Screetsec/Brutal.git
  cd Brutal
  sudo chmod 777 Brutal.sh
  sudo apt-get install zenity -y
  cd ..
fi
cd escalate
if [ -d "PeekABoo" ]; then
  printf "${GREEN}[+] PeekABoo Installed${NC}\n"
else
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
  cd ..
fi
cd ..
if [ -d "webkiller" ]; then
  printf "${GREEN}[+] Webkiller Installed${NC}\n"
else
  sudo git clone https://github.com/ultrasecurity/webkiller.git
  cd webkiller
  sudo pip3 install -r requirements.txt
  sudo chmod 777 webkiller.py
  cd ..
fi
if [ -d "Evil-Droid" ]; then
  printf "${GREEN}[+] Evil-Droid Installed${NC}\n"
else
  sudo git clone https://github.com/M4sc3r4n0/Evil-Droid.git
  cd Evil-Droid
  sudo chmod 777 evil-droid
  cd ..
fi
if [ -d "catchyou" ]; then
  printf "${GREEN}[+] Catchyou Installed${NC}\n"
else
  sudo git clone https://github.com/jermainlaforce/catchyou.git
  cd catchyou
  sudo chmod 777 catchyou.sh
  cd ..
fi
if [ -d "saycheese" ]; then
  printf "${GREEN}[+] Saycheese Installed${NC}\n"
else
  sudo git clone https://github.com/hangetzzu/saycheese.git
  cd saycheese
  sudo chmod 777 *
  cd ..
fi
cd escalate
if [ -d "firefox_decrypt" ]; then
  printf "${GREEN}[+] Firefox_Decrypt Installed${NC}\n"
else
  sudo git clone https://github.com/Unode/firefox_decrypt.git
fi
if [ -d "invoker" ]; then
  printf "${GREEN}[+] Invoker Installed${NC}\n"
else
  sudo git clone https://github.com/ivan-sincek/invoker.git
fi
cd ..
if [ -d "BadMod" ]; then
  printf "${GREEN}[+] Badmod Installed${NC}\n"
else
  sudo git clone https://github.com/MrSqar-Ye/BadMod.git
  cd BadMod
  sudo chmod 777 -R *
  sudo ./INSTALL
  cd ..
fi
if [ -d "shellphish" ]; then
  printf "${GREEN}[+] Shellphish Installed${NC}\n"
else
  sudo git clone https://github.com/suljot/shellphish.git
  cd shellphish
  sudo chmod 777 shellphish.sh
  cd ..
fi
if [ -d "deep-explorer" ]; then
  printf "${GREEN}[+] Deep-Explorer Installed${NC}\n"
else
  sudo git clone https://github.com/blueudp/deep-explorer.git
  cd deep-explorer
  sudo chmod 777 *
  sudo pip3 install -r requirements.txt
  cd ..
fi
cd escalate
if [ -f "HiveJack.exe" ]; then
  printf "${GREEN}[+] Hivejack Installed${NC}\n"
else
  sudo wget https://github.com/Viralmaniar/HiveJack/releases/download/v1.0/HiveJack.exe
fi
cd ..
if [ -d "nexphisher" ]; then
  printf "${GREEN}[+] Nexphisher Installed${NC}\n"
else
  sudo git clone https://github.com/htr-tech/nexphisher.git
  cd nexphisher
  sudo chmod 777 nexphisher
  sudo ./setup
  cd ..
fi
if [ -d "userrecon" ]; then
  printf "${GREEN}[+] Userrecon Installed${NC}\n"
else
  sudo git clone https://github.com/wishihab/userrecon.git
  cd userrecon
  sudo chmod 777 userrecon.sh
  cd ..
fi
if [ -d "winspy" ]; then
  printf "${GREEN}[+] Winspy Installed${NC}\n"
else
  sudo git clone https://github.com/Cyb0r9/winspy.git
  cd winspy
  sudo chmod 777 setup.sh
  sudo chmod 777 winspy.sh
  sudo ./setup.sh
  cd ..
fi
cd escalate
if [ -d "impacket" ]; then
  printf "${GREEN}[+] Impacket Installed${NC}\n"
else
  sudo git clone https://github.com/SecureAuthCorp/impacket.git
  cd impacket
  sudo pip install -r requirements.txt
  sudo chmod 777 setup.py
  sudo ./setup.py install
  cd ..
fi
cd ..
if [ -d "Th3inspector" ]; then
  printf "${GREEN}[+] Th3inspector Installed${NC}\n"
else
  printf " ${RED}[!]Enter any number other than 1-14 to exit Th3inspector...${NC}\n"
  wait_func
  sudo git clone https://github.com/Moham3dRiahi/Th3inspector.git
  cd Th3inspector
  sudo chmod 777 install.sh
  sudo ./install.sh
  cd ..
fi
cd escalate
if [ -d "win-brute-logon" ]; then
  printf "${GREEN}[+] Win-brute-logon Installed${NC}\n"
else
  sudo git clone https://github.com/DarkCoderSc/win-brute-logon.git
fi
cd ..
if [ -d "lockphish" ]; then
  printf "${GREEN}[+] Lockphish Installed${NC}\n"
else
  sudo git clone https://github.com/JasonJerry/lockphish.git
  cd lockphish
  sudo chmod 777 lockphish.sh
  cd ..
fi
if [ -d "evilreg" ]; then
  printf "${GREEN}[+] Evilreg Installed${NC}\n"
else
  sudo git clone https://github.com/8L4NK/evilreg.git
  cd evilreg
  sudo chmod 777 evilreg.sh
  cd ..
fi
if [ -d "badlnk" ]; then
  printf "${GREEN}[+] Badlnk Installed${NC}\n"
else
  sudo git clone https://github.com/VikasVarshney/badlnk.git
  cd badlnk
  sudo chmod 777 badlnk.sh
  cd ..
fi
if [ -d "BlackDir-Framework" ]; then
  printf "${GREEN}[+] BlackDir-Framework Installed${NC}\n"
else
  sudo git clone https://github.com/RedVirus0/BlackDir-Framework.git
  cd BlackDir-Framework
  sudo pip3 install -r requirements.txt
  sudo chmod 777 *
  cd ..
fi
if [ -d "SocialFish" ]; then
  printf "${GREEN}[+] SocialFish Installed${NC}\n"
else
  sudo git clone https://github.com/UndeadSec/SocialFish.git
  cd SocialFish
  sudo apt-get install python3-dev -y
  sudo pip3 install -r requirements.txt
  printf " ${RED}[!]Set your APP_SECRET_KEY...${NC}\n"
  wait_func
  sudo nano core/config.py
  cd ..
fi
if [ -d "HeraKeylogger" ]; then
  printf "${GREEN}[+] HeraKeylogger Installed${NC}\n"
else
  sudo git clone https://github.com/UndeadSec/HeraKeylogger.git
  cd HeraKeylogger
  sudo pip3 install -r requirements.txt
  sudo chmod 777 hera.py
  cd ..
fi
if [ -d "Enigma" ]; then
  printf "${GREEN}[+] Enigma Installed${NC}\n"
else
  sudo git clone https://github.com/UndeadSec/Enigma.git
  cd Enigma
  sudo chmod 777 enigma.py
  cd ..
fi
if [ -d "Idisagree" ]; then
  printf "${GREEN}[+] Idisagree Installed${NC}\n"
else
  sudo git clone https://github.com/UndeadSec/Idisagree.git
fi
if [ -d "locator" ]; then
  printf "${GREEN}[+] Locator Installed${NC}\n"
else
  sudo git clone https://github.com/yuhisern7/locator
  cd locator
  sudo chmod 777 locator.sh
  cd ..
fi
if [ -d "EvilApp" ]; then
  printf "${GREEN}[+] EvilApp Installed${NC}\n"
else
  sudo git clone https://github.com/Ro9ueAdmin/EvilApp.git
  cd EvilApp
  sudo chmod 777 evilapp.sh
  cd ..
fi
#if [ -d "skiptracer" ]; then
#  printf "${GREEN}[+] Skiptracer Installed${NC}\n"
#else
  #sudo git clone https://github.com/xillwillx/skiptracer.git
  #cd skiptracer
  #sudo pip install -r requirements.txt
  #cd ..
#fi
cd escalate
if [ -d "covermyass" ]; then
  printf "${GREEN}[+] Covermyass Installed${NC}\n"
else
  sudo git clone https://github.com/sundowndev/covermyass.git
  cd covermyass
  sudo chmod 777 covermyass
  cd ..
fi
cd ..
if [ -d "leviathan" ]; then
  printf "${GREEN}[+] Leviathan Installed${NC}\n"
else
  sudo git clone https://github.com/leviathan-framework/leviathan.git
  cd leviathan
  sudo pip install -r requirements.txt
  cd ..
fi
if [ -d "linset" ]; then
  printf "${GREEN}[+] Linset Installed${NC}\n"
else
  sudo git clone https://github.com/vk496/linset.git
  cd linset
  sudo chmod 777 linset
  cd ..
fi
if [ -d "hidden-cry" ]; then
  printf "${GREEN}[+] Hidden-cry Installed${NC}\n"
else
  sudo git clone https://github.com/sivazozo/hidden-cry.git
  cd hidden-cry
  sudo chmod 777 hidden-cry
  sudo apt-get install mingw-w64 -y
  cd ..
fi
if [ -d "droidfiles" ]; then
  printf "${GREEN}[+] Droidfiles Installed${NC}\n"
else
  sudo git clone https://github.com/vaginessa/droidfiles.git
  cd droidfiles
  sudo chmod 777 droidfiles.sh
  cd ..
fi
if [ -d "avet" ]; then
  printf "${GREEN}[+] Avet_Fabric Installed${NC}\n"
else
  sudo git clone https://github.com/govolution/avet.git
  cd avet
  sudo chmod 777 avet.py
  sudo ./setup.sh
  cd ..
fi
if [ -d "Konan" ]; then
  printf "${GREEN}[+] Konan Installed${NC}\n"
else
  sudo git clone https://github.com/m4ll0k/Konan.git
fi
if [ -d "ispy" ]; then
  printf "${GREEN}[+] Ispy Installed${NC}\n"
else
  sudo git clone https://github.com/Cyb0r9/ispy.git
  cd ispy
  sudo chmod 777 setup.sh
  sudo ./setup.sh
  cd ..
fi
if [ -d "ufonet" ]; then
  printf "${GREEN}[+] Ufonet Installed${NC}\n"
else
  sudo git clone https://github.com/epsylon/ufonet.git
  cd ufonet
  sudo python3 setup.py build
  cd ..
fi
if [ -d "NekoBotV1" ]; then
  printf "${GREEN}[+] NekoBotV1 Installed${NC}\n"
else
  sudo git clone https://github.com/tegal1337/NekoBotV1.git
  cd NekoBotV1
  sudo chmod 777 NekoBot.py
  cd ..
fi
if [ -d "GhostShell" ]; then
  printf "${GREEN}[+] GhostShell Installed${NC}\n"
else
  sudo git clone https://github.com/ReddyyZ/GhostShell.git
fi
if [ -d "Cuteit" ]; then
  printf "${GREEN}[+] Cuteit Installed${NC}\n"
else
  sudo git clone https://github.com/D4Vinci/Cuteit.git
  cd Cuteit
  sudo chmod 777 Cuteit.py
  cd ..
fi
if [ -d "HomePWN" ]; then
  printf "${GREEN}[+] HomePWN Installed${NC}\n"
else
  sudo git clone https://github.com/ElevenPaths/HomePWN.git
  cd HomePWN
  sudo ./install.sh
  cd ..
fi
if [ -d "eviloffice" ]; then
  printf "${GREEN}[+] Eviloffice Installed${NC}\n"
else
  sudo git clone https://github.com/srnframe/eviloffice.git
fi
if [ -d "FTPBruter" ]; then
  printf "${GREEN}[+] FTPBruter Installed${NC}\n"
else
  sudo git clone https://github.com/GitHackTools/FTPBruter.git
fi
if [ -d "gtfo" ]; then
  printf "${GREEN}[+] Gtfo Installed${NC}\n"
else
  sudo git clone https://github.com/t0thkr1s/gtfo.git
fi
if [ -d "trevorc2" ]; then
  printf "${GREEN}[+] TrevorC2 Installed${NC}\n"
else
  sudo git clone https://github.com/trustedsec/trevorc2.git
  cd trevorc2
  sudo pip install -r requirements.txt
  cd ..
fi
if [ -d "tangalanga" ]; then
  printf "${GREEN}[+] TangaLanga Installed${NC}\n"
else
  sudo git clone https://github.com/elcuervo/tangalanga.git
  cd tangalanga
  sudo make
  cd ..
fi
if [ -d "crydroid" ]; then
  printf "${GREEN}[+] CryDroid Installed${NC}\n"
else
  sudo git clone https://github.com/benniraj25/crydroid.git
  cd crydroid
  sudo chmod 777 crydroid.sh
  cd ..
fi
if [ -d "KatroLogger" ]; then
  printf "${GREEN}[+] KatroLogger Installed${NC}\n"
else
  sudo git clone https://github.com/Katrovisch/KatroLogger.git
fi
if [ -d "Fast-Google-Dorks-Scan" ]; then
  printf "${GREEN}[+] Fast-Google-Dork-Scan Installed${NC}\n"
else
  sudo git clone https://github.com/IvanGlinkin/Fast-Google-Dorks-Scan.git
  cd Fast-Google-Dorks-Scan
  sudo chmod 777 FGDS.sh
  cd ..
fi
if [ -d "evildll" ]; then
  printf "${GREEN}[+] EvilDLL Installed${NC}\n"
else
  sudo git clone https://github.com/CrackerCat/evildll.git
  cd evildll
  sudo chmod 777 evildll.sh
  cd ..
fi
if [ -d "SysIntegrity" ]; then
  printf "${GREEN}[+] SysIntegrity Installed${NC}\n"
else
  sudo git clone https://github.com/Cisc0-gif/SysIntegrity.git
fi
cd escalate
if [ -d "Grok-backdoor" ]; then
  printf "${GREEN}[+] Grok-backdoor Installed${NC}\n"
else
  sudo git clone https://github.com/deepzec/Grok-backdoor.git
fi
cd ..
if [ -d "DroidTracker" ]; then
  printf "${GREEN}[+] DroidTracker Installed${NC}\n"
else
  sudo git clone https://github.com/indexnotfound404/DroidTracker.git
  cd DroidTracker
  sudo bash install.sh
  sudo chmod 777 droidtracker.sh
  cd ..
fi
if [ -d "OWASP-ZSC" ]; then
  printf "${GREEN}[+] OWASP-ZSC Installed${NC}\n"
else
  sudo git clone https://github.com/zscproject/OWASP-ZSC.git
  cd OWASP-ZSC
  sudo chmod 777 installer.py
  sudo ./installer.py
  cd ..
fi
if [ -d "Zip-Cracker-" ]; then
  printf "${GREEN}[+] Zip-Cracker Installed${NC}\n"
else
  sudo git clone https://github.com/priyankvadaliya/Zip-Cracker-.git
fi
if [ -d "Pompem" ]; then
  printf "${GREEN}[+] Pompem Installed${NC}\n"
else
  sudo git clone https://github.com/rfunix/Pompem.git
  cd Pompem
  sudo pip3 install -r requirements.txt
  cd ..
fi
if [ -d "hmmcookies" ]; then
  printf "${GREEN}[+] hmmcookies Installed${NC}\n"
else
  sudo git clone https://github.com/swagkarna/hmmcookies.git
  cd hmmcookies
  sudo chmod 777 hmmcookies.sh
  cd ..
fi
cd escalate
if [ -d "mimikatz_trunk" ]; then
  printf "${GREEN}[+] mimikatz_trunk Installed${NC}\n"
else
  sudo mkdir mimikatz_trunk
  cd mimikatz_trunk
  sudo wget https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20200519/mimikatz_trunk.zip
  sudo unzip mimikatz_trunk.zip
  sudo rm mimikatz_trunk.zip
  cd ..
fi
cd ..
if [ -d "Espionage" ]; then
  printf "${GREEN}[+] Espionage Installed${NC}\n"
else
  sudo git clone https://github.com/josh0xA/Espionage
  cd Espionage
  sudo pip3 install -r requirments.txt
  cd ..
fi
if [ -d "EvilNet" ]; then
  printf "${GREEN}[+] EvilNet Installed${NC}\n"
else
  sudo git clone https://github.com/Matrix07ksa/EvilNet
  cd EvilNet
  sudo pip3 install -r requirements.txt
  cd ..
fi
if [ -d "sayhello" ]; then
  printf "${GREEN}[+] SayHello Installed${NC}\n"
else
  sudo git clone https://github.com/d093w1z/sayhello
  cd sayhello
  sudo curl https://pastebin.com/raw/RPFM5Uqn > sayhello.sh
  sudo chmod 777 *
  cd ..
fi
if [ -d "Striker" ]; then
  printf "${GREEN}[+] Striker Installed${NC}\n"
else
  sudo git clone https://github.com/s0md3v/Striker
  cd Striker 
  sudo chmod 777 *
  cd ..
fi
if [ -d "ADB-Toolkit" ]; then
  printf "${GREEN}[+] ADB-Toolkit Installed${NC}\n"
else
  sudo git clone https://github.com/ASHWIN990/ADB-Toolkit
  cd ADB-Toolkit
  sudo chmod 777 install.sh
  sudo ./install.sh -i
  cd ..
fi
if [ -d "trape" ]; then
  printf "${GREEN}[+] Trape v2.0 Installed${NC}\n"
else
  sudo git clone https://github.com/jofpin/trape.git
fi
if [ -d "Ninja" ]; then
  printf "${GREEN}[+] NinjaC2 Installed${NC}\n"
else
  sudo git clone https://github.com/ahmedkhlief/Ninja.git
fi
if [ -d "Email-Extract" ]; then
  printf "${GREEN}[+] Email-Extract Installed${NC}\n"
else
  sudo git clone https://github.com/Cisc0-gif/Email-Extract.git
fi
if [ -d "ntlm_theft" ]; then
  printf "${GREEN}[+] ntlm_theft Installed${NC}\n"
else
  sudo git clone https://github.com/Greenwolf/ntlm_theft.git
  cd ntlm_theft
  sudo chmod 777 *
  cd ..
fi
if [ -d "HTTP-revshell" ]; then
  printf "${GREEN}[+] HTTP-revshell Installed${NC}\n"
else
  sudo git clone https://github.com/3v4Si0N/HTTP-revshell.git
  cd HTTP-revshell
  sudo python3 -m pip install -r requirements.txt
  cd ..
fi
if [ -d "nuclei" ]; then
  printf "${GREEN}[+] nuclei Installed${NC}\n"
else
  sudo git clone https://github.com/projectdiscovery/nuclei.git
  cd nuclei/cmd/nuclei
  sudo go build
  sudo mv nuclei /usr/local/bin
  cd ..
fi
if [ -d "wacker" ]; then
  printf "${GREEN}[+] wacker Installed${NC}\n"
else
  sudo git clone https://github.com/blunderbuss-wctf/wacker
fi
if [ -d "bypass-firewalls-by-DNS-history" ]; then
  printf "${GREEN}[+] bypass-firewalls-by-DNS-history Installed${NC}\n"
else
  sudo git clone https://github.com/vincentcox/bypass-firewalls-by-DNS-history
  cd bypass-firewalls-by-DNS-history
  sudo chmod 777 bypass-firewalls-by-DNS-history
  sudo apt install jq
  cd ..
fi
if [ -d "c41n" ]; then
  printf "${GREEN}[+] C41N Installed${NC}\n"
else
  sudo git clone https://github.com/MS-WEB-BN/c41n.git
  cd c41n
  sudo chmod 777 install.sh
  sudo ./install.sh
  sudo chmod 777 c41n
  cd ..
fi
if [ -d "infog" ]; then
  printf "${GREEN}[+] Infog Installed${NC}\n"
else
  sudo git clone https://github.com/OffXec/infog.git
  cd infog
  sudo chmod 777 infog.sh
  cd ..
fi
printf "${GREEN}[+] All Caught Up!${NC}\n"
