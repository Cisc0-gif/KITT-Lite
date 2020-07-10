#! /bin/bash

figlet -f slant ' SSH_ENCR7PT '
echo "============================================================="
echo ":SSH_E: Creating User sshlogin, don't leave password blank!"
sudo useradd sshlogin
echo ":SSH_E: User sshlogin added!"
sudo curl https://pastebin.com/raw/cpvnkCp4 > /etc/ssh/sshd_config
echo ':SSH_E: ListenAddress set to 127.0.0.1'
echo ':SSH_E: Port set to 43594!'
echo ':SSH_E: PasswordAuthentication Disabled!'
echo ':SSH_E: RootLogin Disabled!'
echo ':SSH_E: BlankPasswords Disabled!'
echo ':SSH_E: Login to sshlogin with password you set...'
read -p 'PRESS ENTER TO CONTINUE' e
su sshlogin
ssh-keygen
echo ':SSH_E: SSH RSA Keys Generated!'
echo ':SSH_E: Copy key without .pub extension to remote systems and use to login with user name sshlogin at port 43594'
echo ':SSH_E: Ex. ssh -i fp/to/id_rsa sshlogin@IP/HOSTNAME -p 43595'
echo ':SSH_E: SSH Encryption & Authentication Setup Complete!'
read -p 'PRESS ENTER TO CONTINUE' e
