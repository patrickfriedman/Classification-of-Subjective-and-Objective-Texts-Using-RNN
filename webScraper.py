from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time
from ics import Calendar,Event
import datetime


def showMoreNY(passInDriver):
    showMore=passInDriver.find_elements_by_tag_name("button")
    for i in range(len(showMore)):
        if "show more" in showMore[i].text.lower():
            try:
                print(showMore[i].click())
                time.sleep(2)

            except:
                # time.sleep(1)
                print(showMore[i].click())

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
                print(showMore[i].click())
                # time.sleep(1)
            except:
                time.sleep(1)
                print(showMore[i].click())


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

    # objective1 = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    # objective2 = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    subjective1 = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

    # objective1.get("https://www.nytimes.com/section/politics")
    # objective2.get("https://www.npr.org/sections/politics/")
    # subjective1.get("https://www.nytimes.com/section/opinion/politics")
    # sum=0
    # for i in range(100):
    #     # if sum%3==0:
        # showMoreNY(subjective1)
    #     # if sum%3==1:
    # showMoreNY(objective1)
        # if sum%3==2:
        # showMoreNPR(objective2)
        #
        # time.sleep(1)
    # getNYArticles(subjective1)
    # getNYArticles(objective1)

    # getNPRArticles(objective2)
    #
    # getNYArticles(subjective1)

    # for i in range(300):
    #     try:
    #         showMoreNY(objective1)
    #         showMoreNPR(objective2)
    #     except:
    #         continue



    # Go through each event entry, gather data and determine whether they are valid entries
    #   If they are, print their information and add them to the cal (Calendar()) object
    sum=0



main()
