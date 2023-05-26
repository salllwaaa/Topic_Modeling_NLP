from utils.functions import *

data = pd.read_csv('./articles1.csv')

data = data[['content']]
data = data[pd.notnull(data['content'])]


dataSample = data.sample(500)


corpusA = dataSample['content'].tolist()


corpusB = []
for document in corpusA:
    corpusB.append(removeGarbage(document))


cleanData =  [cleanCorpus(doc) for doc in corpusB]


tfidfVectorizer = TfidfVectorizer(use_idf=True,ngram_range=(1,3), max_df=0.7)
tfidfMatrix = tfidfVectorizer.fit_transform(cleanData) 
feature_names = tfidfVectorizer.get_feature_names_out()
dense = tfidfMatrix.todense()
denselist = dense.tolist()

all_keywords = []

for description in denselist:
    x=0
    keywords = []
    for word in description:
        if word > 0:
            keywords.append(feature_names[x])
        x=x+1
    all_keywords.append(keywords)

