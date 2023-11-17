# ZTE Home assistant addon
**ZTE Home assistant addon**

Supported models : 

```
MC801A
MC889
MC888
```

![alt tag](https://github.com/Kajkac/ZTE-MC801A-Home-assistant/blob/master/ztemc801av2.png?raw=true?)

You can add home assistant sensors and SMS parsing from Zte MC801A router


**UPDATE : modified configuration to support new versions of Home assistant**

1. Add command line merge directory : command_line: !include_dir_merge_list command_line/ to configuration.yaml
2. Adjust sensors.py
3. Add command_line directory from repo
4. Comment out ZTE switches
5. Restart and test


## How to use

You need to create folder inside Home Assistant (under ```/root/config/``` ) named : 

```
 python_scripts
 sensors
 switch
```

After that you need to add to ```configuration.yaml``` : 

```
sensor: !include_dir_merge_list sensors/
switch: !include_dir_merge_list switch/
command_line: !include_dir_merge_list command_line/ to configuration.yaml
```

in file ```zte_tool.py``` you need to replace ip and password with your own values: 

```
zteInstance = zteRouter("IP OF ROUTER", "PASSWORD")
```

After all that reboot HA and all sensors  in Home assistant will be created

**SMS SENDER : (for anyone who has like me need to send sms-s after you spend your data plan, or you just need sms :)**

Edit lines in ```zte_tool.py``` need for sending sms :

```
phoneNumber = 'PHONENUMBER' # enter phone number here
message = 'MESSAGE' # enter your message here
zteInstance = zteRouter("192.168.0.1", "PASSWORD") # enter your router IP nad password here
```

Switch for send (you can create that from switches)

![alt tag](https://github.com/Kajkac/ZTE-MC801A-Home-assistant/blob/master/ztemc801av2SMS.png?raw=true)

Home assistant part : 

Look in switches configuration...

Automation for send SMS (you can put to ```automations.yaml```): are in repo as yaml with clean and reboot automations


**UPDATE : modified configuration to support new versions of Home assistant**

From 2023.8.0 Command line is moving so you need to adjust the configuration like 





**FURTHER INFO : I switch all to python and next step is to try to pack it like Hassio addon or integration, but for now this is functioning for me, anyone wanna contribute u can use this code and expand the funcionalities, like i use lot of code from guys bellow to achieve any functionalites so big thanks to them to share code.**

**And also i will try to pull all the parameter out of onfiguration files so that all stuff will be at one place.**


**Special thanks to:**

```
https://github.com/ngarafol - for providig fixes along the way to this repo

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
```