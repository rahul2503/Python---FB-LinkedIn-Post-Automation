import MySQLdb
from selenium import webdriver
import csv


def get_values():
    db = MySQLdb.connect(host="127.0.0.1", port=2002, user="admin", passwd="admin1234", db="linkedIn")
    cursor = db.cursor()
    cursor.execute('select profile_url from t_li_connections')
    urls = cursor.fetchall()
    db.close()
    return urls


def linkedin_login(email, password):
    user_email = email
    user_pass = password
    browser = webdriver.Chrome('C:/Users/admin/Downloads/chromedriver.exe')
    browser.maximize_window()

    print "Operation in progress."

    browser.get('http://www.linkedin.com/')
    email_elem = browser.find_element_by_id("login-email")
    email_elem.send_keys(user_email)
    pass_elem = browser.find_element_by_id("login-password")
    pass_elem.send_keys(user_pass)
    pass_elem.submit()

    get_profile_urls(browser)


def get_profile_urls(self, browser):
    urls = get_values()
    for url in urls:
        send_message(browser, url)


def send_message(browser, line):
    user_message = unicode(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
        "the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley "
        "of type and scrambled it to make a type specimen book. It has survived not only five centuries, "
        "but also the leap into electronic typesetting, remaining essentially unchanged.",
        errors='ignore'
    )

    user_subject = unicode("Lorem Ipsum is simply dummy text",
                           errors='ignore')

    operation = True
    if operation:
        browser.get(line)
        browser.implicitly_wait(3)
        browser.find_element_by_xpath('//*[@id="tc-actions-send-message"]').click()
        browser.implicitly_wait(3)

        subj_msg = browser.find_element_by_css_selector('li input.compose-dialog-subject')
        this_subject = user_subject
        subj_msg.send_keys(this_subject)
        browser.implicitly_wait(3)

        body_msg = browser.find_element_by_css_selector('li textarea.compose-dialog-body')
        this_message = user_message
        body_msg.send_keys(this_message)
        browser.implicitly_wait(3)

        browser.find_element_by_css_selector('li input.btn-primary').click()
        browser.implicitly_wait(3)

    print "Operation successful."


if __name__ == "__main__":
    email = ''
    password = ''
    linkedin_login(email, password)
