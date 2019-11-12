from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import os.path
from os import path
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
    NYArticles=passInDriver.find_elements_by_tag_name("a")
    for i in range(len(NYArticles)):
        eventLink=NYArticles[i].get_attribute('href')
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
                time.sleep(2)
            except:
                # time.sleep(1)
                showMore[i].click()


def getNPRArticles(passInDriver):

    NPRArticles=passInDriver.find_elements_by_tag_name("a")
    articles=[]
    for i in range(len(NPRArticles)):

        try:
            eventLink=NPRArticles[i].get_attribute('href')
            if type(eventLink)==str and "www.npr.org" in eventLink and len(eventLink)>30 and (eventLink not in articles):
                articles.append(eventLink)
                print(eventLink)
        except:
            continue
    return articles
def getNPRArchives(passInDriver):


def readFoundArticles(txtFileString):
    articles=[]
    if path.exists(txtFileString):
        txtFile=open(txtFileString,"r")
        lines=txtFile.readlines()
        for line in lines:
            articles.append(line)
    return articles

def writeFoundArticles(txtFileString,articles):
    txtFile=open(txtFileString,"a+")
    for article in articles:
        txtFile.write(article+"\n")
def removeDuplicates(txtFileString,articles):
    alreadyFound=readFoundArticles(txtFileString)
    if len(alreadyFound)<len(articles):
        for article in alreadyFound:
            if articles.count(article)>0:
                articles.remove(article)
    elif len(alreadyFound)>len(articles):
        for article in articles:
            if alreadyFound.count(article)>0:
                articles.remove(article)
    else:
        for article in articles:
            if alreadyFound.count(article)>0:
                articles.remove(article)

    return articles

def main():


    # cal=Calendar()
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # https://sites.google.com/a/chromium.org/chromedriver/download
    # put driver executable file in the script directory
    chrome_driver = os.path.join(os.getcwd(), "chromedriver")

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    # objective2 = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    # subjective1 = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

    for i in range(3):
        if i ==0:
            print("Getting objective articles...\n")
            driver.get("https://www.nytimes.com/section/politics")
        if i==1:
            driver.get("https://www.npr.org/sections/politics/")
        if i==2:
            print("\n\nGetting subjective articles...\n")
            driver.get("https://www.nytimes.com/section/opinion/politics")
        clickedMore=0
        for x in range(100):
            if i ==0:
                showMoreNY(driver)
                clickedMore=clickedMore+1
                print("Clicked show more "+ str(clickedMore)+" time.")
            if i==1:
                showMoreNPR(driver)
                clickedMore=clickedMore+1
                print("Clicked load more "+ str(clickedMore)+" time.")
            if i==2:
                showMoreNY(driver)
                clickedMore=clickedMore+1
                print("Clicked show more "+ str(clickedMore)+" time.")
        if i ==0:
            articles=getNYArticles(driver)
            articles=removeDuplicates("objective.txt",articles)
            writeFoundArticles("objective.txt",articles)
        if i==1:
            articles=getNPRArticles(driver)
            articles=removeDuplicates("objective.txt",articles)
            writeFoundArticles("objective.txt",articles)
        if i==2:
            articles=getNYArticles(driver)
            articles=removeDuplicates("subjective.txt",articles)
            writeFoundArticles("subjective.txt",articles)












main()
