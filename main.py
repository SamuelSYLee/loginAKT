'----------------------------------------------------'
'Automation for AP AnimalKenTei Website              '
'Copyright @ Samuel Lee                              '
'----------------------------------------------------'

import time, os, csv
from selenium import webdriver
from public import Login

class LoginTest():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1000, 1000)
        self.driver.get("https://www.discoverychannel.com.tw/animalkentei/index.php")

    def member_login(self, username, password):
        Login().user_login(self.driver, username, password)
        time.sleep(0.5)
        userinfo = self.driver.find_element_by_xpath("//div[@class = 'userName']").text
        #Login().user_logout(self.driver)

        return userinfo

def txtlines(filename):
    user_info = open(filename, 'r')
    lines = user_info.readlines()
    user_info.close()
    return lines

def csvlines(filename):
    lines = csv.reader(open(filename, 'r'))
    return lines

filetype = 'csv'
filename = os.path.dirname(__file__) + '/info.' + filetype

if filetype == 'txt':
    getlines = txtlines(filename)
elif filetype == 'csv':
    getlines = csvlines(filename)

cnt = 0

for line in getlines:
    cnt = cnt + 1
    if filetype == 'txt':
        username = line.split(',')[0]
        password = line.split(',')[1]
    elif filetype == 'csv':
        username = line[0]
        password = line[1]
    
    if cnt == 1:
        continue
    else:
        userinfo = LoginTest().member_login(username, password)
        print('Test Username: %-15s; Result: PASS' %userinfo)
