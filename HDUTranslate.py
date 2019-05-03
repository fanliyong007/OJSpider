from selenium import webdriver
import json
import urllib.request as urllib
import hashlib
import mysql.connector
import time, threading
# 打开数据库连接
conn = mysql.connector.connect(user='root', password='123456', database='hdu')
cursor = conn.cursor()
option = webdriver.ChromeOptions()
option.add_argument("headless")
browser = webdriver.Chrome(chrome_options=option)
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
        con = urllib.urlopen(req).read()
        decoded = json.loads(con)
        dst = str(decoded["trans_result"][0]["dst"])
        return dst
    except:
        print(src+" is wrong")
worddict = {}
def loop(begin,end):
    for i in range(begin,end):
        try:
            website = "http://acm.hdu.edu.cn/showproblem.php?pid=" + str(i)
            browser.get(website)
            descpription = browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/div[2]")
            tmp=str(descpription.text).split()
            for word in tmp:
                if word not in worddict and len(word)>3:
                    worddict[word]=1
                elif len(word)>3:
                    worddict[word]=worddict[word]+1
            questioninput=browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/div[5]")
            tmp = str(questioninput.text).split()
            for word in tmp:
                if word not in worddict and len(word) > 3:
                    worddict[word] = 1
                elif len(word) > 3:
                    worddict[word] = worddict[word] + 1
            questionoutput=browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/div[8]")
            tmp = str(questionoutput.text).split()
            for word in tmp:
                if word not in worddict and len(word) > 3:
                    worddict[word] = 1
                elif len(word) > 3:
                    worddict[word] = worddict[word] + 1
            print(i)
        except:
            print("not have question "+str(i))
t1 = threading.Thread(target=loop, args=(1000,2000))
t1.start()
# t2 = threading.Thread(target=loop, args=(2001,3000))
# t2.start()
# t3 = threading.Thread(target=loop, args=(3001,4000))
# t3.start()
# t4 = threading.Thread(target=loop, args=(4001,5000))
# t4.start()
# t5 = threading.Thread(target=loop, args=(5001,6000))
# t5.start()
# t6 = threading.Thread(target=loop, args=(6001,6489))
# t6.start()
t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
# t6.join()
worddict=sorted(worddict.items(),key=lambda d: d[1],reverse = True)
for i in worddict:
    if i[1] > 2:
        try:
            translate=trans_baidu(i[0])
            cursor.execute('insert into word values (%s,%s,%s)', [i[0], translate, i[1]])
            conn.commit()
        except:
            print("Internet error")
conn.commit()
conn.close()
browser.quit()