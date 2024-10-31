import streamlit as st

st.title('🎵음악🎵')

# 퀴즈 데이터 (문제: [(선택지1, 정답 여부), (선택지2, 정답 여부), ...])
quiz_data = {
    1: ("비틀즈의 유명한 곡 'Hey Jude'는 누구의 작품인가요?", [
        ("존 레논", False),
        ("폴 매카트니", True),
        ("조지 해리슨", False),
        ("링고 스타", False)
    ]),
    2: ("클래식 작곡가 중 '사계'를 작곡한 사람은 누구인가요?", [
        ("바흐", False),
        ("베토벤", False),
        ("비발디", True),
        ("모차르트", False)
    ]),
    3: ("'Thriller' 앨범을 발표한 아티스트는 누구인가요?", [
        ("프린스", False),
        ("마이클 잭슨", True),
        ("엘튼 존", False),
        ("비욘세", False)
    ]),
    4: ("'Rolling in the Deep'의 가수는 누구인가요?", [
        ("아델", True),
        ("테일러 스위프트", False),
        ("비욘세", False),
        ("켈리 클락슨", False)
    ]),
    5: ("고전 음악의 대표적인 형식 중 하나인 '소나타'는 몇 악장으로 구성되나요?", [
        ("1악장", False),
        ("2악장", False),
        ("3악장", False),
        ("3~4악장", True)
    ]),
    6: ("'Bohemian Rhapsody'는 어떤 밴드의 곡인가요?", [
        ("레드 제플린", False),
        ("퀸", True),
        ("비틀즈", False),
        ("더 도어스", False)
    ]),
    7: ("오페라 '카르멘'의 작곡가는 누구인가요?", [
        ("푸치니", False),
        ("베르디", False),
        ("비제", True),
        ("스트라빈스키", False)
    ]),
    8: ("'Shape of You'의 가수는 누구인가요?", [
        ("에드 시런", True),
        ("샘 스미스", False),
        ("브루노 마스", False),
        ("저스틴 비버", False)
    ]),
    9: ("'Imagine'의 주제는 무엇인가요?", [
        ("전쟁", False),
        ("평화", True),
        ("사랑", False),
        ("자유", False)
    ]),
    10: ("피아노 협주곡 21번의 작곡가는 누구인가요?", [
        ("쇼팽", False),
        ("모차르트", True),
        ("베토벤", False),
        ("리스트", False)
    ]),
    11: ("록 음악의 왕으로 알려진 아티스트는 누구인가요?", [
        ("엘비스 프레슬리", True),
        ("비틀즈", False),
        ("밥 딜런", False),
        ("퀸", False)
    ]),
    12: ("대중 음악의 최초의 팝스타로 알려진 아티스트는 누구인가요?", [
        ("비틀즈", False),
        ("프랭크 시나트라", True),
        ("마이클 잭슨", False),
        ("엘튼 존", False)
    ]),
    13: ("'Nessun Dorma'로 유명한 오페라의 주인공은 누구인가요?", [
        ("라이트", False),
        ("푸치니", True),
        ("바그너", False),
        ("베르디", False)
    ]),
    14: ("영국의 유명한 밴드로 'Stairway to Heaven'으로 알려진 밴드는?", [
        ("비틀즈", False),
        ("레드 제플린", True),
        ("롤링 스톤스", False),
        ("퀸", False)
    ]),
    15: ("'Someone Like You'의 가수는 누구인가요?", [
        ("아델", True),
        ("테일러 스위프트", False),
        ("비욘세", False),
        ("레이디 가가", False)
    ]),
    16: ("'Clair de Lune'의 작곡가는 누구인가요?", [
        ("드뷔시", True),
        ("리스트", False),
        ("쇼팽", False),
        ("모차르트", False)
    ]),
    17: ("'La Traviata'의 주제는 무엇인가요?", [
        ("사랑과 희생", True),
        ("전쟁", False),
        ("정치", False),
        ("자유", False)
    ]),
    18: ("힙합의 아버지로 알려진 아티스트는 누구인가요?", [
        ("투팍", False),
        ("노토리어스 B.I.G.", False),
        ("DJ Kool Herc", True),
        ("제이지", False)
    ]),
    19: ("'Gangnam Style'의 아티스트는 누구인가요?", [
        ("싸이", True),
        ("비", False),
        ("장범준", False),
        ("김범수", False)
    ])
}

# 앱 제목
st.title("고등학교 3학년 음악 퀴즈")

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