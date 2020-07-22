import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Welcome to my world, a world where all the secrets will be revealed.')
imag = Image.open('Banner.jpg')
st.image(imag,use_column_width=True)
imag2= Image.open('Result.jpg')
my_list=[]

st.header("To unlock the secrets, let's see how well you knoe me?")
st.subheader('Answer the following questions about me (there is only one correct answer)')
adventure = st.multiselect('Which is my favourite adventure sport?', ['Sky Diving','Scuba Diving','Bungee Jumping'])
my_list.append(adventure)
holiday= st.multiselect('Which place is my dream holiday destination', ['The Alps, Switzerland','The Hollywood,California','Athenian Riviera, Greece'])
my_list.append(holiday)
dress = st.multiselect('What was the dress that I wore for my first date?', ['Red Dress','Leather Jacket and Boot', 'Pink Jumpsuit'])
my_list.append(dress)
john = st.multiselect('Who is Jacob?', ['Best Friend','Boy Friend', 'First Cousin'])
my_list.append(john)
food = st.multiselect('The cuisine that tops the list of my favourite food?', ['Japanesse','Korean', 'Italian'])
my_list.append(food)
wedding = st.multiselect('When did my best friend Beth get married?', ['10 January, 2018','12 March, 2018', '26 September, 2018'])
my_list.append(wedding)

if st.button('Press this button when ready'):
    df= pd.DataFrame({'tag_list': [my_list]})
    df.to_csv('Wishlist.csv')
    cust_tags_list= pd.read_csv('Wishlist.csv') 
    s = cust_tags_list.tag_list[0]
    correct_ans= 'Sky Diving, The Hollywood,California, Leather Jacket and Boot, Best Friend, South Indian, 12 March, 2018'
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
            st.write('Welcome the world of my deepest secrests')
            st.image(imag2,use_column_width=True)
            keep_playing = "false"
        else:
            if app2 != correct_ans:
                st.write("Sorry, that is not the correct answer. Try again!")
                keep_playing = "false"
                
                                
                
                
            
        
    
