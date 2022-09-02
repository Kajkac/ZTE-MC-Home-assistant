# ZTE-MC801A Home assistant addon
ZTE MC801A Home assistant addon

![alt tag](https://github.com/Kajkac/ZTE-MC801A/blob/main/HA%20sensors.png?raw=true)

U can add home assistant sensors and SMS parsing from Zte MC801A router

U need to put PHP files to some apache server : i use home assistant repo : https://github.com/faserf/hassio-addons
and add Apache2 to HA server

After that u need to set section in both files (smslist and ztestatus) :

$ip = "IP"; // zte ip address

$password = strtoupper(hash('sha256', "XXXXXX")); // plain text password

also set proper rights for this section in smslist.php: \\\PATH so that home assistant can access to this directory

After all that create sensors in Home assistant Homeassistant_sensors.yaml

I put that to configuration.yaml


