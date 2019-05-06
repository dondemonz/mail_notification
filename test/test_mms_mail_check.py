from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_mail_iss():
    wd = webdriver.Chrome()
    wd.get("https://mail.iss.ru")
    time.sleep(5)
    wd.find_element_by_name("username").send_keys("qatest")
    wd.find_element_by_name("password").send_keys("P0stgres")
    wd.find_element_by_xpath("//input[@value='Вход']").click()
    time.sleep(2)
    wd.find_element_by_name("chkhd").click()
    time.sleep(2)
    wd.find_element_by_xpath("//a[@id='lnkHdrdelete']").click()
    time.sleep(2)
    # в будущем можно сделать проверку на количество писем и содержание, но пока удаляем все что есть (тест проходит даже если нет писем) chkmsg работает для одного первого сообщения
    wd.quit()


def test_yandex_mail():
    wd = webdriver.Chrome()
    wd.get("https://mail.yandex.ru")
    wd.find_element_by_class_name("HeadBanner-Button-Enter").click()
    time.sleep(3)
    wd.find_element_by_name("login").send_keys("qatestiss")
    wd.find_element_by_name("login").send_keys(Keys.ENTER)
    time.sleep(1)
    wd.find_element_by_name("passwd").send_keys("P0stgres")
    time.sleep(1)
    wd.find_element_by_name("passwd").send_keys(Keys.ENTER)
    time.sleep(3)
    # иногда тут появляется окно о привязке к телефону, тест может падать, если будет повторяться, нужно решить проблему
    #wd.execute_script("window.open('https://mail.yandex.ru/');")
    wd.find_element_by_css_selector("span.checkbox_view").click()
    time.sleep(3)
    wd.find_element_by_css_selector("span.mail-Toolbar-Item-Text.js-toolbar-item-title.js-toolbar-item-title-delete").click()
    time.sleep(1)
    wd.quit()


def test_google_mail():
    wd = webdriver.Chrome()
    wd.get("https://mail.google.com/")
    #wd.get("https://accounts.google.com/signin")
    time.sleep(2)
    wd.find_element_by_name("identifier").send_keys("qutestiss@gmail.com")
    wd.find_element_by_name("identifier").send_keys(Keys.ENTER)
    time.sleep(1)
    wd.find_element_by_name("password").send_keys("P0stgres")
    time.sleep(1)
    wd.find_element_by_name("password").send_keys(Keys.ENTER)
    time.sleep(5)
    wd.find_element_by_css_selector("span.T-Jo").click()
    time.sleep(3)
    wd.find_element_by_xpath("//div[@aria-label='Удалить']").click()
    time.sleep(2)
    wd.quit()

def test_google_mail2():
    wd = webdriver.Chrome()
    wd.get("https://mail.google.com/")
    #wd.get("https://accounts.google.com/signin")
    time.sleep(2)
    wd.find_element_by_name("identifier").send_keys("vtestp986@gmail.com")
    wd.find_element_by_name("identifier").send_keys(Keys.ENTER)
    time.sleep(1)
    wd.find_element_by_name("password").send_keys("azov1022")
    time.sleep(1)
    wd.find_element_by_name("password").send_keys(Keys.ENTER)
    time.sleep(5)
    wd.find_element_by_css_selector("span.T-Jo").click()
    time.sleep(3)
    wd.find_element_by_xpath("//div[@aria-label='Удалить']").click()
    time.sleep(2)
    wd.quit()
