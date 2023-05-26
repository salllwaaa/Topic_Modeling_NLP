from utils.libraries import *
from utils.vars import *



# documentTokensTokens --> is documentTokensTokens represented as a list of words (tokens).
# stopWords --> is a list of stopWords we want to remove.
def removeStopWords(documentTokens, stopWords):
   return [word for word in documentTokens if word.casefold() not in stopWords] 



   
# documentTokens --> is documentTokens represented as a list of words (tokens).
def removePunctuations(documentTokens):
    filteredDocumentTokens =  [''.join(char for char in word if char not in string.punctuation) for word in documentTokens]
    return [word for word in filteredDocumentTokens if len(word) > 0]



# documentString --> is document (string)
# tis function --> remove Numbers, Date, Time and Symbols.
def removeGarbage(documentString):
    return re.sub(r'\d+:\d+ p\. m\.||\d+:\d+ a\. m\.||\d+||■', "", documentString)





# documentTokens --> is documentTokens represented as a list of words (tokens).
def shrinkSpaces(documentTokens):
     return [word for word in documentTokens if len(word) > 1]


# documentTokens --> is document represented as a list of words (tokens).
def lemmatize(documentTokens):
    lemmatizer = WordNetLemmatizer()
    treeBankTags = pos_tag(documentTokens)

    lemmas = []
    for tokTag in treeBankTags:
        lem = lemmatizer.lemmatize(tokTag[0], pos=tagMap[tokTag[1]])
        lemmas.append(lem)
        
    return lemmas

    




def getStopWords():
    enStopWords =  list(stopwords.words('english'))
    return enStopWords + stops["days"] + stops["numbers"] + stops["months"] + stops["items"] + stops["aStops"] + stops["bStops"]



def stem(tokens, opt):
    # 0 --> porter
    # 1 --> snowball
    if opt == 0:
        stemmer = PorterStemmer()
        return [stemmer.stem(token) for token in tokens]
    else:
        stemmer = SnowballStemmer("english")
        return [stemmer.stem(token) for token in tokens]
        

def cleanCorpus(text):
    pattern = r'\b[A-Z]\.\s(?:[A-Z]\.\s)*[A-Z]+\b|\w+'
    tokenizer = RegexpTokenizer(pattern)
    tokens = [word for sent in nltk.sent_tokenize(text) for word in tokenizer.tokenize(sent)]
    t1 = removePunctuations(tokens)
    t2 = removeStopWords(t1, getStopWords())
    t3 = shrinkSpaces(t2)
    # t4 = lemmatize(t3)
    t5 = stem(t3, 1)

    return ' '.join(t5)


       