import streamlit as st

st.title('문제 분야 ')

btn_a=st.button('사회')
btn_b=st.button('예술')
btn_c=st.button('음악')

if btn_a:
    st.switch_page('사회.py')
if btn_b:
     st.switch_page('예술.py')
if btn_c:
    st.switch_page('음악.py')
