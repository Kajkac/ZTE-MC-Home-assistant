import requests
import hashlib
import js2py
from datetime import datetime
import binascii
import urllib.parse
import json
import sys
import time



gsm = ("@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ\x1bÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?"
       "¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ`¿abcdefghijklmnopqrstuvwxyzäöñüà")
ext = ("````````````````````^```````````````````{}`````\\````````````[~]`"
       "|````````````````````````````````````€``````````````````````````")

s = requests.Session()

def get_sms_time():
    return datetime.now().strftime("%y;%m;%d;%H;%M;%S;+2")

def gsm_encode(plaintext):
    res = bytearray()
    for c in plaintext:
        res.append(0)
        idx = gsm.find(c)
        if idx != -1:
            res.append(idx)
            continue
        idx = ext.find(c)
        if idx != -1:
            res.append(27)
            res.append(idx)
    return binascii.hexlify(res)


class zteRouter:


    def __init__(self, ip, password):
        self.ip = ip
        self.referer = f"http://{self.ip}/"
        self.password = password
        self.js = """/*\n * A JavaScript implementation of the RSA Data Security, Inc. MD5 Message\n * Digest Algorithm, as defined in RFC 1321.\n * Version 2.1 Copyright (C) Paul Johnston 1999 - 2002.\n * Other contributors: Greg Holt, Andrew Kepert, Ydnar, Lostinet\n * Distributed under the BSD License\n * See http://pajhome.org.uk/crypt/md5 for more info.\n */\n\n/*\n * Configurable variables. You may need to tweak these to be compatible with\n * the server-side, but the defaults work in most cases.\n */\nvar hexcase = 0;  /* hex output format. 0 - lowercase; 1 - uppercase        */\nvar b64pad  = ""; /* base-64 pad character. "=" for strict RFC compliance   */\nvar chrsz   = 8;  /* bits per input character. 8 - ASCII; 16 - Unicode      */\n\n/*\n * These are the functions you\'ll usually want to call\n * They take string arguments and return either hex or base-64 encoded strings\n */\nfunction hex_md5(s){ return binl2hex(core_md5(str2binl(s), s.length * chrsz));}\nfunction b64_md5(s){ return binl2b64(core_md5(str2binl(s), s.length * chrsz));}\nfunction str_md5(s){ return binl2str(core_md5(str2binl(s), s.length * chrsz));}\nfunction hex_hmac_md5(key, data) { return binl2hex(core_hmac_md5(key, data)); }\nfunction b64_hmac_md5(key, data) { return binl2b64(core_hmac_md5(key, data)); }\nfunction str_hmac_md5(key, data) { return binl2str(core_hmac_md5(key, data)); }\n\n/*\n * Perform a simple self-test to see if the VM is working\n */\nfunction md5_vm_test()\n{\n  return hex_md5("abc") == "900150983cd24fb0d6963f7d28e17f72";\n}\n\n/*\n * Calculate the MD5 of an array of little-endian words, and a bit length\n */\nfunction core_md5(x, len)\n{\n  /* append padding */\n  x[len >> 5] |= 0x80 << ((len) % 32);\n  x[(((len + 64) >>> 9) << 4) + 14] = len;\n\n  var a =  1732584193;\n  var b = -271733879;\n  var c = -1732584194;\n  var d =  271733878;\n\n  for(var i = 0; i < x.length; i += 16)\n  {\n    var olda = a;\n    var oldb = b;\n    var oldc = c;\n    var oldd = d;\n\n    a = md5_ff(a, b, c, d, x[i+ 0], 7 , -680876936);\n    d = md5_ff(d, a, b, c, x[i+ 1], 12, -389564586);\n    c = md5_ff(c, d, a, b, x[i+ 2], 17,  606105819);\n    b = md5_ff(b, c, d, a, x[i+ 3], 22, -1044525330);\n    a = md5_ff(a, b, c, d, x[i+ 4], 7 , -176418897);\n    d = md5_ff(d, a, b, c, x[i+ 5], 12,  1200080426);\n    c = md5_ff(c, d, a, b, x[i+ 6], 17, -1473231341);\n    b = md5_ff(b, c, d, a, x[i+ 7], 22, -45705983);\n    a = md5_ff(a, b, c, d, x[i+ 8], 7 ,  1770035416);\n    d = md5_ff(d, a, b, c, x[i+ 9], 12, -1958414417);\n    c = md5_ff(c, d, a, b, x[i+10], 17, -42063);\n    b = md5_ff(b, c, d, a, x[i+11], 22, -1990404162);\n    a = md5_ff(a, b, c, d, x[i+12], 7 ,  1804603682);\n    d = md5_ff(d, a, b, c, x[i+13], 12, -40341101);\n    c = md5_ff(c, d, a, b, x[i+14], 17, -1502002290);\n    b = md5_ff(b, c, d, a, x[i+15], 22,  1236535329);\n\n    a = md5_gg(a, b, c, d, x[i+ 1], 5 , -165796510);\n    d = md5_gg(d, a, b, c, x[i+ 6], 9 , -1069501632);\n    c = md5_gg(c, d, a, b, x[i+11], 14,  643717713);\n    b = md5_gg(b, c, d, a, x[i+ 0], 20, -373897302);\n    a = md5_gg(a, b, c, d, x[i+ 5], 5 , -701558691);\n    d = md5_gg(d, a, b, c, x[i+10], 9 ,  38016083);\n    c = md5_gg(c, d, a, b, x[i+15], 14, -660478335);\n    b = md5_gg(b, c, d, a, x[i+ 4], 20, -405537848);\n    a = md5_gg(a, b, c, d, x[i+ 9], 5 ,  568446438);\n    d = md5_gg(d, a, b, c, x[i+14], 9 , -1019803690);\n    c = md5_gg(c, d, a, b, x[i+ 3], 14, -187363961);\n    b = md5_gg(b, c, d, a, x[i+ 8], 20,  1163531501);\n    a = md5_gg(a, b, c, d, x[i+13], 5 , -1444681467);\n    d = md5_gg(d, a, b, c, x[i+ 2], 9 , -51403784);\n    c = md5_gg(c, d, a, b, x[i+ 7], 14,  1735328473);\n    b = md5_gg(b, c, d, a, x[i+12], 20, -1926607734);\n\n    a = md5_hh(a, b, c, d, x[i+ 5], 4 , -378558);\n    d = md5_hh(d, a, b, c, x[i+ 8], 11, -2022574463);\n    c = md5_hh(c, d, a, b, x[i+11], 16,  1839030562);\n    b = md5_hh(b, c, d, a, x[i+14], 23, -35309556);\n    a = md5_hh(a, b, c, d, x[i+ 1], 4 , -1530992060);\n    d = md5_hh(d, a, b, c, x[i+ 4], 11,  1272893353);\n    c = md5_hh(c, d, a, b, x[i+ 7], 16, -155497632);\n    b = md5_hh(b, c, d, a, x[i+10], 23, -1094730640);\n    a = md5_hh(a, b, c, d, x[i+13], 4 ,  681279174);\n    d = md5_hh(d, a, b, c, x[i+ 0], 11, -358537222);\n    c = md5_hh(c, d, a, b, x[i+ 3], 16, -722521979);\n    b = md5_hh(b, c, d, a, x[i+ 6], 23,  76029189);\n    a = md5_hh(a, b, c, d, x[i+ 9], 4 , -640364487);\n    d = md5_hh(d, a, b, c, x[i+12], 11, -421815835);\n    c = md5_hh(c, d, a, b, x[i+15], 16,  530742520);\n    b = md5_hh(b, c, d, a, x[i+ 2], 23, -995338651);\n\n    a = md5_ii(a, b, c, d, x[i+ 0], 6 , -198630844);\n    d = md5_ii(d, a, b, c, x[i+ 7], 10,  1126891415);\n    c = md5_ii(c, d, a, b, x[i+14], 15, -1416354905);\n    b = md5_ii(b, c, d, a, x[i+ 5], 21, -57434055);\n    a = md5_ii(a, b, c, d, x[i+12], 6 ,  1700485571);\n    d = md5_ii(d, a, b, c, x[i+ 3], 10, -1894986606);\n    c = md5_ii(c, d, a, b, x[i+10], 15, -1051523);\n    b = md5_ii(b, c, d, a, x[i+ 1], 21, -2054922799);\n    a = md5_ii(a, b, c, d, x[i+ 8], 6 ,  1873313359);\n    d = md5_ii(d, a, b, c, x[i+15], 10, -30611744);\n    c = md5_ii(c, d, a, b, x[i+ 6], 15, -1560198380);\n    b = md5_ii(b, c, d, a, x[i+13], 21,  1309151649);\n    a = md5_ii(a, b, c, d, x[i+ 4], 6 , -145523070);\n    d = md5_ii(d, a, b, c, x[i+11], 10, -1120210379);\n    c = md5_ii(c, d, a, b, x[i+ 2], 15,  718787259);\n    b = md5_ii(b, c, d, a, x[i+ 9], 21, -343485551);\n\n    a = safe_add(a, olda);\n    b = safe_add(b, oldb);\n    c = safe_add(c, oldc);\n    d = safe_add(d, oldd);\n  }\n  return Array(a, b, c, d);\n\n}\n\n/*\n * These functions implement the four basic operations the algorithm uses.\n */\nfunction md5_cmn(q, a, b, x, s, t)\n{\n  return safe_add(bit_rol(safe_add(safe_add(a, q), safe_add(x, t)), s),b);\n}\nfunction md5_ff(a, b, c, d, x, s, t)\n{\n  return md5_cmn((b & c) | ((~b) & d), a, b, x, s, t);\n}\nfunction md5_gg(a, b, c, d, x, s, t)\n{\n  return md5_cmn((b & d) | (c & (~d)), a, b, x, s, t);\n}\nfunction md5_hh(a, b, c, d, x, s, t)\n{\n  return md5_cmn(b ^ c ^ d, a, b, x, s, t);\n}\nfunction md5_ii(a, b, c, d, x, s, t)\n{\n  return md5_cmn(c ^ (b | (~d)), a, b, x, s, t);\n}\n\n/*\n * Calculate the HMAC-MD5, of a key and some data\n */\nfunction core_hmac_md5(key, data)\n{\n  var bkey = str2binl(key);\n  if(bkey.length > 16) bkey = core_md5(bkey, key.length * chrsz);\n\n  var ipad = Array(16), opad = Array(16);\n  for(var i = 0; i < 16; i++)\n  {\n    ipad[i] = bkey[i] ^ 0x36363636;\n    opad[i] = bkey[i] ^ 0x5C5C5C5C;\n  }\n\n  var hash = core_md5(ipad.concat(str2binl(data)), 512 + data.length * chrsz);\n  return core_md5(opad.concat(hash), 512 + 128);\n}\n\n/*\n * Add integers, wrapping at 2^32. This uses 16-bit operations internally\n * to work around bugs in some JS interpreters.\n */\nfunction safe_add(x, y)\n{\n  var lsw = (x & 0xFFFF) + (y & 0xFFFF);\n  var msw = (x >> 16) + (y >> 16) + (lsw >> 16);\n  return (msw << 16) | (lsw & 0xFFFF);\n}\n\n/*\n * Bitwise rotate a 32-bit number to the left.\n */\nfunction bit_rol(num, cnt)\n{\n  return (num << cnt) | (num >>> (32 - cnt));\n}\n\n/*\n * Convert a string to an array of little-endian words\n * If chrsz is ASCII, characters >255 have their hi-byte silently ignored.\n */\nfunction str2binl(str)\n{\n  var bin = Array();\n  var mask = (1 << chrsz) - 1;\n  for(var i = 0; i < str.length * chrsz; i += chrsz)\n    bin[i>>5] |= (str.charCodeAt(i / chrsz) & mask) << (i%32);\n  return bin;\n}\n\n/*\n * Convert an array of little-endian words to a string\n */\nfunction binl2str(bin)\n{\n  var str = "";\n  var mask = (1 << chrsz) - 1;\n  for(var i = 0; i < bin.length * 32; i += chrsz)\n    str += String.fromCharCode((bin[i>>5] >>> (i % 32)) & mask);\n  return str;\n}\n\n/*\n * Convert an array of little-endian words to a hex string.\n */\nfunction binl2hex(binarray)\n{\n  var hex_tab = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";\n  var str = "";\n  for(var i = 0; i < binarray.length * 4; i++)\n  {\n    str += hex_tab.charAt((binarray[i>>2] >> ((i%4)*8+4)) & 0xF) +\n           hex_tab.charAt((binarray[i>>2] >> ((i%4)*8  )) & 0xF);\n  }\n  return str;\n}\n\n/*\n * Convert an array of little-endian words to a base-64 string\n */\nfunction binl2b64(binarray)\n{\n  var tab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";\n  var str = "";\n  for(var i = 0; i < binarray.length * 4; i += 3)\n  {\n    var triplet = (((binarray[i   >> 2] >> 8 * ( i   %4)) & 0xFF) << 16)\n                | (((binarray[i+1 >> 2] >> 8 * ((i+1)%4)) & 0xFF) << 8 )\n                |  ((binarray[i+2 >> 2] >> 8 * ((i+2)%4)) & 0xFF);\n    for(var j = 0; j < 4; j++)\n    {\n      if(i * 8 + j * 6 > binarray.length * 32) str += b64pad;\n      else str += tab.charAt((triplet >> 6*(3-j)) & 0x3F);\n    }\n  }\n  return str;\n}\nhex_md5(evalString)\n"""

    def hash(self, str):
        return hashlib.sha256(str.encode()).hexdigest()

    def getVersion(self):
        header = {"Referer": self.referer}
        payload = "isTest=false&cmd=wa_inner_version"
        r = s.get(self.referer + f"goform/goform_get_cmd_process?{payload}", headers=header , data=payload)
        return r.json()["wa_inner_version"]

    def get_LD(self):
        header = {"Referer": self.referer}
        payload = "isTest=false&cmd=LD"
        r = s.get(self.referer + f"goform/goform_get_cmd_process?{payload}", headers=header, data=payload)
        return r.json()["LD"].upper()

    def getCookie(self, password, LD):
        header = {"Referer": self.referer}
        hashPassword = self.hash(password).upper()
        ztePass = self.hash(hashPassword+LD).upper()
        payload = "isTest=false&goformId=LOGIN&password=" + ztePass
        r = s.post(self.referer + "goform/goform_set_cmd_process", headers=header, data=payload)
        return "stok=" + r.cookies["stok"].strip('\"')

    def get_RD(self):
        header = {"Referer": self.referer}
        payload = "isTest=false&cmd=RD"
        r = s.post(self.referer + "goform/goform_get_cmd_process", headers=header, data=payload)
        return r.json()["RD"]

    def sendsms(self):
        cookie = self.getCookie(password = self.password, LD = self.get_LD())
        newjs = self.js.replace("evalString", f"'{self.getVersion()}'")
        a = js2py.eval_js(newjs)
        u = self.get_RD()
        newjs = self.js.replace("evalString", '"' + a + u + '"')
        AD = js2py.eval_js(newjs)
        header = {"Referer": self.referer, "Cookie": cookie}
        payload = f'isTest=false&goformId=SEND_SMS&notCallback=true&Number={phoneNumberEncoded}&sms_time={getsmstimeEncoded}&MessageBody={outputmessage}&ID=-1&encode_type=GSM7_default&AD=' + AD
        print(payload)
        r = s.post(self.referer + "goform/goform_set_cmd_process", headers=header, data=payload)
        return r.status_code

    def zteinfo(self):
        ip = self.ip
        cookie = self.getCookie(password = self.password, LD = self.get_LD())
        cmd_url = f"http://{ip}/goform/goform_get_cmd_process?isTest=false&cmd=wa_inner_version%2Cnetwork_type%2Crssi%2Crscp%2Crmcc%2Crmnc%2Cenodeb_id%2Clte_rsrq%2Clte_rsrp%2CZ5g_snr%2CZ5g_rsrp%2CZCELLINFO_band%2CZ5g_dlEarfcn%2Clte_ca_pcell_arfcn%2Clte_ca_pcell_band%2Clte_ca_scell_band%2Clte_ca_pcell_bandwidth%2Clte_ca_scell_info%2Clte_ca_scell_bandwidth%2Cwan_lte_ca%2Clte_pci%2CZ5g_CELL_ID%2CZ5g_SINR%2Ccell_id%2Cwan_lte_ca%2Clte_ca_pcell_band%2Clte_ca_pcell_bandwidth%2Clte_ca_scell_band%2Clte_ca_scell_bandwidth%2Clte_ca_pcell_arfcn%2Clte_ca_scell_arfcn%2Clte_multi_ca_scell_info%2Cwan_active_band%2Cnr5g_pci%2Cnr5g_action_band%2Cnr5g_cell_id%2Clte_snr%2Cecio%2Cwan_active_channel%2Cnr5g_action_channel%2Cngbr_cell_info%2Cmonthly_tx_bytes%2Cmonthly_rx_bytes%2Clte_pci%2Clte_pci_lock%2Clte_earfcn_lock%2Cwan_ipaddr%2Cwan_apn%2Cpm_sensor_mdm%2Cpm_modem_5g%2Cnr5g_pci%2Cnr5g_action_channel%2Cnr5g_action_band%2CZ5g_SINR%2CZ5g_rsrp%2Cwan_active_band%2Cwan_active_channel%2Cwan_lte_ca%2Clte_multi_ca_scell_info%2Ccell_id%2Cdns_mode%2Cprefer_dns_manual%2Cstandby_dns_manual%2Cnetwork_type%2Crmcc%2Crmnc%2Clte_rsrq%2Clte_rssi%2Clte_rsrp%2Clte_snr%2Cwan_lte_ca%2Clte_ca_pcell_band%2Clte_ca_pcell_bandwidth%2Clte_ca_scell_band%2Clte_ca_scell_bandwidth%2Clte_ca_pcell_arfcn%2Clte_ca_scell_arfcn%2Cwan_ipaddr%2Cstatic_wan_ipaddr%2Copms_wan_mode%2Copms_wan_auto_mode%2Cppp_status%2Cloginfo%2Crealtime_time&multi_data=1"
        cookie_pass = cookie

        headers = {
            "Host": ip,
            "Referer": f"http://{ip}/index.html",
            "Cookie": f"{cookie_pass}"
                 }

        response = s.get(cmd_url, headers=headers)
        print(response.text)

    def ztesmsinfo(self):
        ip = self.ip
        cookie = self.getCookie(password = self.password, LD = self.get_LD())
        cmd_url = f"http://{ip}/goform/goform_get_cmd_process?isTest=false&cmd=sms_capacity_info"
        cookie_pass = cookie

        headers = {
            "Host": ip,
            "Referer": f"http://{ip}/index.html",
            "Cookie": f"{cookie_pass}"
                 }

        response = s.get(cmd_url, headers=headers)
        return response.text


    def ztereboot(self):
        cookie = self.getCookie(password = self.password, LD = self.get_LD())
        newjs = self.js.replace("evalString", f"'{self.getVersion()}'")
        a = js2py.eval_js(newjs)
        u = self.get_RD()
        newjs = self.js.replace("evalString", '"' + a + u + '"')
        AD = js2py.eval_js(newjs)
        header = {"Referer": self.referer, "Cookie": cookie}
        payload = f'isTest=false&goformId=REBOOT_DEVICE&AD=' + AD
        print(payload)
        r = s.post(self.referer + "goform/goform_set_cmd_process", headers=header, data=payload)
        return r.status_code

    def deletesms(self, msg_id):
        cookie = self.getCookie(password = self.password, LD = self.get_LD())
        newjs = self.js.replace("evalString", f"'{self.getVersion()}'")
        a = js2py.eval_js(newjs)
        u = self.get_RD()
        newjs = self.js.replace("evalString", '"' + a + u + '"')
        AD = js2py.eval_js(newjs)
        header = {"Referer": self.referer, "Cookie": cookie}
        payload = f'isTest=false&goformId=DELETE_SMS&msg_id={msg_id}&AD=' + AD
        print(payload)
        r = s.post(self.referer + "goform/goform_set_cmd_process", headers=header, data=payload)
        return r.status_code

    def parsesms(self):
        cookie = self.getCookie(password = self.password, LD = self.get_LD())
        header = {"Referer": self.referer, "Cookie": cookie}
        payload = f'cmd=sms_data_total&page=0&data_per_page=5000&mem_store=1&tags=10&order_by=order+by+id+desc'# + AD
        r = s.post(self.referer + "goform/goform_get_cmd_process", headers=header, data=payload)
        response_text = r.text

        # Find and replace the string
        modified_response_text = response_text.replace('HRTelekom', 'HR Telekom')
        response_json = json.loads(modified_response_text)
        value = response_json['messages']
        def hex2utf(string):
            length = len(string) // 4
            result = ''
            for i in range(length):
                result += chr(int(string[i*4:i*4+4], 16))
            return result

        # Load the JSON data from a file
        smslist = response_json

        # Convert the hexadecimal code points in the 'content' field to Unicode characters
        for item in smslist['messages']:
            item['content'] = hex2utf(item['content'])

        # Write the modified JSON data to a new file
        #with open('smslist_converted.json', 'w') as f:
            #json.dump(smslist, f, indent=2)
        return json.dumps(smslist, indent=2)



