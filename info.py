#!/usr/bin/python

import requests
import re
talosintelligence = requests.get("https://www.talosintelligence.com/documents/ip-blacklist", verify=False)
#vpngate = requests.get("http://www.vpngate.net/api/iphone/", verify=False)
greensnow = requests.get("https://blocklist.greensnow.co/greensnow.txt", verify=False)

IPtalosintelligence=re.findall(r'\b(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b', talosintelligence.text)
#IPvpngate = re.findall(r'\b(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b', vpngate.text)
IPgreensnow = re.findall(r'\b(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b', greensnow.text)

blockip = IPtalosintelligence + IPgreensnow
blockip = set(blockip)
blockip = list(blockip)

fp = open("blackip", "a")

for i in range(len(blockip)):
    #print(blockip[i])
    fp.write(blockip[i])
    fp.write('\n')

fp.close()
