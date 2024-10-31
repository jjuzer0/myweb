import streamlit as st 

st.set_page_config(
page_title='시사상식 퀴즈',page_icon='🕵️‍♂️'
)

st.title('🕵️‍♂️로그인🕵️‍♂️')
id=st.text_input('아이디')
pw=st.text_input('비밀번호',type='password')
btn=st.button('확인')

if btn:
        if id== '너진짜' and pw=='똑똑해':
                st.success('로그인성공')
        else:
            st.error('로그인실패')


st.title('너진똑')
st.write('시사 상식 퀴즈를 풀고  "너 진짜 똑똑하다" 라는 말 들어봅시다')

btn_d=st.button('문제 분야 선택')
if btn_d:
    st.switch_page('문제 분야 선택.py')

