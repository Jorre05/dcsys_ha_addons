#!/bin/bash
echo `date`": Plug $1 to ${2,,}" >> /tmp/smartplug.log
PLUG=`echo $1|cut -c 1-4`_`echo $1|cut -c 5-6`
#wget -q -O - --timeout 7 "http://$1.struyve.local/cm?cmnd=Power%20$2" 1>>/tmp/smartplug.log 2>>/tmp/smartplug.log&
if [[ "$1" == *"plug"* ]]; then
	wget --user admin --password Abc123 -q -O - --timeout 7 --post-data "" "http://$1.struyve.lan/switch/${PLUG}_relais/turn_"${2,,} 1>>/tmp/smartplug.log 2>>/tmp/smartplug.log&
else
	wget --user admin --password Abc123 -q -O - --timeout 7 --post-data "" "http://esp-dimmer-boiler.struyve.lan/light/dimmer_boiler_output/turn_"${2,,} 1>>/tmp/smartplug.log 2>>/tmp/smartplug.log&
fi
