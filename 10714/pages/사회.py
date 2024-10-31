import streamlit as st

st.title('📚사회📚')

# 퀴즈 데이터 (문제: [(선택지1, 정답 여부), (선택지2, 정답 여부), ...])
quiz_data = {
    1: ("대한민국의 헌법은 몇 차례 개정되었나요?", [
        ("1차", False),
        ("5차", False),
        ("9차", True),
        ("12차", False)
    ]),
    2: ("조선시대의 성리학을 대표하는 인물은 누구인가요?", [
        ("이이", True),
        ("정약용", False),
        ("세종대왕", False),
        ("홍대용", False)
    ]),
    3: ("대한민국의 대통령 직선제는 언제 도입되었나요?", [
        ("1987년", True),
        ("1992년", False),
        ("2000년", False),
        ("2002년", False)
    ]),
    4: ("한국전쟁이 발발한 해는 언제인가요?", [
        ("1945년", False),
        ("1950년", True),
        ("1953년", False),
        ("1960년", False)
    ]),
    5: ("우리나라의 법률이 헌법에 위반될 경우 어떻게 되는가요?", [
        ("법률은 무효가 된다.", True),
        ("법률은 그대로 유지된다.", False),
        ("법률이 재개정된다.", False),
        ("법률이 판결을 받는다.", False)
    ]),
    6: ("한국의 민주화 운동이 본격적으로 일어난 시기는 언제인가요?", [
        ("1960년대", False),
        ("1980년대", True),
        ("1990년대", False),
        ("2000년대", False)
    ]),
    7: ("대한민국의 첫 여성 대통령은 누구인가요?", [
        ("박근혜", True),
        ("이명박", False),
        ("노무현", False),
        ("김대중", False)
    ]),
    8: ("한일 간의 수교가 이루어진 해는 언제인가요?", [
        ("1965년", True),
        ("1972년", False),
        ("1980년", False),
        ("1992년", False)
    ]),
    9: ("대한민국의 수도는 어디인가요?", [
        ("서울", True),
        ("부산", False),
        ("대구", False),
        ("광주", False)
    ]),
    10: ("남북한 간의 정전협정은 언제 체결되었나요?", [
        ("1950년", False),
        ("1953년", True),
        ("1960년", False),
        ("1972년", False)
    ]),
    11: ("한국의 고대 국가 중 하나로, '삼국시대'에 속하는 국가는 무엇인가요?", [
        ("신라", True),
        ("고구려", True),
        ("백제", True),
        ("고려", False)
    ]),
    12: ("헌법재판소의 역할은 무엇인가요?", [
        ("법률 심판", True),
        ("대통령 선출", False),
        ("국회 의결", False),
        ("행정명령 발동", False)
    ]),
    13: ("제1공화국의 초대 대통령은 누구인가요?", [
        ("이승만", True),
        ("윤보선", False),
        ("박정희", False),
        ("김대중", False)
    ]),
    14: ("한국의 대표적인 비무장지대(DMZ) 지역은 어디인가요?", [
        ("한강", False),
        ("대동강", False),
        ("38선", True),
        ("소백산", False)
    ]),
    15: ("대한민국의 국기는 무엇인가요?", [
        ("태극기", True),
        ("성조기", False),
        ("일장기", False),
        ("유니온잭", False)
    ]),
    16: ("세계 제2차 대전이 끝난 해는 언제인가요?", [
        ("1945년", True),
        ("1946년", False),
        ("1950년", False),
        ("1953년", False)
    ]),
    17: ("대한민국의 민주화 선언은 언제 이루어졌나요?", [
        ("1987년", True),
        ("1992년", False),
        ("2000년", False),
        ("2005년", False)
    ]),
    18: ("우리나라의 경제개발 5개년 계획이 시작된 해는 언제인가요?", [
        ("1962년", True),
        ("1965년", False),
        ("1970년", False),
        ("1975년", False)
    ]),
    19: ("인권 선언이 최초로 이루어진 해는 언제인가요?", [
        ("1948년", True),
        ("1950년", False),
        ("1960년", False),
        ("1975년", False)
    ])
}

# 앱 제목
st.title("고등학교 3학년 사회 퀴즈")

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