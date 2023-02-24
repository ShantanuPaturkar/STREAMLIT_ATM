import streamlit as st
st.set_page_config(page_title='ATM_Config_screen', page_icon =':ship:',layout='wide')

st.markdown("""
<style>

.css-2ykyy6.egzxvld0
{
  visibility: hidden;
}

</style>""",unsafe_allow_html=True)


with st.container():
     st.subheader("ATM_Config_screen")
     st.markdown('---')
     
with st.container():
     left_column, right_column = st.columns(2)
     with left_column:
          number = st.number_input('Person Confidence')
          number1 = st.number_input('Face Confidence')
          number2 = st.number_input('Helmet Confidence')
          number3 = st.number_input('Motion Confidence')
          number4 = st.number_input('No Onject Threshold')
          number5 = st.number_input('camera status ')
          number6 = st.number_input('FPS')
          sidebar1 =st.radio("Color Balancing", ["Yes","No"])
          

     with right_column:
          number7 = st.number_input('Person count >')
          number8 = st.number_input('Face Threshold ')
          number9 = st.number_input('Helmet Threshold')
          number10 = st.number_input('Mass Threshold ')
          number11 = st.number_input('Skip Frames')
          number12 = st.number_input('Camera Tempering')
          sidebar2 = st.radio("Capture Face of trasnscating user ", ["Yes","No"])
          sidebar3 = st.radio("Audio Output", ["Yes","No"])
     
     st.markdown('---') 

with st.container():
     left_column, right_column = st.columns(2)
     
     with left_column:
          st.button('Back')
          st.caption("Powered by Tarsyer")    
     with right_column:
          st.button('Submit')
          st.write('info@tarsyer.com')

