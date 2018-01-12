#coding=utf-8

from selenium import webdriver
import unittest,time,xlrd
from PIL import Image


class Baoan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.fname = "G:\python课程\架构\\baoan.xls"
        self.op = xlrd.open_workbook(self.fname)
        self.sh = self.op.sheet_by_name("Sheet1")
        self.url = self.sh.cell_value(1,0)
        self.user = int(self.sh.cell_value(1,1))
        self.passwd = str(self.sh.cell_value(1,2))
        self.policyno = str(self.sh.cell_value(1,3))

    def test_baoan(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id('userCode').send_keys(self.user)
        driver.find_element_by_id('password').send_keys(self.passwd)
        driver.find_element_by_id('but_login').click()
        self.assertEqual(driver.title,u'理赔工作流系统')
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/input[2]').click()
        driver.switch_to.frame('Top_Message')
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[6]/div[2]/ul/li[1]/p').click()
        driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
        driver.find_element_by_id('policyNo').send_keys(self.policyno)
        driver.find_element_by_css_selector('span.glyphicon.glyphicon-search').click()
        time.sleep(2)
        driver.find_element_by_link_text('报案登记').click()
        driver.switch_to.default_content()
        driver.switch_to.frame('RegistId')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/form/fieldset[1]/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]/div/table/tbody/tr/td[1]/div/input').click()
        driver.find_element_by_id('prpLregistPage_sceneRegistFalg1').click()
        driver.find_element_by_id('prpLaccidentInfoPage_damageRemark').send_keys('啦啦啦')
        driver.find_element_by_xpath('/html/body/div[1]/div/div/form/fieldset[1]/div[4]/div/table/tbody/tr[5]/td[2]/table/tbody/tr/td[1]/span[1]/span').click()
        driver.find_element_by_id('_easyui_combobox_i5_2').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/form/fieldset[1]/div[4]/div/table/tbody/tr[5]/td[2]/table/tbody/tr/td[1]/span[2]/input[1]').click()
        driver.find_element_by_id('_easyui_combobox_i6_1').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/form/fieldset[1]/div[4]/div/table/tbody/tr[5]/td[2]/table/tbody/tr/td[1]/span[3]/input[1]').click()
        driver.find_element_by_id('_easyui_combobox_i7_1').click()
        driver.find_element_by_id('prpLaccidentInfoPage_address').send_keys('凤囚凰')
        driver.find_element_by_id('prpLcar_driverName').send_keys('凤求凰')
        driver.find_element_by_id('prpLregistPage.reportorName').send_keys('凤求凰')
        driver.find_element_by_id('prpLregistPage_linkerName').send_keys('凤求凰')
        driver.find_element_by_id('prpLregistPage_reportorPhoneNo').send_keys('13111111111')
        driver.find_element_by_xpath('/html/body/div[1]/div/div/form/fieldset[6]/div/table/tbody/tr[2]/td/button').click()
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//input[@value='提交']").click()

        time.sleep(3)
        driver.get_screenshot_as_file('G:\python课程\架构\\a.png')
        location = driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div').location
        size = driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div').size
        left = location['x']
        top = location['y']
        right = location['x']+size['width']
        bottom = location['y']+size['height']
        a = Image.open('G:\python课程\架构\\a.png')
        im = a.crop((left,top,right,bottom))
        im.save('G:\python课程\架构\\ok.png')




    def tearDown(self):
        pass
        # self.driver.quit()

if __name__ == '__main__':
    unittest.main()