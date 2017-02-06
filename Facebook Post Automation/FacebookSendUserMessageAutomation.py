from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import MySQLdb


def sql():
    db = MySQLdb.connect(host="127.0.0.1", port=2002, user="admin", passwd="admin1234", db="facebook")
    cursor = db.cursor()
    cursor.execute("SELECT username FROM users")
    users = cursor.fetchall()
    db.close()
    return users

Users = sql()

userEmail = ""
userPass = ""
NumberOfUsers = len(Users)
print(NumberOfUsers)

# User Message
userMessage = unicode(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
        "the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley "
        "of type and scrambled it to make a type specimen book. It has survived not only five centuries, "
        "but also the leap into electronic typesetting, remaining essentially unchanged. ",
        errors='ignore'
    )

operation = True
if operation:
    browser = webdriver.Chrome('C:/Users/admin/Downloads/chromedriver.exe')
    browser.maximize_window()

    browser.get('http://www.facebook.com')
    emailElem = browser.find_element_by_id("email")
    emailElem.send_keys(userEmail)
    passElem = browser.find_element_by_id("pass")
    passElem.send_keys(userPass)
    passElem.submit()

    for i in range(0, NumberOfUsers):
        browser.implicitly_wait(3)

        userTargetUrl = "http://www.facebook.com/messages/" + Users[i][0]
        browser.get(userTargetUrl)
        browser.implicitly_wait(3)
        time.sleep(5)

        textAreaElem = browser.find_element_by_css_selector("textarea.uiTextareaNoResize")
        thisMessage = userMessage
        textAreaElem.send_keys(thisMessage)
        browser.implicitly_wait(3)
        time.sleep(5)

        # upload image
        browser.find_element_by_xpath('//*[@id="js_1"]').send_keys("C:\\Users\\admin\\Downloads\\hindi.jpg")
        browser.implicitly_wait(5)
        time.sleep(5)

        textAreaElem.send_keys(Keys.ENTER)
        time.sleep(3)

    print "Operation successful."
    browser.close()

