#!/bin/bash

#USE WITH USB BOOT UBUNTU ON LOCKED WINDOWS PC

echo "Updating & Upgrading Packages..."
sudo apt-get update && sudo apt-get upgrade
echo "Intalling CHNTPW..."
sudo apt-get install chntpw
cd /media/ubuntu
ls
read -p "Input Drive Name: " drive
cd $drive/Windows/System32/config
sudo chntpw SAM
