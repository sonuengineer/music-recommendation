#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 09:35:33 2021

@author: anonymous
"""
import numpy as np
from sklearn.metrics.pairwise import sigmoid_kernel
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import bs4 as bs
import urllib.request
import pickle
import requests
from model import rcmd


data = pd.read_csv('datasets/cleaned.csv')   

app = Flask(__name__)
def get_suggestions():
    return list(data['title'])
@app.route("/")
@app.route("/home")
def home():
    suggestions = get_suggestions()
    return render_template('home.html',suggestions=suggestions)
@app.route("/recommender")
def recommender():
    data = pd.read_csv('datasets/cleaned.csv')
    music = request.args.get('music')
    music_raw=data[data['title']== music]
    title=music_raw['title'].values[0]
    video_id=music_raw['video_id'].values[0]
    publlisheddate=music_raw['publishedate'].values[0]
    poster=music_raw['Thumbnails_url'].values[0]
    views=music_raw['views'].values[0]
    likes=music_raw['likes'].values[0]
    dislikes=music_raw['dislikes'].values[0]
#Recommendation1 
    rcmnd=rcmd(music)
    rmnd1=rcmnd[0]
    music_raw1=data[data['title']== rmnd1]
    title1=music_raw1['title'].values[0]
    video_id1=music_raw1['video_id'].values[0]
    publlisheddate1=music_raw1['publishedate'].values[0]
    views1=music_raw1['views'].values[0]
    likes1=music_raw1['likes'].values[0]
    dislikes1=music_raw1['dislikes'].values[0]
    rmndlist1=[title1,video_id1,publlisheddate1,views1,likes1,dislikes1]
#Recommendation2
    rmnd2=rcmnd[1]
    music_raw2=data[data['title']== rmnd2]
    title2=music_raw2['title'].values[0]
    video_id2=music_raw2['video_id'].values[0]
    publlisheddate2=music_raw2['publishedate'].values[0]
    views2=music_raw2['views'].values[0]
    likes2=music_raw2['likes'].values[0]
    dislikes2=music_raw2['dislikes'].values[0]
    rmndlist2=[title2,video_id2,publlisheddate2,views2,likes2,dislikes2]
#Recommendation3
    rmnd3=rcmnd[2]
    music_raw3=data[data['title']== rmnd3]
    title3=music_raw3['title'].values[0]
    video_id3=music_raw3['video_id'].values[0]
    publlisheddate3=music_raw3['publishedate'].values[0]
    views3=music_raw3['views'].values[0]
    likes3=music_raw3['likes'].values[0]
    dislikes3=music_raw3['dislikes'].values[0]
    rmndlist3=[title3,video_id3,publlisheddate3,views3,likes3,dislikes3]  
    #Recommendation4
    rmnd4=rcmnd[3]
    music_raw4=data[data['title']== rmnd4]
    title4=music_raw4['title'].values[0]
    video_id4=music_raw4['video_id'].values[0]
    publlisheddate4=music_raw4['publishedate'].values[0]
    views4=music_raw4['views'].values[0]
    likes4=music_raw4['likes'].values[0]
    dislikes4=music_raw4['dislikes'].values[0]
    rmndlist4=[title4,video_id4,publlisheddate4,views4,likes4,dislikes4] 
     #Recommendation5
    rmnd5=rcmnd[4]
    music_raw5=data[data['title']== rmnd5]
    title5=music_raw5['title'].values[0]
    video_id5=music_raw5['video_id'].values[0]
    publlisheddate5=music_raw5['publishedate'].values[0]
    views5=music_raw5['views'].values[0]
    likes5=music_raw5['likes'].values[0]
    dislikes5=music_raw5['dislikes'].values[0]
    rmndlist5=[title5,video_id5,publlisheddate5,views5,likes5,dislikes5] 
    
    
    
    
    return render_template ('recommend.html',title=title,publlisheddate=publlisheddate,video_id=video_id,dislikes=dislikes,likes=likes,views=views,poster=poster,rmndlist1=rmndlist1,rmndlist2=rmndlist2,rmndlist3=rmndlist3,rmndlist4=rmndlist4,rmndlist5=rmndlist5)




if __name__ == '__main__':
    app.run(debug=True)
