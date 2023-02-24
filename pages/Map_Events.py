import streamlit as st
import numpy as np
st.set_page_config(page_title='Map_Events', page_icon =':ship:',layout='wide')

# st.markdown("""
# <style>

# .css-2ykyy6.egzxvld0
# {
#   visibility: hidden;
# }

# </style>""",unsafe_allow_html=True)

with st.container():
     st.subheader("Map_Events")
     st.markdown('---')
     with st.container():
          left_column, mid_column , right_column = st.columns(3)
          with left_column:
               Features=['Multiple People', 'Inside ATM but not Transcting','Helmet','Mask','camera_tempering','camera_turned_off']
               # Features = st.radio(['Multiple People', 'Inside ATM but not Transcting','Helmet','Mask','camera_tempering','camera_turned_off'])
               # st.header ("select box from a list")
               selected_features= st.multiselect("Camera_1",options = Features)
               # st.write("selectBox returns :",selected_features)
               # options = st.multiselect('Which beverage do you like?', ['Tea', 'Coffee','Iced Tea' ,'Diet Coke', 'Lemonade'],['Tea', 'Coffee'])
               Features=['Multiple People', 'Inside ATM but not Transcting','Helmet','Mask','camera_tempering','camera_turned_off']
               # Features = st.radio(['Multiple People', 'Inside ATM but not Transcting','Helmet','Mask','camera_tempering','camera_turned_off'])

               selected_features= st.multiselect("Camera_2",options = Features)
               # st.write("selectBox returns :",selected_features)
               
               Features=['Multiple People', 'Inside ATM but not Transcting','Helmet','Mask','camera_tempering','camera_turned_off']
               # Features = st.radio(['Multiple People', 'Inside ATM but not Transcting','Helmet','Mask','camera_tempering','camera_turned_off'])

               # st.header ("select box from a list")
               selected_features= st.multiselect("Camera_3",options = Features)
               # st.write("selectBox returns :",selected_features)
               
               # import streamlit as st
               # tra = st.radio('Select three known variables:', ['initial velocity (u)', 'final velocity (v)', 'acceleration (a)', 'time (t)']) 
       
          with mid_column :
               time_list=['00:00','00:30','01:00','01:30','02:00']
               
               select_time=st.selectbox("start_time",time_list)
              
               
               select_time1=st.selectbox("start_time2",time_list)
               # t= st.time_input('Set an alarm for',select_time )
               
               select_time2=st.selectbox("start_time3",time_list)
               # t = st.time_input('Set an alarm for',select_time )
               
          with right_column:
               time_list=['00:00','00:30','01:00','01:30','02:00']
               
               select_time=st.selectbox("End_time",time_list)
              
               
               select_time1=st.selectbox("End_time2",time_list)
               # t= st.time_input('Set an alarm for',select_time )
               
               select_time2=st.selectbox("End_time3",time_list)
               # t = st.time_input('Set an alarm for',select_time )
               
          st.markdown('---') 

with st.container():
     left_column, right_column = st.columns(2)
     
     with left_column:
          st.button('Back')
          st.caption("Powered by Tarsyer")    
     with right_column:
          st.button('Submit')
          st.write('info@tarsyer.com')
     st.markdown('---') 

# with st.container():
#      left_column, right_column = st.columns(2)
     
#      with left_column:
#           st.button('Back')
#           st.caption("Powered by Tarsyer")    
#      with right_column:
#           st.button('Submit')
#           st.write('info@tarsyer.com')

     
               
               
               
