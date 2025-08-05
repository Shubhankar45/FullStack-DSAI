import streamlit as st
st.write("First app")
st.title("First app")
st.header("First app")
st.text('enter a name')
st.text_input('enter text')
a=st.number_input('enter a number')
st.button('Click')
st.selectbox('what you want select',
            ['Add','Subtract'])
st.checkbox('what you want select',
            ['Add','Subtract'])
st.radio('what you want select',
           ['Add','Subtract'])
# st.radio()
# st.checkbox()
# st.slider()