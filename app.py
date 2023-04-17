
import streamlit as st
import numpy as np
import pickle
from scipy.sparse import csr_matrix

st.header("Food recommender Web App ")

model= pickle.load(open('artifacts/model.pkl','rb'))
food_name= pickle.load(open('artifacts/food_name.pkl','rb'))
final_rating=pickle.load(open('artifacts/final_rating.pkl','rb'))
food_pivot=pickle.load(open('artifacts/food_pivot.pkl','rb'))



selected_food = st.selectbox(
    "Type/Select your recipe's name",
    food_name
)

def get_description(suggesiton):

    ids = np.where(final_rating['name']==suggesiton)[0]
    description=final_rating.iloc[ids[1]]['description']
    print(final_rating.columns)
    return description

def get_recipe(suggesiton):
    
    ids = np.where(final_rating['name']==suggesiton)[0]
    description=final_rating.iloc[ids[1]]['steps']
    #Removes brackets and quotes
    description = description.strip('[]')
    description = description.replace("'","")
    return description

def get_ingredients(suggesiton):
    
    ids = np.where(final_rating['name']==suggesiton)[0]
    ingreds=final_rating.iloc[ids[1]]['ingredients']
    #Removes brackets and quotes
    ingreds = ingreds.strip('[]')
    ingreds = ingreds.replace("'","")
    return ingreds

def recommend_food(food_name):
    food_list=[]
    food_id = np.where(food_pivot.index==food_name)[0][0]
    distance, suggestion = model.kneighbors(food_pivot.iloc[food_id,:].values.reshape(1,-1), n_neighbors=8)
    
    for i in range(len(suggestion)):
  
        food = food_pivot.index[suggestion[i]]
        for j in food:
            food_list.append(j)
    
    return(food_list)

if st.button('Show Similar Dishes'):
    
    recommendation_food = recommend_food(selected_food) 
    print(recommendation_food)
    col1, col2, col3, col4, col5 = st.columns(5, gap='large')

    with st.expander(recommendation_food[1]):
        #st.header(recommendation_food[1])
        st.write(get_description(recommendation_food[1]))
        st.write('Ingredients:', get_ingredients(recommendation_food[1]))
        st.write( get_recipe(recommendation_food[1]))
        #st.text(description[1])
    with st.expander(recommendation_food[2]):
        #st.header(recommendation_food[1])
        st.write(get_description(recommendation_food[2]))
        st.write('Ingredients:', get_ingredients(recommendation_food[2]))
        st.write( get_recipe(recommendation_food[2]))
        #st.text(description[1])
    with st.expander(recommendation_food[3]):
        #st.header(recommendation_food[1])
        st.write(get_description(recommendation_food[3]))
        st.write('Ingredients:', get_ingredients(recommendation_food[3]))
        st.write( get_recipe(recommendation_food[3]))
        #st.text(description[1])
    with st.expander(recommendation_food[4]):
        #st.header(recommendation_food[1])
        st.write(get_description(recommendation_food[4]))
        st.write('Ingredients:', get_ingredients(recommendation_food[4]))
        st.write( get_recipe(recommendation_food[4]))
        #st.text(description[1])
    with st.expander(recommendation_food[5]):
        #st.header(recommendation_food[1])
        st.write(get_description(recommendation_food[5]))
        st.write('Ingredients:', get_ingredients(recommendation_food[5]))
        st.write( get_recipe(recommendation_food[5]))
        #st.text(description[1])