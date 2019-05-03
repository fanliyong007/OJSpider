import os,sys
import zipfile
import re
from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument("headless")
browser = webdriver.Chrome(options=option)
patternTotal = re.compile(r'Total Submission\(s\): \d*')
patternSubmission = re.compile(r'Accepted Submission\(s\): \d*')
url="http://acm.hdu.edu.cn/showproblem.php?pid="
for i in range(1001,2000):
    try:
        browser.get(url+str(i))
        try:
            all=browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/font/b/span").text
            Description=browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/div[2]").text
            Input=browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/div[5]").text
            Output=browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/div[8]").text
            SampleInput=browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/div[11]").text
            SampleOutput=browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/div[14]").text
            que = browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/h1").text
        except:
            print("格式不正确")
        total = patternTotal.search(all).group(0)
        submission = patternSubmission.search(all).group(0)
        num = re.compile(r'[\d]*')
        Total = int(num.findall(total)[21])
        Submission = int(num.findall(submission)[24])
        # filename = sys.path[0] + "\\tmp\\" + que.replace('==', ' equals ').replace('?', " wen ")
        # f = open(filename, 'w')
        # f.write("第" + str(i) + "题 " + "提交数：" + str(Total) + " 通过数：" + str(Submission) + "难度系数（越大越难）：" + str(
        #     int(100 - Submission / Total * 100)))
        # f.write("Problem Description\n")
        # f.write(Description+"\n")
        # f.write("Input\n")
        # f.write(Input+"\n")
        # f.write("Output\n")
        # f.write(Output+"\n")
        # f.write("Sample Input\n")
        # f.write(SampleInput+"\n")
        # f.write("Sample Output\n")
        # f.write(SampleOutput+"\n")
        print("第"+str(i)+"题 "+"提交数："+str(Total)+" 通过数："+str(Submission)+"难度系数（越大越难）："+str(int(100-Submission/Total*100)))
        # print("Problem Description")
        # print(Description)
        # print("Input")
        # print(Input)
        # print("Output")
        # print(Output)
        # print("Sample Input")
        # print(SampleInput)
        # print("Sample Output")
        # print(SampleOutput)
        # f.close()
    except:
        print(i+" 页面不存在")