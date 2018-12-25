from selenium import webdriver
import json
import urllib.request as urllib
import hashlib
browser = webdriver.Chrome()
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
        print()
def trans_google(src):
    url="https://translate.google.cn/#view=home&op=translate&sl=auto&tl=zh-CN&text="+str(src)
    browser.get(url)
    dst=browser.find_element_by_class_name("tlid-translation translation")
    return dst.text
worddict={}
for i in range(1000,1010):
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
    except:
        print("not have question "+str(i))
worddict=sorted(worddict.items(),key=lambda d: d[1],reverse = True)
for i in worddict:
    if i[1] > 2:
        print(i)
        print("英文"+i[0]+" 中文翻译："+trans_google(i[0])+" 出现次数"+str(i[1]))
browser.quit()