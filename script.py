import gensim
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
import re
class Extractor:

    def __init__(self):
        pass

    def filegetter(self):
        book = open("gaurisbook.txt", "r")
        print "Name of file: ", book.name

    def cleanText(self, dirtyWordList):
        stopw = stopwords.words('english') + list(string.punctuation)
        return [i for i in dirtyWordList if i not in stopw]




if __name__ == '__main__':
    print("something")
    ext = Extractor()
    ext.filegetter()
    with open("gaurisbook.txt") as f:
        words = [word for line in f for word in re.findall(r"[\w']+|[.,!?;]", line)]
    cleanWordList = ext.cleanText(words)
    print(cleanWordList)




