#! /bin/bash

hciconfig hci0 up
echo "CTRL^C to finish scan..."
hcitool -i hci0 scan --length=30
hcitool inq
echo "Look up class @ https://wwww.bluetooth.org/en-us/specification/assigned-numbers/service-discovery"
read -p "Enter MAC Address to run service scan against: " mac
sdptool browse $mac
echo "Testing if device still in range..."
l2ping $mac -c 4
echo "Initial Scan Complete!"