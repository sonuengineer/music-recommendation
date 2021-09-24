from sklearn.metrics.pairwise import sigmoid_kernel
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import bs4 as bs
import urllib.request
import pickle
import requests


data = pd.read_csv('datasets/cleaned.csv')   




def create_sim():
    # creating a count matrix
    cv = TfidfVectorizer()
    count_matrix = cv.fit_transform(data['tags'])
    # creating a similarity score matrix
    sim = cosine_similarity(count_matrix)
    return data,sim
def rcmd(m):
    m = m.lower()
    # check if data and sim are already assigned
    try:
        data.head()
        sim.shape
    except:
        data, sim = create_sim()
    # check if the movie is in our database or not
    if m not in data['title'].unique():
        return('Sorry! This movie is not in our database. Please check the spelling or try with some other movies')
    else:
        # getting the index of the movie in the dataframe
        i = data.loc[data['title']==m].index[0]
        # fetching the row containing similarity scores of the movie
        # from similarity matrix and enumerate it
        lst = list(enumerate(sim[i]))

        # sorting this list in decreasing order based on the similarity score
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)

        # taking top 1- movie scores
        # not taking the first index since it is the same movie
        lst = lst[1:11]

        # making an empty list that will containg all 10 movie recommendations
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['title'][a])
        return l
