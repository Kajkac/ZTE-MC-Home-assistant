# ZTE-MC801A Home assistant addon
**ZTE MC801A Home assistant addon**

![alt tag](https://github.com/Kajkac/ZTE-MC801A-Home-assistant/blob/main/ztemc801av2.png?raw=true?)

U can add home assistant sensors and SMS parsing from Zte MC801A router

U need to put PHP files to some apache server : i use home assistant repo : https://github.com/faserf/hassio-addons
and add Apache2 to HA server

After that u need to set section in both files (smslist and ztestatus) :

$ip = "IP"; // zte ip address

$password = strtoupper(hash('sha256', "XXXXXX")); // plain text password

also set proper rights for this section in smslist.php: \\\PATH so that home assistant can access to this directory

After all that create sensors in Home assistant Homeassistant_sensors.yaml

I put that to configuration.yaml

**UPDATE: for Apache part u also need to set correct rights to share/htdocsfolder : **

chmod 777 on that folders

**SMS SENDER : (for anyone ho has like me need to send sms-s after u spend your data plan, or u just need sms :)**

Switch for send
![alt tag](https://github.com/Kajkac/ZTE-MC801A/blob/main/sms1.png?raw=true)

Log:
![alt tag](https://github.com/Kajkac/ZTE-MC801A/blob/main/sms2.png?raw=true)

Home assistant part : 

configuration.yaml:

switch:
  - platform: command_line
    switches:
      zte_sms:
        friendly_name: ZTE SMS Sender
        command_on: "/usr/local/bin/python /config/python_scripts/zte_sms.py"
        value_template: >
          {{value_json.config.on}}
        icon_template: >
          {% if value_json.config.on == true %} mdi:message-alert
          {% else %} mdi:message-text-lock
          {% endif %}

zte_sms.py

Edit lines u need for sending sms :

phoneNumber = 'PHONENUMBER' # enter phone number here
message = 'MESSAGE' # enter your message here
zteInstance = zteRouter("192.168.0.1", "PASSWORD") # enter your router IP nad password here


**FURTHER INFO : When i will have time i will switch all to python and try to pack it like Hassio addon or integration, but for now this is functioning for me, anyone wanna contribute u can use this code and expand the funcionalities, like i use lot of code from guys bellow to achieve any functionalites so big thanks to them to share code.**

**And also i will try to pull all the parameter out of onfiguration files so that all stuff will be at one place.**


**Special thanks to:**

https://github.com/gediz/Superbox-Helper

https://github.com/paddy-314/zteRouterReboot/blob/1e3977979ae2dfb6bb05dc28fb9cda233174f437/README.md

paulo-correia/ZTE_API_and_Hack - for list of Requests and PHP Class

Mohammad Aghazadeh - for MD5 hash and UTF8 Encoding

Behzad Ebrahimi - for encode unicode string in "UCS2" format

gediz/trivial-tools-n-scripts/blob/superbox-hacks - for AD calculating algorithm

https://habr.com/en/post/277637/
and
http://www.bez-kabli.pl/viewtopic.php?f=12&t=62164

for providing me a solution to autheticating and parsing data from ZTE router
