<?php
$ip = "IP"; // zte ip address

$password = strtoupper(hash('sha256', "XXXXXX")); // plain text password


$ld_url = "http://$ip/goform/goform_get_cmd_process?isTest=false&cmd=LD";
$login_url = "http://$ip/goform/goform_set_cmd_process";
$cmd_url = "http://$ip/goform/goform_get_cmd_process?isTest=false&cmd=network_type%2Crssi%2Crscp%2Crmcc%2Crmnc%2Cenodeb_id%2Clte_rsrq%2Clte_rsrp%2CZ5g_snr%2CZ5g_rsrp%2CZCELLINFO_band%2CZ5g_dlEarfcn%2Clte_ca_pcell_arfcn%2Clte_ca_pcell_band%2Clte_ca_scell_band%2Clte_ca_pcell_bandwidth%2Clte_ca_scell_info%2Clte_ca_scell_bandwidth%2Cwan_lte_ca%2Clte_pci%2CZ5g_CELL_ID%2CZ5g_SINR%2Ccell_id%2Cwan_lte_ca%2Clte_ca_pcell_band%2Clte_ca_pcell_bandwidth%2Clte_ca_scell_band%2Clte_ca_scell_bandwidth%2Clte_ca_pcell_arfcn%2Clte_ca_scell_arfcn%2Clte_multi_ca_scell_info%2Cwan_active_band%2Cnr5g_pci%2Cnr5g_action_band%2Cnr5g_cell_id%2Clte_snr%2Cecio%2Cwan_active_channel%2Cnr5g_action_channel%2Cngbr_cell_info%2Cmonthly_tx_bytes%2Cmonthly_rx_bytes%2Clte_pci%2Clte_pci_lock%2Clte_earfcn_lock%2Cwan_ipaddr%2Cwan_apn%2Cpm_sensor_mdm%2Cpm_modem_5g%2Cnr5g_pci%2Cnr5g_action_channel%2Cnr5g_action_band%2CZ5g_SINR%2CZ5g_rsrp%2Cwan_active_band%2Cwan_active_channel%2Cwan_lte_ca%2Clte_multi_ca_scell_info%2Ccell_id%2Cdns_mode%2Cprefer_dns_manual%2Cstandby_dns_manual%2Cnetwork_type%2Crmcc%2Crmnc%2Clte_rsrq%2Clte_rssi%2Clte_rsrp%2Clte_snr%2Cwan_lte_ca%2Clte_ca_pcell_band%2Clte_ca_pcell_bandwidth%2Clte_ca_scell_band%2Clte_ca_scell_bandwidth%2Clte_ca_pcell_arfcn%2Clte_ca_scell_arfcn%2Cwan_ipaddr%2Cstatic_wan_ipaddr%2Copms_wan_mode%2Copms_wan_auto_mode%2Cppp_status%2Cloginfo&multi_data=1";

// LD
$c_ld = curl_init($ld_url);
curl_setopt($c_ld, CURLOPT_RETURNTRANSFER, true);
curl_setopt($c_ld, CURLOPT_HTTPHEADER, array(
    "Host: $ip",
    "Referer: http://$ip/index.html"
));
$ld_response_string = curl_exec($c_ld);
curl_close($c_ld);
$ld_response = json_decode($ld_response_string, true);
$ld = strtoupper($ld_response['LD']);
$token = strtoupper(hash('sha256', $password.$ld));


// Auth
$login_body = "isTest=false&goformId=LOGIN&password=$token";
$c_login = curl_init($login_url);
curl_setopt($c_login, CURLOPT_POST, 1);
curl_setopt($c_login, CURLOPT_RETURNTRANSFER, true);
curl_setopt($c_login, CURLOPT_HEADER, 1);
curl_setopt($c_login, CURLOPT_HTTPHEADER, array(
    "Referer: http://$ip/index.html"
));
curl_setopt($c_login, CURLOPT_POSTFIELDS, $login_body);
$login_response = curl_exec($c_login);
preg_match_all('/^Set-Cookie:\s*([^;]*)/mi', $login_response, $matches);
$cookies = array();
foreach($matches[1] as $item) {
    parse_str($item, $cookie);
    $cookies = array_merge($cookies, $cookie);
}
curl_close($c_login);

$cookie_pass = $cookies['stok'];

// Request
$c_data = curl_init($cmd_url);
curl_setopt($c_data, CURLOPT_RETURNTRANSFER, true);
curl_setopt($c_data, CURLOPT_HTTPHEADER, array(
    "Host: $ip",
    "Referer: http://$ip/index.html",
   'Cookie: stok='.$cookie_pass
));
$data_response_string = curl_exec($c_data);
curl_close($c_data);
$data_response = json_decode($data_response_string, true);

header("Content-Type: application/json");
echo $data_response_string;
#printf($data_response_string);
exit();
?>