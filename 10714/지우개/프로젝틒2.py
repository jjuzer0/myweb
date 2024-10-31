
import streamlit as st 

st.set_page_config(
page_title='걱정 지우개',page_icon='❤'
)

st.title('✏로그인✏')
id=st.text_input('아이디')
pw=st.text_input('비밀번호',type='password')
btn=st.button('확인')

if btn:
        if id== '걱정' and pw=='지우개':
                st.success('로그인성공')
        else:
            st.error('로그인실패')


st.title('걱정지우개')
st.write('걱정을 저장되지 않는 프로젝트인 이곳에 털어 놓고 날려보냅시다')

btn_d=st.button('걱정 털러가기')
if btn_d:
    st.switch_page('pages/걱정털기.py')

