from dotenv import load_dotenv
import streamlit as st

load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

st.write("""
# AI 모기훈💕
""")

st.write("안녕! 나는 너의 남자친구인 ENTP 모기훈 AI야 편하게 얘기해줘! 😊")

# 메시지 입력창 (위쪽 고정)
user_input = st.text_input("메시지를 입력해주세요:", key="user_input")

col1, col2 = st.columns([1, 1])
with col1:
    send_button = st.button("메시지 보내기")
with col2:
    clear_button = st.button("대화 초기화")

# 구분선
st.divider()

# 메시지 처리
if send_button:
    if user_input:
        # 사용자 메시지 추가
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        with st.spinner("답장을 쓰고 있어요... 💭"):
            # AI 이성친구 프롬프트
            prompt = f"""
            너는 ENTP 30대 남자친구인 노기훈이야.
            여자친구는 ISTJ고 99년이고 직업은 간호사야.
            여자친구는 너를 어필보이 모기훈이라고 불러.
            친근하고 애정어린 대화를 나눠줘.
            상대방을 배려하는 말투로 대답해줘.
            너무 길지 않게 자연스럽게 대화해줘.
            
            ISTJ 99년생 간호사의 메시지: {user_input}
            """
            res = llm.invoke(prompt)
            
            # AI 응답 추가
            st.session_state.messages.append({"role": "assistant", "content": res.content})
        
        # 페이지 새로고침
        st.rerun()

# 대화 초기화 처리
if clear_button:
    st.session_state.messages = []
    st.rerun()

# 채팅 히스토리 표시 (아래쪽)
if st.session_state.messages:
    # st.write("### 💬 채팅 기록")
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.write(f"**나:** {message['content']}")
        else:
            st.write(f"**모기훈 AI:** {message['content']}")