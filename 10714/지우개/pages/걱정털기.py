
import streamlit as st
import random

# 세션 상태를 사용하여 걱정 저장
if 'worries' not in st.session_state:
    st.session_state.worries = []

# 위로 메시지 목록
comfort_messages = [
    "괜찮아요, 모든 일이 잘 풀릴 거예요.",
    "당신은 혼자가 아니에요. 힘내세요!",
    "지금 힘든 시간을 보내고 있지만, 곧 나아질 거예요.",
    "걱정하지 마세요. 긍정적인 마음을 가지세요!",
    "하루하루 조금씩 나아질 거예요."
]

# 응원 메시지 목록
encouragement_messages = [
    "새로운 시작을 응원합니다!",
    "당신은 강합니다. 계속 나아가세요!",
    "오늘도 한 걸음 나아갔습니다. 잘하고 있어요!",
    "과거를 놓아주세요. 앞으로 나아갈 시간입니다!",
    "힘든 시간을 지나온 당신을 응원합니다!"
]

st.title("걱정 적기")

# 걱정 입력
worry = st.text_input("걱정을 적어주세요:")

# 걱정 추가 버튼
if st.button("추가"):
    if worry:
        st.session_state.worries.append(worry)
        st.success("걱정이 추가되었습니다.")
    else:
        st.warning("걱정을 입력해주세요.")

# 걱정 목록 표시
if st.session_state.worries:
    st.write("당신의 걱정 목록:")
    for idx, w in enumerate(st.session_state.worries):
        st.write(f"{idx + 1}. {w}")

# 모두 지우기 버튼
if st.button("모두 지우기"):
    st.session_state.worries.clear()  # 세션 비우기
    st.success("모든 걱정이 사라졌습니다.")
    # 위로 메시지 출력
    st.write(random.choice(comfort_messages))

# 세션 상태 확인
if not st.session_state.worries:
    st.write("현재 걱정이 없습니다.")
