
class Ys_Zhuce(object):
    zhuce_into = lambda x: x.find_element_by_link_text('注册')
    jianchadian1 = lambda x: x.find_element_by_class_name('active')
    username = lambda x: x.find_element_by_id('loginname')
    password = lambda x: x.find_element_by_id('pass')
    re_password = lambda x: x.find_element_by_id('re_pass')
    email = lambda x: x.find_element_by_id('email')
    zhuce_click = lambda x: x.find_element_by_class_name('span-primary')
    tishi = lambda x: x.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/strong')
