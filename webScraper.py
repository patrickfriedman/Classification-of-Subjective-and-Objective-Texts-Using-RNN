from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time
import datetime


def showMoreNY(passInDriver):
    showMore=passInDriver.find_elements_by_tag_name("button")
    for i in range(len(showMore)):
        if "show more" in showMore[i].text.lower():
            try:
                showMore[i].click()
                time.sleep(2)

            except:
                # time.sleep(1)
                showMore[i].click()

def getNYArticles(passInDriver):
    articles=[]
    objective1Articles=passInDriver.find_elements_by_tag_name("a")
    for i in range(len(objective1Articles)):
        # eventObject = Event()
        eventLink=objective1Articles[i].get_attribute('href')
        if ".html" in eventLink and eventLink not in articles and eventLink[25].isdigit():
            print(eventLink)
            articles.append(eventLink)
    return articles

def showMoreNPR(passInDriver):
    showMore=passInDriver.find_elements_by_tag_name("button")
    for i in range(len(showMore)):
        if "load more" in showMore[i].text.lower():
            try:
                showMore[i].click()
                # time.sleep(1)
            except:
                time.sleep(1)
                showMore[i].click()


def getNPRArticles(passInDriver):

    # passInDriver=passInDriver.find_elements_by_class_name("teaser")
    objective1Articles=passInDriver.find_elements_by_tag_name("a")
    # objective1Articles=passInDriver.
    articles=[]
    for i in range(len(objective1Articles)):

        # eventObject = Event()
        try:
            eventLink=objective1Articles[i].get_attribute('href')
            if type(eventLink)==str and "www.npr.org" in eventLink and len(eventLink)>25 and (eventLink not in articles) and eventLink[25].isdigit():
                articles.append(eventLink)
                print(eventLink)
        except:
            continue
    return articles

def main():

    # cal=Calendar()
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # https://sites.google.com/a/chromium.org/chromedriver/download
    # put driver executable file in the script directory
    chrome_driver = os.path.join(os.getcwd(), "chromedriver")

    objective1 = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    # objective2 = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    # subjective1 = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

    for i in range(3):
        if i ==0:
            print("Getting objective articles...\n")
            objective1.get("https://www.nytimes.com/section/politics")
        if i==1:
            objective1.get("https://www.npr.org/sections/politics/")
        if i==2:
            print("\n\nGetting subjective articles...\n")
            objective1.get("https://www.nytimes.com/section/opinion/politics")
        for x in range(5):
            if i ==0:
                showMoreNY(objective1)

            if i==1:
                showMoreNPR(objective1)

            if i==2:
                showMoreNY(objective1)
                time.sleep(1)
                showMoreNY(objective1)
                time.sleep(1)
                showMoreNY(objective1)
                time.sleep(1)
                showMoreNY(objective1)
        if i ==0:
            getNYArticles(objective1)
        if i==1:
            getNPRArticles(objective1)
        if i==2:
            getNYArticles(objective1)








    # Go through each event entry, gather data and determine whether they are valid entries
    #   If they are, print their information and add them to the cal (Calendar()) object




main()
