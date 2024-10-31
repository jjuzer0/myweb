import streamlit as st

st.title("시사상식 퀴즈")

pages ={
    '카테고리명' : [
        st.Page('문제 분야 선택.py', title= 'A페이지'),
        st.Page('b.py', title= 'b페이지')
],
'카테고리 명2':[
      st.Page('c.py', title= 'a페이지'),
      st.Page('d.py', title= 'b페이지')
]
}
pg= st.navigation(pages)
pg.run()