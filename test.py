import re
from selenium import webdriver
import string
import re,os
import json
import urllib.request as urllib
import sys
import hashlib
def trans_baidu(src):
    appid = "20181225000252033"  # 百度开发者apikey
    salt="520176"
    password="GTw6TvkRXmiRIsi8eOj1"
    data= appid+src+salt+password
    turl = "http://api.fanyi.baidu.com/api/trans/vip/translate?q="+src+\
           "&from=en&to=zh&appid="+ appid+\
           "&salt="+salt+\
           "&sign="+str(hashlib.md5(data.encode("utf-8")).hexdigest())
    req = urllib.Request(turl)
    con = urllib.urlopen(req).read()
    decoded = json.loads(con)
    dst = str(decoded["trans_result"][0]["dst"])
    return dst

print(trans_baidu("this"))