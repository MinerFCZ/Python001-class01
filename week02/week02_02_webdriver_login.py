from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 加载石墨文档首页
    browser.get('https://shimo.im/')
    time.sleep(3)
    # 通过XPath找到登录按钮，并点击
    browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button').click()
    time.sleep(1)
    # 通过XPath找到用户名框，并输入值
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('***')
    # 通过XPath找到密码框，并输入值
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('***')
    time.sleep(3)
    # 通过XPath找到登录按钮，并点击
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
    time.sleep(10)

except Exception as e:
    print(e)
finally:
    browser.close()
