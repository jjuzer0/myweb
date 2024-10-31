import streamlit as st

st.title('🎨예술🎨')


# 퀴즈 데이터 (문제: [(선택지1, 정답 여부), (선택지2, 정답 여부), ...])
quiz_data = {
    1: ("모나리자의 작가는 누구인가요?", [
        ("레오나르도 다빈치", True),
        ("미켈란젤로", False),
        ("반 고흐", False),
        ("피카소", False)
    ]),
    2: ("'별이 빛나는 밤에'의 화가는 누구인가요?", [
        ("클로드 모네", False),
        ("빈센트 반 고흐", True),
        ("파블로 피카소", False),
        ("살바도르 달리", False)
    ]),
    3: ("르네상스 시대에 가장 유명한 건축가는 누구인가요?", [
        ("안토니 가우디", False),
        ("미켈란젤로", True),
        ("프랭크 로이드 라이트", False),
        ("루이 칸", False)
    ]),
    4: ("영국의 대표적인 화가는 누구인가요?", [
        ("윌리엄 터너", True),
        ("제임스 워홀", False),
        ("에드워드 호퍼", False),
        ("피터 폴 루벤스", False)
    ]),
    5: ("현대 미술의 대표적인 작가 중 한 명인 '캔디맨'의 본명은 무엇인가요?", [
        ("로이 리히텐슈타인", False),
        ("제프 쿤스", False),
        ("바스키아", True),
        ("데미안 허스트", False)
    ]),
    6: ("'여인의 초상'으로 유명한 화가는 누구인가요?", [
        ("고흐", False),
        ("그리쿠", False),
        ("르누아르", True),
        ("모네", False)
    ]),
    7: ("고대 그리스의 조각가로, '미소의 비너스'를 만든 사람은 누구인가요?", [
        ("피디아스", True),
        ("프락시텔레스", False),
        ("폴리클레이토스", False),
        ("로댕", False)
    ]),
    8: ("인상파의 창시자로 알려진 화가는 누구인가요?", [
        ("모네", True),
        ("세잔", False),
        ("시스리", False),
        ("드가", False)
    ]),
    9: ("'도시의 밤'으로 유명한 화가는 누구인가요?", [
        ("에드워드 호퍼", True),
        ("바스키아", False),
        ("잭슨 폴락", False),
        ("클로드 모네", False)
    ]),
    10: ("'최후의 만찬'은 누구의 작품인가요?", [
        ("레오나르도 다빈치", True),
        ("미켈란젤로", False),
        ("보티첼리", False),
        ("프라 안젤리코", False)
    ]),
    11: ("이탈리아의 고대 로마 건축물 중 가장 유명한 것은 무엇인가요?", [
        ("콜로세움", True),
        ("판테온", False),
        ("트라야누스 기둥", False),
        ("로마 포럼", False)
    ]),
    12: ("모더니즘 미술의 대표적인 작가는 누구인가요?", [
        ("파블로 피카소", True),
        ("빈센트 반 고흐", False),
        ("클로드 모네", False),
        ("살바도르 달리", False)
    ]),
    13: ("'사랑의 정원'으로 알려진 작품을 만든 화가는 누구인가요?", [
        ("클로드 모네", True),
        ("고흐", False),
        ("세잔", False),
        ("르누아르", False)
    ]),
    14: ("'별과 달의 길'이라는 이름으로 유명한 화가는 누구인가요?", [
        ("빈센트 반 고흐", True),
        ("카미유 피사로", False),
        ("에드가 드가", False),
        ("조르주 쇠라", False)
    ]),
    15: ("프랑스의 유명한 화가로, '여름'이라는 작품으로 잘 알려진 사람은 누구인가요?", [
        ("앙리 마티스", True),
        ("피카소", False),
        ("클로드 모네", False),
        ("조르주 쇠라", False)
    ]),
    16: ("'신부의 자살'로 유명한 작가는 누구인가요?", [
        ("마르셀 뒤샹", True),
        ("미켈란젤로", False),
        ("파블로 피카소", False),
        ("에드가 드가", False)
    ]),
    17: ("영국의 대표적인 화가로, '블루 레이디'로 잘 알려진 사람은 누구인가요?", [
        ("조지 스튜어트", True),
        ("윌리엄 터너", False),
        ("지오바니 벨리니", False),
        ("벤자민 웨스트", False)
    ]),
    18: ("'마담 보바리'로 유명한 화가는 누구인가요?", [
        ("에드가 드가", True),
        ("세잔", False),
        ("고흐", False),
        ("모네", False)
    ]),
    19: ("이탈리아의 대표적인 바르크 화가로 알려진 사람은 누구인가요?", [
        ("카라바조", True),
        ("바르톨로메오 바르베리니", False),
        ("안토니오 캄피", False),
        ("프란체스코 할리", False)
    ])
}

# 앱 제목
st.title("고등학교 3학년 예술 퀴즈")

# 세션 상태 초기화
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# 퀴즈 진행
for number, (question, options) in quiz_data.items():
    st.write(f"{number}. {question}")
    user_answer = st.radio("선택하세요:", [opt[0] for opt in options], key=question)
    
    # 사용자 답안 저장
    st.session_state.answers[number] = user_answer

# 정답 확인 버튼
if st.button("정답 확인"):
    score = 0
    wrong_answers = []

    for number, (question, options) in quiz_data.items():
        user_answer = st.session_state.answers[number]
        correct_answer = next(opt[0] for opt in options if opt[1])
        if user_answer == correct_answer:
            score += 1
        else:
            wrong_answers.append(number)

    # 점수 및 틀린 문제 표시
    st.write(f"당신의 점수는 {score}/{len(quiz_data)}입니다.")
    if wrong_answers:
        st.error("틀린 문제 번호: " + ", ".join(map(str, wrong_answers)))
    else:
        st.success("모든 문제를 맞췄습니다!")
        st.success("수고했습니다! 다른 분야의 문제도 풀어보세요")