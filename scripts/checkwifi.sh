#Sourced from: https://weworkweplay.com/play/rebooting-the-raspberry-pi-when-it-loses-wireless-connection-wifi/
ping -c4 192.168.1.1 > /dev/null

if [ $? != 0 ]
then
  echo "No network connection, restarting wlan0"
  /usr/sbin/ifdown 'wlan0'
  sleep 5
  /usr/sbin/ifup --force 'wlan0'
fi

