import os,sys
import zipfile
import re
from selenium import webdriver
# Time Limit: 1000/500 MS (Java/Others)    Memory Limit: 65536/32768 K (Java/Others)
# Total Submission(s): 624905    Accepted Submission(s): 158091
option = webdriver.ChromeOptions()
option.add_argument("headless")
browser = webdriver.Chrome(options=option)
text="Time Limit: 1000/500 MS (Java/Others)    Memory Limit: 65536/32768 K (Java/Others)" \
     "Total Submission(s): 624905    Accepted Submission(s): 158091"
patternTotal = re.compile(r'Total Submission\(s\): \d*')
patternSubmission = re.compile(r'Accepted Submission\(s\): \d*')
total=patternTotal.search(text).group(0)
submission=patternSubmission.search(text).group(0)
num = re.compile(r'[\d]*')
Total=num.findall(total)[21]
Submission=num.findall(submission)[24]
print(Total)
print(Submission)

# url="http://acm.hdu.edu.cn/showproblem.php?pid="
# for i in range(1000,1002):
#     try:
#         browser.get(url+str(i))
#         all=browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/font/b/span").text
#         Total=patternTotal.match(all)
#         Submisson=patternSubmission.match(all)
#         print(Total.group())
#     except:
#         print(i+" 页面不存在")