import re, requests, string, time
from bs4 import BeautifulSoup

start_time = time.time()

def sub() :
	with open('subjective.txt') as file1:
		articleCollection = []
		superString = ''
		progress = 0
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
			output = regex.sub('', output.lower())


			dictF = open("dict.txt","r+")  
			dictionary = dictF.read()
			dictionary = dictionary.split()
			dictF.close()

			wordTokens = ''
			wordTokensUntrimmed = output.split()

			for each in wordTokensUntrimmed:
				if each in dictionary:
					wordTokens = wordTokens + each + ' '

			progress = progress + 1
			print("Subjective article: ", progress)
			
			# print(wordTokens)
			# print()

			articleCollection.append(wordTokens.split(' '))
			superString = superString + wordTokens

		progress = 0
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

			progress = progress + 1
			print("Subjective data: ", progress)

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
		progress = 0
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
			output = regex.sub('', output.lower())


			dictF = open("dict.txt","r+")  
			dictionary = dictF.read()
			dictionary = dictionary.split()
			dictF.close()

			wordTokens = ''
			wordTokensUntrimmed = output.split()

			for each in wordTokensUntrimmed:
				if each in dictionary:
					wordTokens = wordTokens + each + ' '

			progress = progress + 1
			print("Objective article: ", progress)
			
			# print(wordTokens)
			# print()

			articleCollection.append(wordTokens.split(' '))
			superString = superString + wordTokens

		progress = 0
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

			progress = progress + 1
			print("Objective data: ", progress)

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

def timer(start,end):
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))

sub()
obj()
print()

timer(0.0, (time.time() - start_time))

#50
#00:02:39.38			00:03:26.20
#00:02:41.19			00:03:25.63         36% Improvement
#00:02:43.71			00:03:25.65

#100
#00:17:56.06			00:22:34:52         30% Improvement
