# coding = utf-8
import os,sys
import zipfile
from selenium import webdriver
Myque=[]
option = webdriver.ChromeOptions()
option.add_argument("headless")
browser = webdriver.Chrome(options=option)
def zip_file(src_dir):
    zip_name = src_dir +'.zip'
    z = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(src_dir):
        fpath = dirpath.replace(src_dir,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
            print ('==压缩成功==')
    z.close()
def removeFileInFirstDir(targetDir):
    for file in os.listdir(targetDir):
        targetFile = os.path.join(targetDir,  file)
        if os.path.isfile(targetFile):
            os.remove(targetFile)
username=input()#读入账户
userpass=input()#读入密码
browser.get("http://acm.hdu.edu.cn/status.php?user="+username)#取得当前用户题目集
browser.find_element_by_name("username").send_keys(username)
browser.find_element_by_name("userpass").send_keys(userpass)
browser.find_element_by_name("login").click()#模拟登录
flag=True
while flag:
    table=browser.find_element_by_id("fixed_table")

    for i in range(2,17):
        try:
            xpath="//table/tbody/tr[" + str(i) + "]/td[3]/font"
            status = table.find_element_by_xpath(xpath)
        except:
            try:
                xpath = "//table/tbody/tr[" + str(i) + "]/td[3]/a/font"
                status = table.find_element_by_xpath(xpath)
            except:
                flag=False
        if flag:
            if status.text=="Accepted":
                ans=table.find_element_by_xpath("//table/tbody/tr["+str(i)+"]/td[7]/a").get_attribute("href")
                Myque.append(ans)
    browser.find_element_by_xpath("//*[@id=\"fixed_table\"]/p/a[3]").click()
Myque=set(Myque)
for quePath in Myque:
    browser.get(quePath)
    code = browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/div/div[2]/pre")
    queNum=browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/div/div[1]/b/font/a[1]").text
    print(code.text)
    filename=sys.path[0]+"\\tmp\\"+queNum.replace('==',' equals ').replace('?'," wen ")
    f=open(filename,'w')
    f.write(code.text)
    f.close()
browser.close()
zip_file(sys.path[0]+"\\tmp")
removeFileInFirstDir(sys.path[0]+"\\tmp")
browser.quit()