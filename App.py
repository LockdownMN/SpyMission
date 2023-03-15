import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Welcome, Secret Agent.')
imag = Image.open('SpyBanner.jpg')
st.image(imag,use_column_width=True)
imag2= Image.open('Match.jpg')
my_list=[]

st.header("Varify your identity before you proceed!")
st.subheader('Answer the following questions. (There is only 1 correct answer)')
adventure = st.multiselect('What was your rank in Operation Blue Lotus?', ['Sergeant','Flight Cadet','Group Captain'])
my_list.append(adventure)
dress = st.multiselect('Which operation was our most successful operation that got us a Medal of Honor?', ['Blue Lotus','Sky Light', 'Hill Top'])
my_list.append(dress)
john = st.multiselect('We successfully infiltraded the Secret Nuclear Program of which country?', ['Japan','North Korea', 'South Korea'])
my_list.append(john)
food = st.multiselect('Which is our only mission that failed?', ['Sky Light','Night Dawn', 'Black Hawk'])
my_list.append(food)

if st.button('Press this button when ready'):
    df= pd.DataFrame({'tag_list': [my_list]})
    df.to_csv('Wishlist.csv')
    cust_tags_list= pd.read_csv('Wishlist.csv') 
    s = cust_tags_list.tag_list[0]
    correct_ans= 'Flight Cadet, Sky Light, South Korea, Black Hawk'
    guesses_remaining = 3
    #Clean the string
    def listToString(s):    
            str1 = ""
            for ele in s:  
                str1 += ele     
            return str1 
    
    hello=listToString(s)
    app=hello.replace('[', '')
    app1=app.replace(']', '')
    app2=app1.replace("'", "")
    keep_playing = "true"
    while keep_playing == "true":
        guesses_remaining = guesses_remaining - 1
        if app2 == correct_ans:
            st.write('Welcome abode Secret Agent!')
            st.image(imag2,use_column_width=True)
            keep_playing = "false"
        else:
            if app2 != correct_ans:
                st.write("Sorry, your answers are not correct. Please Try again!")
                keep_playing = "false"
                
                                
                
                
            
        
    
