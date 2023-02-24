import streamlit as st
st.set_page_config(page_title='ATM_Config_screen', page_icon =':ship:',layout='wide')

# st.markdown("""
# <style>

# .css-2ykyy6.egzxvld0
# {
#   visibility: hidden;
# }

# </style>""",unsafe_allow_html=true)


with st.container():
    st.subheader("Log")
    st.markdown('---')
     
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        number =  st.text_input('Top_camera_1')
        number1 = st.text_input('Top_camera_2')
        number2 = st.text_input('Front_camera')
        number3 = st.text_input('Motion Confidence')
        number4 = st.text_input('Images')
        number5 = st.text_input('Videos')
        # number6 = st.text_input('FPS')
        # sidebar1 =st.radio("Color Balancing", ["Yes","No"])
        
    # with right_column:
    #     number7 = st.text_input('Motion Confidence')
    #     number8 = st.text_input('Images')
    #     number9 = st.text_input('Videos') 
                                                  
        
    st.markdown('---') 
        
with st.container():
     left_column, right_column = st.columns(2)
     
     with left_column:
          st.button('Back')
          st.caption("Powered by Tarsyer")    
     with right_column:
          st.button('Submit')
          st.write('info@tarsyer.com')
          