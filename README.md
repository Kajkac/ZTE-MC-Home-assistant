# ZTE-MC801A Home assistant addon
**ZTE MC801A Home assistant addon**

![alt tag](https://github.com/Kajkac/ZTE-MC801A-Home-assistant/blob/main/ztemc801av2.png?raw=true?)

U can add home assistant sensors and SMS parsing from Zte MC801A router

U need to create folder inside Home Assistant named : python_scripts,sensors,switch

After that u need to set configuration.yaml with : 

sensor: !include_dir_merge_list sensors/
switch: !include_dir_merge_list switch/

in file zte_tool.py u need to change ip and password and put your own values: 

zteInstance = zteRouter("IP OF ROUTER", "PASSWORD")

After all that reboot HA and all sensors  in Home assistant will be created

**SMS SENDER : (for anyone ho has like me need to send sms-s after u spend your data plan, or u just need sms :)**

Edit lines in zte_tool.py need for sending sms :

phoneNumber = 'PHONENUMBER' # enter phone number here
message = 'MESSAGE' # enter your message here
zteInstance = zteRouter("192.168.0.1", "PASSWORD") # enter your router IP nad password here

Switch for send (u can create that from switches)
![alt tag](https://github.com/Kajkac/ZTE-MC801A-Home-assistant/blob/main/ztemc801av2SMS.png?raw=true)

Home assistant part : 

Look in switches configuration...

Automation for send SMS: 

alias: T-Mobile Sender
description: ""
trigger:
  - platform: state
    entity_id:
      - sensor.glances
    from: "\"Data Plan Active\""
    to: "\"Data Plan Expired\""
condition:
  - condition: state
    entity_id: sensor.glances
    state: "\"Data Plan Expired\""
action:
  - service: switch.turn_on
    data: {}
    target:
      entity_id:
        - switch.zte_sms_py
mode: single


**FURTHER INFO : I switch all to python and next step is to try to pack it like Hassio addon or integration, but for now this is functioning for me, anyone wanna contribute u can use this code and expand the funcionalities, like i use lot of code from guys bellow to achieve any functionalites so big thanks to them to share code.**

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
