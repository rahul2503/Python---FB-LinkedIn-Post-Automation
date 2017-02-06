import MySQLdb
import time
from selenium import webdriver
import csv

from selenium.common.exceptions import NoSuchElementException


def login_to_linkedin(email, password):
    user_email = email
    user_pass = password
    browser = webdriver.Chrome('D:\chromedriver.exe')
    browser.maximize_window()
    
    print "Operation in progress."
    browser.get('http://www.linkedin.com/')
    email_elem = browser.find_element_by_id("login-email")
    email_elem.send_keys(user_email)
    pass_elem = browser.find_element_by_id("login-password")
    pass_elem.send_keys(user_pass)
    pass_elem.submit()

    save_urls_to_file(browser)
    browser.close()


def save_urls_to_file(browser):
    browser.find_element_by_xpath('//*[@id="nav-link-network"]').click()
    browser.find_element_by_xpath('//*[@id="network-sub-nav"]/li[1]/a').click()

    last_height = browser.execute_script("return document.body.scrollHeight")

    while 1:
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        # items = browser.find_elements_by_css_selector('li.contact-item-view')
        time.sleep(4)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    items = browser.find_elements_by_css_selector('li.contact-item-view')
    
    i = 1
    with open('linkedin_connections_data.csv', 'wb') as fp:
        writer = csv.writer(fp)
        for item in items:
            name = item.find_element_by_xpath('//*[@id="contact-list-container"]'
                                              '/ul/li['+str(i)+']/div[2]/h3/a').text

            try:
                title = item.find_element_by_xpath('//*[@id="contact-list-container"]'
                                                   '/ul/li['+str(i)+']/div[2]/p/span[1]').text
            except NoSuchElementException:
                title = ""

            try:
                company = item.find_element_by_xpath('//*[@id="contact-list-container"]'
                                                     '/ul/li['+str(i)+']/div[2]/p/span[2]').text
            except NoSuchElementException:
                company = ""

            try:
                location = item.find_element_by_xpath('//*[@id="contact-list-container"]'
                                                      '/ul/li['+str(i)+']/div[2]/span').text
            except NoSuchElementException:
                location = ""

            link = item.find_element_by_css_selector('a.image').get_attribute('href')

            print name
            writer.writerow((name, title, company, location, link))
            i += 1

    save_connections_to_database():


def insert_values(name, job_title, company, location, link):
    db = MySQLdb.connect(host="127.0.0.1", port=2002, user="admin", passwd="admin1234", db="linkedIn")
    cursor = db.cursor()
    cursor.execute('DROP TABLE IF EXISTS T_LI_CONNECTIONS')
    cursor.execute('CREATE TABLE T_LI_CONNECTIONS(id INT AUTO_INCREMENT PRIMARY KEY, '
                   'name varchar(35), job_title varchar(200), '
                   'company varchar(200), location varchar(200), profile_url varchar(500));')
    cursor.execute('INSERT INTO T_LI_CONNECTIONS(name, job_title, company, location, profile_url) VALUES'
                   '("%s","%s","%s","%s","%s")' % (name, job_title, company, location, link))
    db.commit()
    db.close()


def save_connections_to_database():
    with open('linkedin_connections_data.csv', 'rb') as fp:
        reader = csv.reader(fp)
        for row in reader:
            arr = [None]*5
            i = 0
            for col in row:
                arr[i] = col
                i += 1

            insert_values(arr[0], arr[1], arr[2], arr[3], arr[4])


if __name__ == "__main__":
    email = ''
    password = ''
    login_to_linkedin(email, password)
