from library.getData import get_csv_data
from library.getElement import Ys_Zhuce
from selenium import webdriver

class Register(object):

    def test_register(self,username,passwd,repasswd,email,assert_result):
            driver = webdriver.Firefox()
            driver.get("http://118.31.19.120:3000/")
            Ys_Zhuce.zhuce_into(driver).click()
            Ys_Zhuce.username(driver).send_keys(username)
            Ys_Zhuce.password(driver).send_keys(passwd)
            Ys_Zhuce.re_password(driver).send_keys(repasswd)
            Ys_Zhuce.email(driver).send_keys(email)
Register()
# data1 = get_csv_data('canshu.csv')
# for i in range(len(data1[0])):
#         i += 1
#         n, username, passwd, repasswd, email, assert_result = data1[i]
#         print(n,username, passwd, repasswd, email, assert_result)

# Register().test_register(username, passwd, repasswd, email, assert_result)









