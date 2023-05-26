import nltk
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity  
from nltk.stem import SnowballStemmer
from nltk.stem import PorterStemmer
from sklearn.decomposition import LatentDirichletAllocation
from nltk.tag import pos_tag
from sklearn.cluster import KMeans
from nltk.tokenize import RegexpTokenizer
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
from kneed import KneeLocator
import json
import string
import re
from wordcloud import WordCloud
import PIL.Image
from sklearn.decomposition import NMF