#python3.7
#Filename:selenium预览1.py
#选择器的使用
#使用selenium模拟浏览器

from selenium import webdriver

browser = webdriver.Chrome()    #使用哪种浏览器进行模拟

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}
url = "https://www.taobao.com/"

browser.get(url)    #模拟浏览器请求网页（会打开所模拟的浏览器，且登陆此网址）

#单个元素查找
def search():   #通过不同的方式去获取响应的元素
    input_1 = browser.find_element_by_css_selector("#q")    #css选择器
    input_2 = browser.find_element_by_id("q")   #id
    input_3 = browser.find_element_by_xpath('//*[@id="q"]')     #xpath选择器
    print(input_1,input_2,input_3)  #3个结果相同
    browser.close()     #关闭浏览器
    """
    或
    from selenium.webdriver.commom.by import By

    input = browser.find_element(By.ID,"q")   #此处的ID可替换为其它，相对应的q也替换
    形式代替
    """
#多项元素查找
def search1():  #与但不同的在于elements
    #from selenium.webdriver.commom.by import By
    #input_1 = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
    input_1 = browser.find_elements_by_css_selector('.service-bd li')
    print(input_1)
    browser.close()



if __name__ == "__main__":
    search()
