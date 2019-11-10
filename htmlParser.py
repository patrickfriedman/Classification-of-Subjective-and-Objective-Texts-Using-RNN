import re, requests, string
from bs4 import BeautifulSoup

def sub() :
    with open('subjective.txt') as file1:
        articleCollection = []
        superString = ''
        for line in file1:
            url = line
            res = requests.get(url)
            html_page = res.content
            soup = BeautifulSoup(html_page, 'html.parser')
            text = soup.find_all(text=True)

            output = ''
            blacklist = [
                '[document]',
                'noscript',
                'header',
                'html',
                'meta',
                'head', 
                'input',
                'script',
                'style',
            ]

            for t in text:
                if t.parent.name not in blacklist:
                    output += '{} '.format(t)
            regex = re.compile('[^a-zA-Z ]')
            output = regex.sub('',output)
            output = output.lower()

            articleCollection.append(output.split(' '))
            superString = superString + output

        freqList = []
        for x in sortFreq(words(superString)) :
            freqList.append(x)

        newList = []
        for each in freqList:
            newList.append(each[1])

        convertedCollection = []
        for article in articleCollection:
            tokenizedArticle = []
            for word in article:
                if newList.index(word) != 0:
                    tokenizedArticle.append(newList.index(word))
            convertedCollection.append(tokenizedArticle)
        
        finalSub = open('finalSub.txt','w')
        for each in convertedCollection:
            for nums in each:
                finalSub.write(str(nums))
                finalSub.write(' ')
            finalSub.write('\n')
        
        finalSub.close()
    file1.close()

def obj() :
    with open('objective.txt') as file1:
        articleCollection = []
        superString = ''
        for line in file1:
            url = line
            res = requests.get(url)
            html_page = res.content
            soup = BeautifulSoup(html_page, 'html.parser')
            text = soup.find_all(text=True)

            output = ''
            blacklist = [
                '[document]',
                'noscript',
                'header',
                'html',
                'meta',
                'head', 
                'input',
                'script',
                'style',
            ]

            for t in text:
                if t.parent.name not in blacklist:
                    output += '{} '.format(t)
            regex = re.compile('[^a-zA-Z ]')
            output = regex.sub('',output)
            output = output.lower()

            articleCollection.append(output.split(' '))
            superString = superString + output

        freqList = []
        for x in sortFreq(words(superString)) :
            freqList.append(x)

        newList = []
        for each in freqList:
            newList.append(each[1])

        convertedCollection = []
        for article in articleCollection:
            tokenizedArticle = []
            for word in article:
                if newList.index(word) != 0:
                    tokenizedArticle.append(newList.index(word))
            convertedCollection.append(tokenizedArticle)

        finalObj = open('finalObj.txt','w')
        for each in convertedCollection:
            for nums in each:
                finalObj.write(str(nums))
                finalObj.write(' ')
            finalObj.write('\n')

        finalObj.close()
    file1.close()

def words(output) :
    wordstring = output

    wordlist = []
    for x in re.split(r'(\w+)', wordstring) : wordlist.append(x.strip())

    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))

    return dict(zip(wordlist, wordfreq))

def sortFreq(freq) :
    sort = [(freq[key], key) for key in freq]
    sort.sort()
    sort.reverse()
    return sort

sub()
obj()
