import time
from selenium import webdriver
import pywinauto


def handle_system_dialogue_box(filename):
    app = pywinauto.application.Application()
    main_window = app['Open']  # main windows' title
    ctrl = main_window['Edit']
    main_window.SetFocus()
    ctrl.ClickInput()
    ctrl.TypeKeys(filename)
    ctrl_bis = main_window['Open']  # open file button
    ctrl_bis.ClickInput()


# login details
def login_to_linkedin():
    user_email = ""  # email
    user_pass = ""  # password

    # download chrome webdriver and set its path here
    browser = webdriver.Chrome('C:/Users/admin/Downloads/chromedriver.exe')
    browser.maximize_window()

    browser.get('http://www.linkedin.com/')
    email_elem = browser.find_element_by_id("login-email")
    email_elem.send_keys(user_email)
    pass_elem = browser.find_element_by_id("login-password")
    pass_elem.send_keys(user_pass)
    pass_elem.submit()

    get_urls_from_file(browser)


def get_urls_from_file(browser):
    fp = open('LinkedIn_groups.txt', 'rb')
    for line in fp:
        line = line.rstrip('\n')
        time.sleep(5)
        send_message(browser, line)


def send_message(browser, line):
    user_message = unicode(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
        "the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley "
        "of type and scrambled it to make a type specimen book. It has survived not only five centuries, "
        "but also the leap into electronic typesetting, remaining essentially unchanged. ",
        errors='ignore'
    )

    user_subject = unicode(
        "Lorem Ipsum is simply dummy text.",
        errors='ignore'
    )

    operation = True
    if operation:
        browser.get(line)
        browser.implicitly_wait(15)
        time.sleep(3)

        this_subject = user_subject
        subj_msg = browser.find_element_by_css_selector('div input.input-title')
        subj_msg.send_keys(this_subject)
        browser.implicitly_wait(3)
        time.sleep(2)

        this_message = user_message
        body_msg = browser.find_element_by_css_selector('div textarea.input-body')
        body_msg.send_keys(this_message)
        browser.implicitly_wait(3)
        time.sleep(2)

        # image_Upload
        browser.find_element_by_name('file_upload').click()
        handle_system_dialogue_box('C:\\Users\\admin\\Downloads\\hindi.jpg')
        browser.implicitly_wait(15)

        time.sleep(10)
        browser.find_element_by_css_selector('div button.action-submit').click()
        browser.implicitly_wait(3)
        time.sleep(3)

    print "Operation successful."


if __name__ == "__main__":
    login_to_linkedin()
