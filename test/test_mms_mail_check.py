from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


# в будущем можно сделать проверку на количество писем и содержание, но пока удаляем все что есть (тест проходит даже если нет писем) chkmsg работает для одного первого сообщения


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
    wd.quit()
    time.sleep(2)


def test_yandex_mail():
    wd = webdriver.Chrome()
    wd.get("https://mail.yandex.ru")
    wd.find_element_by_link_text(link_text="Войти").click()
    # wd.find_element_by_class_name("HeadBanner-Button-Enter").click()
    time.sleep(3)
    wd.find_element_by_name("login").send_keys("qatestiss")
    wd.find_element_by_name("login").send_keys(Keys.ENTER)
    time.sleep(1)
    wd.find_element_by_name("passwd").send_keys("P0stgres")
    time.sleep(1)
    wd.find_element_by_name("passwd").send_keys(Keys.ENTER)
    time.sleep(3)

    try:
        wd.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div/div/div[3]/div[2]/div/form/div[3]/button").click()
    except NoSuchElementException:
        pass

    wd.find_element_by_css_selector("span.checkbox_view").click()
    wd.find_element_by_css_selector("span.mail-Toolbar-Item-Text.js-toolbar-item-title.js-toolbar-item-title-delete").click()
    time.sleep(1)
    wd.quit()
    time.sleep(2)

    # //div[@id='root']/div/div/div[2]/div/div/div[3]/div[2]/div/form/div[3]/button
    #//button[@type='button']
    #css=button.control.button2.control_hovered_yes.button2_hovered_yes.button2_view_classic.button2_size_l.button2_theme_normal.button2_width_max.passp-form-button
    #xpath=(.//*[normalize-space(text()) and normalize-space(.)='Не сейчас'])[1]/following::button[1]
    # wd.find_element_by_css_selector("button.control.button2.control_hovered_yes.button2_hovered_yes.button2_view_classic.button2_size_l.button2_theme_normal.button2_width_max.passp - form - button").click()
    # wd.find_element_by_css_selector("span.checkbox_view").is_displayed():
    # span.button2__text



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
    time.sleep(2)

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
    wd.quit()
    time.sleep(2)
