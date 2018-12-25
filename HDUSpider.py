# coding = utf-8
import os
import re
from selenium import webdriver
browser = webdriver.Chrome()
# username=input("请输入账户名")#读入账户
# userpass=input("请输入密码")#读入密码
username="fanliyong007"
userpass="fanliyong8880+"
browser.get("http://acm.hdu.edu.cn/userstatus.php?user="+username)#取得当前用户题目集
queXpath="/html/body/table/tbody/tr[4]/td/table/tbody/tr/td/p[3]"#题目集xpath路径
browser.find_element_by_name("username").send_keys(username)
browser.find_element_by_name("userpass").send_keys(userpass)
browser.find_element_by_name("login").click()#模拟登录
que=browser.find_element_by_xpath(queXpath)#获取题目集文本
Myque=[]
for str in que.text.split(' '):
    if re.match(r'\d{4}',str):
        Myque.append(str)
for queNum in Myque:
    browser.get("http://acm.hdu.edu.cn/status.php?user="+username+"&pid="+queNum+"&status=5")
    browser.find_element_by_xpath("//*[@id=\"fixed_table\"]/table/tbody/tr[2]/td[7]/a").click()
    hander=browser.current_window_handle
    handers=browser.window_handles
    for h in handers:
        if h!=hander:
            browser.switch_to_window(h)
            code = browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/div/div[2]/pre")
            print(code.text)
            f=open('D:\Spider\HDUACM\\'+queNum,'w')
            f.write(code.text)
            f.close()
            browser.close()
            browser.switch_to_window(hander)
browser.quit()