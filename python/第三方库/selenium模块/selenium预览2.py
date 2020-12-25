#python3.7
#Filename:selenium预览2.py
#元素交互操作，浏览器的前进后退

from selenium import webdriver
import time

browser = webdriver.Chrome()    #使用哪种浏览器进行模拟

def a():
    """元素交互"""
    url = "https://www.taobao.com/"
    browser.get(url)    #模拟浏览器请求网页（会打开所模拟的浏览器，且登陆此网址）

    input_str = browser.find_element_by_css_selector("#q")    #用css选择器,此操作代表搜索框

    input_str.send_keys("衣服")   #元素交互操作，即在输入框中输入“衣服”
    time.sleep(1)   #延迟1秒
    input_str.clear()   #清空搜索框
    input_str.send_keys("鞋子")

    button = browser.find_element_by_css_selector("#J_TSearchForm > div.search-button > button")   #代表“确认”按钮
    button.click()  #即点击“确认”按钮

def b():
    """前进后退"""
    browser.get("https://www.baidu.com/")
    browser.get("https://www.taobao.com/")
    #browser.get("https://www.python.org/")

    browser.back()  #后退
    time.sleep(1)
    browser.forward()   #前进

if __name__ == "__main__":
    try:
        b()
        browser.close()     #关闭浏览器
    except:
        print("异常")
    print("Done")
