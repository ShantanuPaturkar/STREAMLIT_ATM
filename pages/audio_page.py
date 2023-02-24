import streamlit as st
# from pydub import AudioSegment
st.set_page_config(page_title='Setup', page_icon =':ship:',layout='wide')


st.markdown("""
<style>

.css-2ykyy6.egzxvld0
{
  visibility: hidden;
}

</style>""",unsafe_allow_html=True)
with st.container():
    st.subheader("Camera Setup ")
    st.markdown('---')
    st.write('Audio Config') 
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
          time= st.slider('Time Interval_1', 0, 300, 0)
          st.write("Time interval in playing the audio ", time ,' seconds')
          option_1 = st.checkbox('Multiple_People')
          if option_1 :
                
              Features=['Multiple People', 'Inside ATM but not Transcting','Helmet','Mask','camera_tempering','camera_turned_off']
              selected_features= st.multiselect("Multiple_People",options = Features)
         
              
          else :
                None
               
          option_2 = st.checkbox('Duration Within Premises')
          if option_2 :
                
              Features=['Multiple People', 'Inside ATM but not Transcting','Helmet','Mask','camera_tempering','camera_turned_off']
                  
              selected_features= st.multiselect("Duration Within Premises",options = Features)
        
          else :
                None
          
          option_3 = st.checkbox('Inside ATM But not transacting ')
          if option_3 :
                
              Features=['Multiple People', 'Inside ATM but not Transcting','Helmet','Mask','camera_tempering','camera_turned_off']
                  
              selected_features= st.multiselect("Inside ATM But not transacting ",options = Features)
             
          else :
                None
          option_4 = st.checkbox('Helmet')
          if option_4 :
                
              Features=['Multiple People', 'Inside ATM but not Transcting','Helmet','Mask','camera_tempering','camera_turned_off']
                 
              selected_features= st.multiselect("Helmet ",options = Features)
               
          else :
                None
          option_5 = st.checkbox('Mask')
          if option_5 :
                
              Features=['Multiple People', 'Inside ATM but not Transcting','Helmet','Mask','camera_tempering','camera_turned_off']
                  
              selected_features= st.multiselect("Mask",options = Features)
               
          else :
                None
          option_6 = st.checkbox('Camera tempering')
          if option_6 :
                
              Features=['Multiple People', 'Inside ATM but not Transcting','Helmet','Mask','camera_tempering','camera_turned_off']
                   
              selected_features= st.multiselect("Camera tempering",options = Features)
          else :
                None
          option_7 = st.checkbox('Camera Turned off')
          if option_7:
                
              Features=['Multiple People', 'Inside ATM but not Transcting','Helmet','Mask','camera_tempering','camera_turned_off']
                  
              selected_features= st.multiselect("Camera Turned off",options = Features)
          else :
                None
          option_8 = st.checkbox('Camera lens covered ')
          if option_8 :
                
              Features=['Multiple People', 'Inside ATM but not Transcting','Helmet','Mask','camera_tempering','camera_turned_off']
                   
              selected_features= st.multiselect("Camera lens covered",options = Features)
               
          else :
                None
          
          
        with right_column:  
            
          seconds= st.slider('Time Interval_2', 0, 300, 0)
          st.write("Time interval in playing the audio ", seconds,' seconds')
          option_1= st.slider('Multiple_People_vol', 0, 100, 0)
          option_2= st.slider('Duration_Vol', 0, 100, 0)
          option_3= st.slider('Inside_vol', 0, 100, 0)
          option_4= st.slider('Helmet_vol', 0, 100, 0)
          option_5= st.slider('Mask_vol', 0, 100, 0)
          option_6= st.slider('Camera_tempering', 0, 100, 0)
          option_7= st.slider('Camera Turned off_vol', 0, 100, 0)
          option_8= st.slider('Camera lens covered_vol', 0, 100, 0)
      
    st.markdown('-------') 
    
    with st.container():
        left_column, right_column = st.columns(2)
        # you can upload multiple files
        with left_column:
            uploaded_files = st.file_uploader("Upload The mp3 file", accept_multiple_files=True)
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                st.write(bytes_data)
    


        with right_column:
            st.markdown('') 
            st.markdown('')
            st.markdown('')
            call = st.button('upload')
    
     
            # sound = AudioSegment.from_mp3("/path/to/file.mp3")
            # sound.export("/output/path/file.wav", format="wav")
    st.markdown('') 

    with st.container():
        left_column , mid_column ,  right_column , extr_column =st.columns(4)
        with left_column:       
            st.markdown("TEST AUDIO CLIP")
            Features=['Multiple People', 'Inside ATM but not Transcting','Helmet','Mask','camera_tempering','camera_turned_off']
            selected_features= st.multiselect("Camera_1",options = Features)
        with mid_column:
            st.markdown('') 
            st.markdown('')
            st.markdown("TEST AUDIO CLIP")
            call = st.button('Play')  
            
        with right_column:
            # st.markdown('') 
            # st.markdown('')
            st.markdown('Audio Volume') 
            option_100 = st.slider('', 0, 100, 0)
            
        st.markdown('--------') 
        
    with st.container():
        left_column, right_column = st.columns(2)
     
        with left_column:
            st.button('Back')
            st.caption("Powered by Tarsyer")    
        with right_column:
            st.button('Submit')
            st.write('info@tarsyer.com')
            
        
        
          

          
          
            
            