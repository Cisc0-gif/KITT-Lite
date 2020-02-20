#! /bin/bash
read -p "*RUN AS ROOT*" root
echo "[*]Writing File Permissions..."
sudo chmod -R 777 *
echo "[*]Done!"
echo "[*]Making sure pip and pip3 are installed..."
sudo apt-get install python-pip python3-pip
echo "[*]Done!"
echo "[*]Running lib installer..."
sudo ./lib_install.py
echo "[+]Done!"
echo "[*]Moving KITT-Lite directory to /opt..."
sudo mkdir /opt
cd ..
sudo mv KITT-Lite /opt
echo "[+]Done!"
echo "[*]Writing KITT_lite.py to alias..."
sudo echo "alias KITTlite='sudo python3 /opt/KITT-Lite/KITT_lite.py'" >> /home/kali/.bashrc
echo "[+]Done!"
echo 'Execute "KITTlite" to run KITT Lite Framework'

