import streamlit as st

slider= st.select_slider('반을 선택하시오',['1반','2반','3반','4반'])


과목=st.selectbox('과목을 선택하세요',['확률과 통계','미적분','기하'])
st.write('당신이 선택한 과목은'+과목+'입니다.')
st.write('다음중 프로그래밍에 대한 설명중 가장 적절한 것은?')
결과 =st.radio('보기',['python을 배운다','10주동안배운다','3번결석해도 괜찮다.','재미 없다.'])
btn=st.button('정답확인')
if btn:
     if 결과  == 'python을 배운다':
              st.success('정답')
              st.balloons()
     else:
            st.error('오답')
       

짜장면=st.checkbox('짜장면5000원')
짬뽕=st.checkbox('짬뽕6000원')
탕수육=st.checkbox('탕수육12000원')
가격=0
if 짜장면:
       st.write('짜장면을 선택하셨습니다..')
if 짬뽕:
       st.write('짬뽕을 선택하셨습니다..')

if 탕수육:
       st.write('탕수육을 선택하셨습니다..')

if 짬뽕:
       가격+=6000
elif 탕수육 :    가격+=5000
elif 짜장면 : 가격+=12000

st.write(str(가격)+'원 입니다.')


st.write('**정주영**님 안녕하세요')
st.header('🍕header')
st.subheader('subheader')
st.title('title')
st.write(':blue[함지]고등학교')
st.title('🍕로그인🍕')
id=st.text_input('아이디')
pw=st.text_input('비밀번호',type='password')
btn=st.button('확인')

if btn:
        if id== 'abc' and pw=='123':
                st.success('로그인성공')
        else:
            st.error('로그인실패')