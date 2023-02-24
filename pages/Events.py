import streamlit as st
st.set_page_config(page_title='Camera Events', page_icon =':ship:',layout='wide')
with st.container():
    st.subheader("Camera Events")
    st.markdown('---')

# st.markdown("""
# <style>

# .css-2ykyy6.egzxvld0
# {
#   visibility: hidden;
# }

# </style>""",unsafe_allow_html=True)


# st.write('Select three known variables:')
# option_1 = st.checkbox('initial velocity (u)')
# option_2 = st.checkbox('final velocity (v)')
# option_3 = st.checkbox('acceleration (a)')
# option_4 = st.checkbox('time (t)')

    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write('People')
            option_1 = st.checkbox('Multiple People')
            option_2 = st.checkbox('Duration Within the premises')
            option_3 = st.checkbox('Loitering outside the ATM')
            option_4 = st.checkbox('Loitering in Back room')
            option_5 = st.checkbox('Entry While Someone is transcating')
            option_6 = st.checkbox('Inside ATM but not Transacting')
            
        with right_column:
            
            st.write('Actions')
            option_1 = st.checkbox(' Sitting ')
            option_2 = st.checkbox('Sleeping')
            option_3 = st.checkbox('Fallen Down')
            option_4 = st.checkbox('Using Mobile while transacting')
            
            
    
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write('Face visibility')
            option_1 = st.checkbox(' Helmet')
            option_2 = st.checkbox('Scarf ')
            option_3 = st.checkbox('Sunglasses')
            option_4 = st.checkbox('Mask')
        with right_column:
            st.write('Camera')
            option_1 = st.checkbox(' Camera Tampering')
            option_2 = st.checkbox('Camera Turned Off')
            option_3 = st.checkbox('Camera Lens Covered')
            
    with st.container():
        left_column, right_column = st.columns(2)    
            
        with left_column:
            st.write('Disruption')
            option_1 = st.checkbox(' Altercation')
            option_2 = st.checkbox('Loud sounds')
        with right_column:
            st.write('ATM Condition')
            option_1 = st.checkbox(' Dirty Floor')
            option_2 = st.checkbox('Low Lighting')
            
       
    with st.container():
        left_column, right_column = st.columns(2)    
            
        with left_column:
            st.write('Device Tampering')
            option_1 = st.checkbox(' ATM moved / shook')
            option_2 = st.checkbox('Cash Box Opened')
        with right_column:
            st.write('Hard Drive')
            option_1 = st.checkbox(' Hard Drive Unavailable')
            option_2 = st.checkbox('Hard Drive Storage Full')         
    st.markdown('---')         
            
with st.container():
     left_column, right_column = st.columns(2)
     
     with left_column:
          st.button('Back')
          st.caption("Powered by Tarsyer")    
     with right_column:
          st.button('Submit')
          st.write('info@tarsyer.com')        
       


