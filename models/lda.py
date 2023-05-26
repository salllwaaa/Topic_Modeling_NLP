from utils.preprocessing import *


def lda():
    
    ldaModelTF = LatentDirichletAllocation(n_components = 7, random_state=42)
    ldaModelTF.fit(tfidfMatrix)



    topics = []

    for index,topic in enumerate(ldaModelTF.components_):
        print(f"Top words for topic #{index}:")
        topics.append([tfidfVectorizer.get_feature_names_out()[index] for index in topic.argsort()[-10:]])

    with open ("./lda-clusters.md", "w", encoding="utf-8") as f:
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