getsmstime = get_sms_time()
getsmstimeEncoded = urllib.parse.quote(getsmstime, safe="")
phoneNumber = '13909' # enter phone number here
phoneNumberEncoded = urllib.parse.quote(phoneNumber, safe="")
message = 'BRZINA' # enter your message here
messageEncoded = gsm_encode(message)
outputmessage = messageEncoded.decode()

zteInstance = zteRouter("IP", "PASSWORD")
ha_select = int(sys.argv[1])


if ha_select == 1:
    time.sleep(2)
    zteInstance.parsesms()
    result = zteInstance.parsesms()
    json_str = json.dumps(result)
    test = json.loads(result)
    first_message = test["messages"][0]
    first_message_json = json.dumps(first_message)
    print(first_message_json)
elif ha_select == 2:
    zteInstance.sendsms()
elif ha_select == 3:
    time.sleep(3)
    result = zteInstance.zteinfo()
elif ha_select == 4:
    zteInstance.ztereboot()
elif ha_select == 5:
    zteInstance.parsesms()
    result = zteInstance.parsesms()
    data = json.loads(result)
    keys = data.keys()  # ['key']
    ids = [message['id'] for message in data['messages']]
    formatted_ids = ";".join(ids)
    print(formatted_ids)
    zteInstance.deletesms(formatted_ids)
elif ha_select == 6:
    time.sleep(6)
    zteInstance.ztesmsinfo()
    json_string = zteInstance.ztesmsinfo()
    totalztememory = 100
    dictionary = json.loads(json_string)
    nv_rev_total = int(dictionary['sms_nv_rev_total'])
    nv_send_total = int(dictionary['sms_nv_send_total'])
    total = nv_rev_total + nv_send_total
    totalremaining = totalztememory - total
    #print(totalremaining)
    print(f"You have {totalremaining} messages left of 100")

else:
    print("ELSE")