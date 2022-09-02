<?php
#ini_set('display_startup_errors', 1);
ini_set('display_errors', 1);
error_reporting(-1);

$ip = "IP"; // zte ip address
$password = strtoupper(hash('sha256', "XXXXX")); // plain text password

mb_internal_encoding("UTF-8");
//functions

function utf2hex($str)
{
    $l=mb_strlen($str);
    $res='';
    for ($i=0;$i<$l;$i++)
    {	
        $s = mb_substr($str,$i,1);
        $s = mb_convert_encoding($s, 'UCS-2LE', 'UTF-8');
        $s = dechex(ord(substr($s, 1, 1))*256+ord(substr($s, 0, 1)));
        if (mb_strlen($s)<4) $s = str_repeat("0",(4-mb_strlen($s))).$s;
        $res.=$s;
    }
    return $res; 
}

function hex2utf($str)
{
    $l=mb_strlen($str)/4;
    $res='';
    for ($i=0;$i<$l;$i++) $res.=html_entity_decode('&#'.hexdec(mb_substr($str,$i*4,4)).';',ENT_NOQUOTES,'UTF-8');
    return $res; 
}


$ld_url = "http://$ip/goform/goform_get_cmd_process?isTest=false&cmd=LD";
$login_url = "http://$ip/goform/goform_set_cmd_process";
$cmd_url = "http://$ip/goform/goform_get_cmd_process?isTest=false&cmd=network_type%2Crssi%2Crscp%2Crmcc%2Crmnc%2Cenodeb_id%2Clte_rsrq%2Clte_rsrp%2CZ5g_snr%2CZ5g_rsrp%2CZCELLINFO_band%2CZ5g_dlEarfcn%2Clte_ca_pcell_arfcn%2Clte_ca_pcell_band%2Clte_ca_scell_band%2Clte_ca_pcell_bandwidth%2Clte_ca_scell_info%2Clte_ca_scell_bandwidth%2Cwan_lte_ca%2Clte_pci%2CZ5g_CELL_ID%2CZ5g_SINR%2Ccell_id%2Cwan_lte_ca%2Clte_ca_pcell_band%2Clte_ca_pcell_bandwidth%2Clte_ca_scell_band%2Clte_ca_scell_bandwidth%2Clte_ca_pcell_arfcn%2Clte_ca_scell_arfcn%2Clte_multi_ca_scell_info%2Cwan_active_band%2Cnr5g_pci%2Cnr5g_action_band%2Cnr5g_cell_id%2Clte_snr%2Cecio%2Cwan_active_channel%2Cnr5g_action_channel%2Cngbr_cell_info%2Cmonthly_tx_bytes%2Cmonthly_rx_bytes&multi_data=1";
$cmd_url_sms_old = "http://$ip/goform/goform_get_cmd_process?isTest=false&cmd=sms_data_total&page=0&data_per_page=500&mem_store=1&tags=10&order_by=order+by+id+desc";
$cmd_url_sms = "http://$ip/goform/goform_get_cmd_process?cmd=sms_data_total&page=0&data_per_page=5000&mem_store=1&tags=10&order_by=order+by+id+desc";
$cmd_url_send_sms = "http://$ip/goform/goform_get_cmd_process?isTest=false&goformId=SEND_SMS&notCallback=true&Number=+385989072702&sms_time=22%3B08%3B20%3B13%3B03%3B35%3B%2B2&MessageBody=00420052005A0049004E0041&ID=-1&encode_type=GSM7_default&AD=6cafdd1e2f9042c1244a6939848c1c6c";

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

 
// Request SMS
$c_data1 = curl_init($cmd_url_sms);
curl_setopt($c_data1, CURLOPT_RETURNTRANSFER, true);
curl_setopt($c_data1, CURLOPT_HTTPHEADER, array(
    "Host: $ip",
    "Referer: http://$ip/index.html",
   'Cookie: stok='.$cookie_pass
));
$data_response_string1 = curl_exec($c_data1);
curl_close($c_data1);

//Change path to your apache bellow

$output = $data_response_string1;
$file = fopen('\\\PATH\smslist.json', 'w+');

fwrite($file, $output);
fclose($file);

function replace_string_in_file($filename, $string_to_replace, $replace_with){
    $content=file_get_contents($filename);
    $content_chunks=explode($string_to_replace, $content);
    $content=implode($replace_with, $content_chunks);
    file_put_contents($filename, $content);
}
//fix for unknown characters for T mobile
$filename='\\\PATH\smslist.json';
$string_to_replace="HRTelekom";
$replace_with="HR Telekom";
replace_string_in_file($filename, $string_to_replace, $replace_with);

$jsonresult = json_decode(file_get_contents('\\\PATH\smslist.json'), true);

$file1 = fopen('\\\PATH\smslist_converted.json', 'w');
$cont = $jsonresult['messages'];
		foreach ($cont as $id => $arr) $cont[$id]['content']=hex2utf(($cont[$id]['content']));
        file_put_contents('\\\PATH\smslist_converted.json', json_encode($cont) . "\n", FILE_APPEND);
        header('Content-Type: application/json');
        echo json_encode($cont, JSON_PRETTY_PRINT);

 
   
exit();

?>