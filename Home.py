import streamlit as st
from PIL import Image
from pathlib import Path 

st.set_page_config(layout="wide")

st.title('Data Science Course (In Quotation Marks)')
curr_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

lol_loss = curr_dir / 'Images' / 'lolloss.png'


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["How this is gonna work!","Some Prior Knowledge", "The Fabled Data", "Not The Maths", "The Science?", "Even Deeper Science?"])

with tab1:
   st.subheader("What are we even doing right now?")
   st.write("""
   I'll tell you what we are doing right now (I sound like a parent). In all seriousness, I have a few motivations for creating a “CoUrSe” on data science.
  - The first is man's best motivator REJECTION. TLDR is that I’ve been rejected from my dream job at the BBC and I’ve decided that I have to go back to the basics and there is no better way of cementing your knowledge than teaching someone.
  - The second is that I have a younger cousin that looks up to me and depending on when you are reading this he will be going to university in September 2023 I would like to make something he can read in the way that we would speak to each other to make it a lot more digestible
  - The third is that I am unemployed what else am I supposed to do? It's either this or playing League of Legends and I am on a losing streak right now soooo….
   
   """)
   
   image = Image.open(lol_loss)
   col1, col2, col3 = st.columns(3)

   with col1:
    st.write(' ')

   with col2:
    st.image(image, caption='Melancholy',width=450)

   with col3:
    st.write(' ')
   
   st.divider()


   st.subheader("You haven't answered how this is gonna work?")
   st.write("""
   😐 Okay, I will try to explain core concepts of data science and machine learning. There will be many chunks of code which I will explain in-depth and elaborate on why it is done in that way.
   Also at the end of each section, I will give questions that when answered will encompass all we have learnt these questions can be used in an active recall and spaced repition method to make sure it stays in the noggin.
   """)

   st.divider() 

   st.subheader("What is the active recall active recall and spaced repition method?")
   st.write("""This is when you actively try and retrive information from memory. How it will integrate into this course when answering the end questions for each lesson in regular intervals of a week or some other period
               it will reinforce your understanding of the material and allow for the information to be actively reaclled. The quesions will not be full blown exam questions, rather questions you would ask yourself when trying to answer the whole question. Take this for example:
            """)
   st.code("""
        
        Big question:
        How does a bicycle work?

        Smaller questions:

        - What are the parts of a bicycle? \n
        - How do the wheels of a bicycle turn? \n
        - How does a person make a bicycle move forward?
   """)
   st.divider()

   st.subheader("Are you going to do semi-comedic yet holisticly cringe cutaways during the course?")
   def rambling():
      st.balloons()
      

   st.button(label='Click Here To Find Out', on_click=rambling)

with tab2:
   st.header("Some Prior Knowledge")

with tab3:
   st.header("The Fabled Data")

with tab4:
   st.header("Not The Maths")

with tab5:
   st.header("The Science?")

with tab6:
   st.header("Even Deeper Science?")
