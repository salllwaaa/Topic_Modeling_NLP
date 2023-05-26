from utils.preprocessing import *


def kmeans():
    
    ## ---> Elbou <----- #

    # K=range(2,40)
    # wss = []

    # for k in K:
    #     kmeans= KMeans(n_clusters=k)
    #     kmeans=kmeans.fit(tfidfMatrix)
    #     wssiter = kmeans.inertia_
    #     wss.append(wssiter)

    # plt.figure(figsize=(7,7))
    # plt.xlabel('K')
    # plt.ylabel('Within-Cluster-Sum of Squared Errors (WSS)')
    # plt.plot(K,wss)

    # kl = KneeLocator(K, wss, curve='convex', direction='decreasing')
    # optimal_k = kl.elbow

    # print(f"The optimal number of clusters is {optimal_k}")




    kNum = 3

    kmeansModel = KMeans(n_clusters=kNum, init="k-means++", max_iter=100, n_init=1)
             
    kmeansModel.fit(tfidfMatrix)

    clusters = kmeansModel.labels_.tolist()


    order_centroids = kmeansModel.cluster_centers_.argsort()[:, ::-1]

    terms = tfidfVectorizer.get_feature_names_out()

    with open ("./kmeans-clusters.md", "w", encoding="utf-8") as f:
        f.write("# Clusters\n\n")
        for i in range(kNum):
            f.write(f"## Cluster {i+1}")
            f.write("\n\n")
            for ind in order_centroids[i, :20]:
                f.write ('-  %s\n' % terms[ind],)
                f.write("\n")
            f.write("\n\n---\n\n")


    for i in range(kNum):
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(all_keywords[i]))
        plt.figure(figsize=(8, 4))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.title(f'Cluster {i+1} Word Cloud')
        plt.axis('off')
        plt.show()


# ----------------------------------> VISUALIZATION <----------------------------------------- #

# Similarity
    similarityDistance = 1 - cosine_similarity(tfidfMatrix)


# Convert two components as we're plotting points in a two-dimensional plane
    mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
    pos = mds.fit_transform(similarityDistance)  # shape (n_components, n_samples)
    xs, ys = pos[:, 0], pos[:, 1]

#Set up colors per clusters using a dict
    cluster_colors = {0: '#1b9e77', 1: '#d95f02', 2: '#7570b3', 3: '#e7298a', 4: '#66a61e',5: '#D2691E'}

#set up cluster names using a dict
    cluster_names = {0: 'news, social', 
                     1: 'donald trump, united states, obama', 
                     2: 'north korea, china, missile', 
                     }

# # Finally plot it
# %matplotlib inline 

#Create data frame that has the result of the MDS and the cluster 
    df = pd.DataFrame(dict(x=xs, y=ys, label=clusters)) 
    groups = df.groupby('label')

# Set up plot
    fig, ax = plt.subplots(figsize=(17, 9)) # set size

    for name, group in groups:
        ax.plot(group.x, group.y, marker='o', linestyle='', ms=20, 
                label=cluster_names[name], color=cluster_colors[name], 
                mec='none')
        ax.set_aspect('auto')
        ax.tick_params(\
            axis= 'x',          
            which='both',      
            bottom='off',     
            top='off',         
            labelbottom='off')
        ax.tick_params(\
            axis= 'y',        
            which='both',    
            left='off',     
            top='off',       
            labelleft='off')
                
    ax.legend(numpoints=1) 
    plt.show()


