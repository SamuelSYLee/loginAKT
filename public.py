'----------------------------------------------------'
'Automation for AP AnimalKenTei Website              '
'Copyright @ Samuel Lee                              '
'----------------------------------------------------'

class Login():
    def user_login(self, driver, username, password):
        driver.find_element_by_xpath("//button[@class='hamburger showMT']").click()
        driver.find_element_by_xpath("//nav[@class='header-nav']/ul/li[5]").click()

        AccountName = driver.find_element_by_xpath("//div[1]/input[@class='input-field w50']")
        AccountName.clear()
        AccountName.send_keys(username)

        AccountPW = driver.find_element_by_xpath("//div[2]/input[@class='input-field w50']")
        AccountPW.clear()
        AccountPW.send_keys(password)

        driver.find_element_by_xpath("//button[@class='btn_signin btn_blue btn_radius']").click()

    def user_logout(self, driver):
        driver.find_element_by_xpath("//button[@class='hamburger showMT']").click()
        driver.find_element_by_xpath("//nav[@class='header-nav']/ul/li[5]").click()
