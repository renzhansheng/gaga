# -*- coding: utf-8 -*
import time,os,sys
sys.path.append("..")
from page.Selenium_page import SeleniumPage
sys.path.append("../..")
import unittest
from public.Config import Config,DATA_PATH
from public.Log import logger
from public.File_Reader import ExcelReader
from public.Assertion import assert_Equal
from selenium.webdriver.common.by import By


class Login(unittest.TestCase):
    ''' 登录 '''
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    def sub_setUp(self):
        #self.driver = BrowserDrivers.Chrome()
        #self.driver.get(self.URL)
        self.page = SeleniumPage(browser_type='firefox').get('http://192.168.112.118:8088/DlWebSys/', maximize_window=True)

    def sub_tearDown(self):
        self.page.quit()

    def test_login_sussess(self):
        ''' 登录成功 '''
        self.sub_setUp()
        self.page.Login('00000001','0003','123456a!')
        self.page.implicitly_wait(3)
        rest = assert_Equal('http://192.168.112.118:8088/DlWebSys/login.html',self.page.current_url)
        logger.info('test_login_sussess:'+rest)
        self.page.save_screen_shot('test_login_sussess')
        self.sub_tearDown()
    
    def test_login_fail1(self):
        ''' 登录失败，客户代码不存在 '''
        self.sub_setUp()
        self.page.Login('12345678','2001','888888') 
        self.page.implicitly_wait(3)
        res = self.page.find_element(By.XPATH, "html/body/div[2]/table/tbody/tr[2]/td[2]/div/div[2]").text
        rest = assert_Equal('客户代码不存在',res)
        logger.info('test_login_fail1:'+rest)
        self.sub_tearDown()

    def test_login_fail2(self):
        ''' 登录失败，该客户下无此用户 '''
        self.sub_setUp()
        self.page.Login('00000001','9999','888888') 
        self.page.implicitly_wait(3)
        res = self.page.find_element(By.XPATH, "html/body/div[2]/table/tbody/tr[2]/td[2]/div/div[2]").text
        rest = assert_Equal('该客户下无此用户',res)
        logger.info('test_login_fail2:'+rest)
        self.sub_tearDown()

    def test_login_fail3(self):
        ''' 登录失败，用户名或者密码错误 '''
        self.sub_setUp()
        self.page.Login('00000001','0002','888889')
        self.page.implicitly_wait(3)
        res = self.page.find_element(By.XPATH, "html/body/div[2]/table/tbody/tr[2]/td[2]/div/div[2]").text
        rest = assert_Equal('该客户下无此用户',res)
        logger.info('test_login_fail3:'+rest)
        self.sub_tearDown()

        
