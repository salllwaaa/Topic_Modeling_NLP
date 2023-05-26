from utils.preprocessing import *



def nmf():
    
    n_topics = 7

    nmfModel = NMF(n_components=n_topics, init='random', random_state=0)

    W = nmfModel.fit_transform(tfidfMatrix)
    H = nmfModel.components_


    featureNames = tfidfVectorizer.get_feature_names_out()

    topics = []
    for topic_idx, topic in enumerate(H):
        topics.append(feature_names[i] for i in topic.argsort()[:-6:-1])

    with open ("./nmf-clusters.md", "w", encoding="utf-8") as f:
        f.write("# Clusters\n\n")
        i = 1
        for topic in topics:
            f.write(f"## Topic {i}")
            i = i + 1
            f.write("\n\n")
            for word in topic:
                f.write ('-  %s\n' % word,)
                f.write("\n")
            f.write("\n\n---\n\n")

