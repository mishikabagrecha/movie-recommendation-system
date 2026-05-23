import numpy as np
import pandas as pd
import ast # abstract syntax tree to convert stringified list of dictionaries to list of strings
import nltk # natural language processing toolkit

movies=pd.read_csv("tmdb_5000_credits.csv")
credits=pd.read_csv("tmdb_5000_movies.csv")
#print(movies.head(1))

movies=movies.merge(credits,on="title")
print(movies.head(1))
# print(movies.shape) to check the number of rows and columns

# extracr tags from dataset columns
movies=movies[["movie_id","title","overview","genres","keywords","cast","crew"]]

#preprocessing the data
movies.isnull().sum() # here 3 columns have null values, we will drop those rows
movies.dropna(inplace=True)
movies.isnull().sum()# now we have no null values in our dataset

movies.duplicated().sum()# to check if we have any duplicate rows in our dataset

# now we will convert the stringified list of dictionaries to a list of strings
# Genres of movies:
def convert(obj): #here it was stringified list of dic
    L=[]
    for i in ast.literal_eval(obj): #ast.literal_eval is use to convert dic to list 
         L.append(i["name"])
    return L

movies["genres"]=movies["genres"].apply(convert)
# here we have converted the stringified list of dictionaries to a list of strings for genres column

# now for same thing for keywords column:
movies["keywords"]=movies["keywords"].apply(convert)

# now for cast column:
def convert3(obj): #we only want top 3 cast names
     L=[]   
     counter=0
     for i in ast.literal_eval(obj):
          if counter!=3:
               L.append(i["name"])
               counter+=1
          else:
                break
     return L
     
     
movies["cast"]=movies["cast"].apply(convert3) 


# fetch director only from crew column:

def fetch_director(obj):
      L=[]
      for i in ast.literal_eval(obj):
           if i["job"]=="Director":
                L.append(i["name"])
                break
      return L
movies["crew"]=movies["crew"].apply(fetch_director)

#now overview col into list of words:

movies["overview"]=movies["overview"].apply(lambda x:x.split())

# remove spaces between words in list:
movies["genres"]=movies["genres"].apply(lambda x:[i.replace(" ","")for i in x])
movies["keywords"]=movies["keywords"].apply(lambda x:[i.replace(" ","")for i in x])
movies["cast"]=movies["cast"].apply(lambda x:[i.replace(" ","")for i in x])
movies["crew"]=movies["crew"].apply(lambda x:[i.replace(" ","")for i in x])

# create col tag : to concatenate all the cols in one

movies["tag"]=movies["overview"]+movies["genres"]+movies["keywords"]+movies["cast"]+movies["crew"]

# new dataframe df with only movie_id,title and tag col
new_df=movies[["movie_id","title","tag"]]

# convert list of tags into string
new_df["tag"]=new_df["tag"].apply(lambda x:" ".join(x))
# convert all the tags into lower case
new_df["tag"]=new_df["tag"].apply(lambda x:x.lower())
#print(new_df["tag"][0]) to check the tag of first movie

#vectorization of tags using count vectorizer- 
# vectorization is the process of converting text data into numerical 
# data so that it can be used for machine learning algorithms

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=5000,stop_words="english") # here we have set max_features to 5000 to keep only top 5000 words and 
#stop_words to english to remove common words like the, is, etc.

vectors=cv.fit_transform(new_df["tag"]).toarray() # here we have converted the tags into numerical data

cv.get_feature_names_out()

from nltk.stem.porter import PorterStemmer 
ps=PorterStemmer() # stemming is the process of reducing a word to its root form
# for example: liked, liking, likes all will be reduced to like
def stem(text):
     y=[]
     for i in text.split():
          y.append(ps.stem(i)) # stremming apply here
     return " ".join(y) # here we have converted the list of stemmed words into a string

new_df["tag"]=new_df["tag"].apply(stem) # here we have applied stemming to the tags

#4806 movies= 4806 vectors with 5000 words each

# now to calculate the similarity between the movies we will use cosine similarity because
# euclidean distance is not a good measure of similarity for high dimensional data like text data
# cosine similarity is the angle between two vectors and it ranges from -1 to 1, 
# where 1(0 degree) means the vectors are identical and -1(180 degrees) means the vectors are opposite
# distance is inverse of similarity, so smaller the distance more similar the movies are

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors).astype('float32')
print(similarity.shape)
# (4806,4806) because we have 4806 movies and we are calculating the similarity between each movie with every other movie

# sorted list of tuples where each tuple is (index of movie, similarity score)
#  and we have sorted it in reverse order so that the most similar movies come first

def recommend(movie):
     movie_index=new_df[new_df["title"]==movie].index[0]  
     # here we are getting the index of the movie for which we want to find similar movies 
     distances=similarity[movie_index] #  the similarity scores of the movie with all other movies
     movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6] 


     for i in movies_list:
          print(new_df.iloc[i[0]].title) # here we are printing the titles of the top 5 similar movies

recommend("The Dark Knight Rises") # here we are finding the similar movies to "The Dark Knight Rises"


#here we are saving the new_df dataframe as a pickle file so that we can use it in our app.py file to recommend
#  movies without having to run the entire code again

import pickle

pickle.dump(new_df.to_dict(), open("movies_dict.pkl", "wb"))
pickle.dump(similarity, open("similarity.pkl", "wb"))

