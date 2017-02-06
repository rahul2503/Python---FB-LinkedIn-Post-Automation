from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys


def login_to_facebook():
    browser = webdriver.Chrome('C:/Users/admin/Downloads/chromedriver.exe')
    browser.maximize_window()

    user_email = ""
    user_pass = ""

    browser.get('http://www.facebook.com')
    email_elem = browser.find_element_by_id("email")
    email_elem.send_keys(user_email)
    pass_elem = browser.find_element_by_id("pass")
    pass_elem.send_keys(user_pass)
    pass_elem.submit()

    get_urls_from_file(browser)


def get_urls_from_file(browser):
    fp = open('fb_groups.txt', 'rb')
    for url in fp:
        url = url.rstrip('\n')
        time.sleep(5)
        send_message(browser, url)


def send_message(browser, url):
    user_message = unicode(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
        "the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley "
        "of type and scrambled it to make a type specimen book. It has survived not only five centuries, "
        "but also the leap into electronic typesetting, remaining essentially unchanged. ",
        errors='ignore'
    )

    operation = True
    if operation:
        print "Operation in progress."

        browser.get(url)
        browser.implicitly_wait(3)
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="facebook"]/body').send_keys(Keys.ESCAPE)
        browser.implicitly_wait(3)

        browser.find_element_by_css_selector('li a.fbReactComposerAttachmentSelector_MEDIA').click()
        browser.implicitly_wait(5)
        time.sleep(5)

        image_select = browser.find_element_by_css_selector('div input._5f0v')
        image_select.send_keys('C:\\Users\\admin\\Downloads\\hindi.jpg')
        browser.implicitly_wait(10)
        time.sleep(15)

        text_area_elem = browser.find_element_by_css_selector('div div._5rpu')
        this_message = user_message
        text_area_elem.send_keys(this_message)
        browser.implicitly_wait(3)
        time.sleep(5)

        # upload image
        browser.find_element_by_css_selector('div button._1mf7').click()
        browser.implicitly_wait(10)
        time.sleep(5)

    print "Operation successful."
    browser.close()


if __name__ == "__main__":
    login_to_facebook()
