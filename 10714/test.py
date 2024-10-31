import streamlit as st
pages ={
    '카테고리명' : [
        st.Page('메인.py', title= '메인'),
       
],
'카테고리 명2':[
      st.Page('문제 분야 선택.py', title= '문제분야 선택'),]
      
,
'카테고리 명3':[
      st.Page('사회.py', title= '사회퀴즈'),
      st.Page('예술.py', title= '예술퀴즈'),st.Page('음악.py', title= '음악퀴즈')
      
]
}
pg= st.navigation(pages)
pg.run()


