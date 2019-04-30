from selenium import webdriver
import json
import urllib.request as urllib
import hashlib
# import mysql.connector
# # 打开数据库连接
# conn = mysql.connector.connect(user='root', password='123456', database='hdu')
# cursor = conn.cursor()
option = webdriver.ChromeOptions()
option.add_argument("headless")
browser = webdriver.Chrome(options=option)
def trans_baidu(src):
    appid = "20181225000252033"  # 百度开发者apikey
    salt="520176"
    password="GTw6TvkRXmiRIsi8eOj1"
    data= appid+src+salt+password
    turl = "http://api.fanyi.baidu.com/api/trans/vip/translate?q="+src+\
           "&from=en&to=zh&appid="+ appid+\
           "&salt="+salt+\
           "&sign="+str(hashlib.md5(data.encode("utf-8")).hexdigest())
    try:
        req = urllib.Request(turl)
        print("   "+turl+"   ")
        con = urllib.urlopen(req).read()
        decoded = json.loads(con)
        dst = str(decoded["trans_result"][0]["dst"])
        return dst
    except:
        print(src+" is wrong")
trans_baidu("translate")
