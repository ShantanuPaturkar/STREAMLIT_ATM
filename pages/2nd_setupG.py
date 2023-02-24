import streamlit as st
st.set_page_config(page_title='Setup', page_icon =':ship:',layout='wide')


# st.markdown("""
# <style>

# .css-2ykyy6.egzxvld0
# {
#   visibility: hidden;
# }

# </style>""",unsafe_allow_html=True)



with st.container():
    st.subheader("Camera Setup ")
    st.markdown('---')
    st.write('General')
    with st.container():
        left_column, mid_column , right_column = st.columns(3)
        with left_column:
          option_1 = st.checkbox('Top Camera-1')
          opt1     = st.text_input('username')  
          password = st.text_input("Enter a password", type="password")
             
        with mid_column:
          option_2 = st.checkbox('Top Camera-2')
          opt3     = st.text_input('username-2')  
          password = st.text_input("Enter a password-2", type="password")
         
        with right_column:
          option_3 = st.checkbox('Front Camera')
          opt5    = st.text_input('username-f')  
          password = st.text_input("Enter a password-3", type="password")
          
    st.markdown('-------') 
    st.write("Config")  
       
    with st.container():
      left_column,  right_column = st.columns(2)      
      with left_column:
        opt7=st.text_input('Json IP')
        opt8=st.text_input("Device IP")
      with  right_column:
        opt9=st.text_input('Json Port ')
        opt10=st.text_input("DVR IP")
        
    st.markdown('-------')        
    
    
with st.container():
     left_column, right_column = st.columns(2)
     
     with left_column:
          st.button('Back')
          st.caption("Powered by Tarsyer")    
     with right_column:
          st.button('Submit')
          st.write('info@tarsyer.com')