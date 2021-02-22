import selenium
from datetime import date
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import PySimpleGUI as sg

# Preliminary stuff
# Check if user exists, save username to txt file

usernameStr = None
dateStr = None
timeInput = None
isValidDate = False

if not os.path.isfile("user.txt"):
    layout = [[sg.Text('No ID detected. Set-up required:')],
              [sg.Text('Enter your ID'), sg.InputText()],
              [sg.Button('Submit')]]
    window = sg.Window('Enter ID', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            exit()
        elif event == 'Submit':
            usernameStr = values[0]
            break
    window.close()

    text_file = open("user.txt", "w")
    text_file.write(usernameStr)
    text_file.close()

else:
    file = open('user.txt', 'r')
    line = file.readlines()
    usernameStr = line[0]

if not os.path.isfile("date.txt"):
    layout = [[sg.Text('No date detected. Enter a date in the form of mm/dd/yyyy.')],
              [sg.Text('Enter your desired date: '), sg.InputText()],
              [sg.Button('Submit')]]
    window = sg.Window('Date Selection', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            exit()
        elif event == 'Submit':
            dateStr = values[0]
            text_file = open("date.txt", "w")
            text_file.write(dateStr)
            text_file.close()
            break
    window.close()

else:
    layout = [[sg.Text('Would you like to update your date? If yes, enter a date in the form of mm/dd/yyyy and Submit. If no, click Continue.')],
              [sg.Text('Enter your desired date: '), sg.InputText()],
              [sg.Button('Submit')],
              [sg.Button('Continue')]]
    window = sg.Window('Date Update', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            exit()
        elif event == 'Submit' and values[0] != "":
            dateStr = values[0]
            text_file = open("date.txt", "w")
            text_file.write(dateStr)
            text_file.close()
            break
        else:
            file = open('date.txt', 'r')
            line = file.readlines()
            dateStr = line[0]
            break
    window.close()


if not os.path.isfile("time.txt"):
    layout = [[sg.Text('No time detected. Enter a time in the form of hh:mm am/pm.')],
              [sg.Text('Enter your desired time: '), sg.InputText()],
              [sg.Button('Submit')]]
    window = sg.Window('Time Selection', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            exit()
        elif event == 'Submit':
            timeInput = values[0]
            text_file = open("time.txt", "w")
            text_file.write(timeInput)
            text_file.close()
            break
        else:
            file = open('time.txt', 'r')
            line = file.readlines()
            timeInput = line[0]
    window.close()

else:
    layout = [[sg.Text('Would you like to update your time? If yes, enter a time in the form of (h)h:mm am/pm and Submit. If no, click Continue.')],
              [sg.Text('Enter your desired time: '), sg.InputText()],
              [sg.Button('Submit')],
              [sg.Button('Continue')]]
    window = sg.Window('Time Update', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            exit()
        elif event == 'Submit' and values[0] != "":
            timeInput = values[0]
            text_file = open("time.txt", "w")
            text_file.write(timeInput)
            text_file.close()
            break
        else:
            file = open('time.txt', 'r')
            line = file.readlines()
            timeInput = line[0]
            break
    window.close()

layout = [  [sg.Text('By clicking OK, the program will start to run, and you may be subject to cancel fees if you change your mind. Click ABORT to cancel.')],
            [sg.Button('Ok'), sg.Button('Abort')] ]

window = sg.Window('WARNING', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Abort': # if user closes window or clicks cancel
        exit()
    else:
        break
window.close()

# TO-DO: Implement course selection
# The absence of any files will introduce set-up options. All set-up fields must be complete for program to run.

# default password for player cards. Don't worry, no one is getting hacked!

passwordStr = 'lacitygolf'
browser = webdriver.Chrome(ChromeDriverManager().install())
url = "https://cityoflapcp.ezlinksgolf.com/index.html#/login"


browser.get(url)
browser.implicitly_wait(20)
username = browser.find_element_by_name('login')
print(username)
username.send_keys(usernameStr)
password = browser.find_element_by_name('password')
password.send_keys(passwordStr)

nextButton = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ui-view/div[2]/div[1]/div/div/div/div[2]/form/div[4]/div[2]/button")
nextButton.click()

# Proceed past initial page and go straight to the selection page
try:
    element = WebDriverWait(browser, 300).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/ui-view/div/div/div/div[2]/div[2]/form/div/div/div/button"))
        )
finally:
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ui-view/div/div/div/div[2]/div[2]/form/div/div/div/button").click()
print("First page bypassed")


dateInput = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[1]/div/input")
dateGuesser = str(date.today())

# if date checked correctly, then parse current calendar month
if dateGuesser[5:7] == dateStr[0:2]:
    try:
        element = WebDriverWait(browser, 1000).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[1]/div/input"))
        )
    finally:
        dateInput.clear()
        dateInput.clear()
        # Obtain list of dates
        x = browser.find_elements_by_tag_name('td')
        for date in x:
            dateCheck = date.text
            print(dateCheck)
            if len(dateCheck) == 2:
                if dateCheck[0] == dateStr[3] and dateCheck[1] == dateStr[4]:
                    try:
                        element = WebDriverWait(browser, 1000).until(
                            EC.element_to_be_clickable(date)
                        )
                    finally:
                        date.click()
                        print("Date added")
                        isValidDate = True
                        break
        if not isValidDate:
            print("Invalid date. Please restart the program and enter another date.")
            exit()

# if date check incorrect, then switch to next month and parse
else:
    if int(dateGuesser[5:7])+1 == int(dateStr[0:2]):
        try:
            element = WebDriverWait(browser, 1000).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[1]/div/input"))
            )
        except:
            print("Invalid date. Please restart the program and enter another date.")
            exit()
        else:
            dateInput.clear()
            dateInput.clear()
            # click the arrow button to navigate to next month
            browser.find_element_by_xpath("/html/body/div[4]/div/a[2]").click()
            # Obtain list of dates
            x = browser.find_elements_by_tag_name('td')
            for date in x:
                dateCheck = date.text
                print(dateCheck)
                # ex: day is 1, user input is 03/01/2021
                if len(dateCheck) == 1 and dateStr[3] == '0':
                    if dateCheck[0] == dateStr[4]:
                        try:
                            element = WebDriverWait(browser, 1000).until(
                                EC.element_to_be_clickable(date)
                            )
                        finally:
                            date.click()
                            print("Date added")
                            isValidDate = True
                            break
                # ex: day is 1, user input is 03/1/2021
                elif len(dateCheck) == 1 and dateStr[3] != 0:
                    if dateCheck[0] == dateStr[3]:
                        try:
                            element = WebDriverWait(browser, 1000).until(
                                EC.element_to_be_clickable(date)
                            )
                        finally:
                            print("clicking on " + date.text)
                            date.click()
                            print("Date added")
                            isValidDate = True
                            break
                else:
                    if dateCheck[0] == dateStr[3] and dateCheck[1] == dateStr[4]:
                        try:
                            element = WebDriverWait(browser, 1000).until(
                                EC.element_to_be_clickable(date)
                            )
                        finally:
                            date.click()
                            print("Date added")
                            isValidDate = True
                            break
            if not isValidDate:
                print("Invalid date. Please restart the program and enter another date.")
                exit()
    else:
        print("Date is invalid. Please restart the program and enter a valid date.")
        exit()

# Remove Hansen Dam Back 9
try:
    element = WebDriverWait(browser, 500).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[5]/div/ul/li[4]/div/div[1]/input"))
    )
finally:
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[5]/div/ul/li[4]/div/div[1]/input").click()
    print("First course removed")

# Remove Los Feliz 3-par
try:
    element = WebDriverWait(browser, 500).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[5]/div/ul/li[6]/div/div[1]/input"))
    )
finally:
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[5]/div/ul/li[6]/div/div[1]/input").click()
    print("Second course removed")

# Remove Rancho Park Back 9
try:
    element = WebDriverWait(browser, 1000).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[5]/div/ul/li[9]/div/div[1]/input"))
    )
