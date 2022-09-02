# ZTE-MC801A
ZTE MC801A Home assistant addon

![alt tag](https://github.com/Kajkac/ZTE-MC801A/blob/main/HA%20sensors.png?raw=true)

U can add home assistant sensors and SMS parsing from Zte MC801A router

U need to put PHP files to some apache server : i use home assistant repo : https://github.com/faserf/hassio-addons
and add Apache2 to HA server

After that u need to set section in both files (smslist and ztestatus) :

$ip = "IP"; // zte ip address

$password = strtoupper(hash('sha256', "XXXXXX")); // plain text password

also set proper rights for this section in smslist.php: \\\PATH so that home assistant can access to this directory

After all that create sensors in Home assistant:


sensor:
    - platform: rest
      name: ztesms
      resource: "http://IP of hosted php files/smslist.php"
      json_attributes:
        - id
        - number
        - content
      scan_interval: "00:05"
      value_template: "{{ value_json.id }}"
  
    - platform: rest
      name: zte
      resource: "http://IP of hosted php files/ztestatus.php"
      json_attributes:
        - network_type
        - lte_rsrq
        - lte_rsrp
        - cell_id
        - lte_snr
        - wan_active_channel
        - wan_active_band
        - wan_ipaddr
        - lte_multi_ca_scell_info
        - monthly_tx_bytes
        - monthly_rx_bytes
      scan_interval: "00:05"
      value_template: "{{ value_json.network_type }}"
    - platform: template
      sensors:
        1kat_temperature_attribute:
          friendly_name: "1 Kat podešena temperatura"
          unit_of_measurement: "°C"
          device_class: temperature
          value_template: "{{ state_attr('climate.haier_ac_1_kat', 'temperature') }}"
        prizemlje_temperature_attribute:
          friendly_name: "Prizemlje podešena temperatura"
          unit_of_measurement: "°C"
          device_class: temperature
          value_template: "{{ state_attr('climate.haier_ac_prizemlje', 'temperature') }}"
        zte_network_type:
          friendly_name: "Network type"
          value_template: "{{ state_attr('sensor.zte', 'network_type') }}"
        zte_wan_ipaddr:
          friendly_name: "WAN IP address"
          value_template: "{{ state_attr('sensor.zte', 'wan_ipaddr') }}"
        zte_lte_rsrq:
          friendly_name: "RSRQ"
          value_template: "{{ state_attr('sensor.zte', 'lte_rsrq') }}"
          unit_of_measurement: "dBm"
        zte_lte_rsrp:
          friendly_name: "RSRP"
          value_template: "{{ state_attr('sensor.zte', 'lte_rsrp') }}"
          unit_of_measurement: "dBm"
        zte_cell_id:
          friendly_name: "Cell ID"
          value_template: "{{ state_attr('sensor.zte', 'cell_id') |int(base=16) }}"
        zte_lte_snr:
          friendly_name: "LTE SNR"
          value_template: "{{ state_attr('sensor.zte', 'lte_snr') }}"
          unit_of_measurement: "dB"
        zte_wan_active_channel:
          friendly_name: "WAN active channel"
          value_template: "{{ state_attr('sensor.zte', 'wan_active_channel') }}"
        zte_wan_active_band:
          friendly_name: "WAN main active band"
          value_template: "{{ state_attr('sensor.zte', 'wan_active_band') }}"
        zte_lte_multi_ca_scell_info:
          friendly_name: "Multi cell info"
          value_template: "{{ state_attr('sensor.zte', 'lte_multi_ca_scell_info') }}"
        zte_lte_monthly_transfer_usage:
          friendly_name: "Monthly usage"
          value_template: '{{ ((state_attr("sensor.zte", "monthly_tx_bytes") |float + state_attr("sensor.zte", "monthly_rx_bytes") |float ) / 1024 / 1024 / 1024) | round(2) }}'
          unit_of_measurement: "GB"
        zte_lte_monthly_transfer_left:
          friendly_name: "Data left"
          value_template: '{{ ( 50 - states("sensor.zte_lte_monthly_transfer_usage") |float) | round(2) }}'
          unit_of_measurement: "GB"
        zte_lte_sms:
          friendly_name: "Last SMS"
          value_template: "{{ state_attr('sensor.ztesms', 'id') }}"
        zte_lte_sms_content:
          friendly_name: "Last SMS"
          value_template: "{{ state_attr('sensor.ztesms', 'content') }}"


