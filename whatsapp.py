from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time 

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")

while True:

    name = input("Enter the name of the user or group : ")
    msg = input("Enter your message : ")
    count = int(input("Enter the count : "))

    input("Press enter after scanning QR Code")

    search_box = driver.find_element_by_class_name("jN-F5")
    search_box.send_keys(name)

    time.sleep(2)

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name("_1Plpp")

    for i in range(count):
        msg_box.send_keys(msg)
        time.sleep(0.2)
        button = driver.find_element_by_class_name("_35EW6")
        button.click()

    flag = input("Do you want to continue sending messages? (y/n) : ")
    if(flag=="n"):
        break
    else:
        continue