finally:
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[5]/div/ul/li[9]/div/div[1]/input").click()
    print("Third course removed")

# Remove Rancho Park Par 3
try:
    element = WebDriverWait(browser, 1001).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[5]/div/ul/li[10]/div/div[1]/input"))
    )
finally:
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[5]/div/ul/li[10]/div/div[1]/input").click()
    print("Fourth course removed")

# Remove Roosevelt

try:
    element = WebDriverWait(browser, 1001).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[5]/div/ul/li[11]/div/div[1]/input"))
    )
finally:
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[5]/div/ul/li[11]/div/div[1]/input").click()
    print("Fifth course removed")

# Remove Sepulveda - Balboa Back 9
try:
    element = WebDriverWait(browser, 1005).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[5]/div/ul/li[13]/div/div[1]/input"))
    )
finally:
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[5]/div/ul/li[13]/div/div[1]/input").click()
    print("Sixth course removed")

# Remove Sepulveda - Encino Back 9
try:
    element = WebDriverWait(browser, 1006).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[5]/div/ul/li[15]/div/div[1]/input"))
    )
finally:
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[5]/div/ul/li[15]/div/div[1]/input").click()
    print("Seventh course removed")

# Remove Woodley Lakes - Back 9
try:
    element = WebDriverWait(browser, 1006).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[5]/div/ul/li[17]/div/div[1]/input"))
    )
finally:
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[1]/ul/li[5]/div/ul/li[17]/div/div[1]/input").click()
    print("Eighth course removed")


timeNotFound = True
i = "1"
print("Initiating time check. Please wait...")
timeList = browser.find_elements_by_css_selector("span[data-ng-bind='ec.teetimeTimeDisplay(t)']")

html = browser.find_element_by_tag_name('html')
html.send_keys(Keys.END)

for time in timeList:
    timeStr = time.text
    if len(timeInput) == 8 and timeInput[0] == '0':
        if timeInput[1:8].upper() == timeStr:
            timeNotFound = False
            break
    if timeStr == timeInput.upper():
        timeNotFound = False
        break
    else:
        number2 = int(i)+1
        i = str(number2)

if timeNotFound:
    print("No times found. Terminating...")
    exit()

try:
    element = WebDriverWait(browser, 1006).until(
        EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[2]/div[2]/div/ul/li[1]/div[3]/button"))
        )
finally:
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[2]/div[2]/div/ul/li["+i+"]/div[3]/button").click()
    print("Course found!")

try:
    element = WebDriverWait(browser, 1007).until(
        EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div/div[2]/uib-accordion/div/div[2]/div[2]/div/div/div[4]/button"))
        )
finally:
    browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/uib-accordion/div/div[2]/div[2]/div/div/div[4]/button").click()
    print("Proceeding to checkout page")

browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ui-view/div/form/div[5]/div[2]/button").click()
print("Checkout successful. Terminating program.")
exit()

