import MySQLdb
import time
from selenium import webdriver
import csv

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver import ActionChains


def login_to_linkedin(email, password):
    user_email = email
    user_pass = password
    browser = webdriver.Chrome('D:\chromedriver.exe')

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
    profile = browser.find_element_by_xpath('//*[@id="main-site-nav"]/ul/li[2]/a')
    ActionChains(browser).move_to_element(profile).perform()
    browser.implicitly_wait(3)

    # Your Updates Tab
    browser.find_element_by_xpath('//*[@id="profile-sub-nav"]/li[3]/a').click()

    # Followers Tab
    browser.find_element_by_xpath('//*[@id="top-bar"]/div[2]/ul/li[4]/a').click()
    last_height = browser.execute_script("return document.body.scrollHeight")

    while 1:
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        try:
            browser.find_element_by_xpath('//*[@id="inline-pagination"]/a').click()
        except ElementNotVisibleException:
            print "End of Page"
        time.sleep(4)

        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break

        last_height = new_height

    items = browser.find_elements_by_css_selector('div li.follow-card')

    i = 1
    with open('linkedin_followers_list.csv', 'wb') as fp:
        writer = csv.writer(fp)
        for item in items:
            name = item.find_element_by_class_name('follow-name').text
            title = item.find_element_by_class_name('follow-headline').text
            link = item.find_element_by_class_name('follow-profile').get_attribute('href')

            print str(i) + ' - ' + name + ' - ' + link
            writer.writerow((name, title, link))
            i += 1


if __name__ == "__main__":
    email = ''
    password = ''
    login_to_linkedin(email, password)
