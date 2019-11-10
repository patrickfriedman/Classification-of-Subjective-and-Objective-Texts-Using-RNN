import re, requests, string
from bs4 import BeautifulSoup

def obj() :
    with open('objective.txt') as file1:
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
            regex = re.compile('[^a-zA-Z +]')
            output = regex.sub('',output)

            sep = 'The Times is committed to publishing  a diversity of letters  to the editor. We’d like to hear what you think about this or any of our articles.'
            output = output.split(sep, 1)[0]

            return str(output)
            # for x in sortFreq(words(output)) :
            #     print(str(x))
            # print()
        
    file1.close()

def sub() :
    with open('subjective.txt') as file1:
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
            regex = re.compile('[^a-zA-Z +]')
            output = regex.sub('',output)

            print(output)
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

obj()
print()
#sub()