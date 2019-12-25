#! /bin/bash

echo " DISHRED v1.0"
echo ===============
servive rsyslog stop
cd /var/log
shred -f -n 10 */*.log
shred -f -n 10 *.log