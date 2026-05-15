import streamlit as st

st.set_page_config(
    page_title="나의 소개 페이지",
    page_icon="👋",
    layout="centered",
)

st.title("👋 안녕하세요! 나의 소개 페이지입니다")
st.subheader("간단한 자기소개와 주요 정보를 이곳에 정리해보세요")

st.markdown(
    "### 🔎 소개\n"
    "안녕하세요! 저는 왕효원이고, 교사입니다.\n"
)

st.markdown(
    "- **관심 분야:** [관심 분야나 전공 입력]\n"
    "- **현재 하는 일:** [현재 업무나 프로젝트]\n"
    "- **주요 기술:** [기술 1], [기술 2], [기술 3]\n"
)

st.markdown("---")

st.header("✨ 나에 대해 더 알아보기")
st.markdown(
    "#### 📚 배경\n"
    "여기에 간단하게 학력, 경력 또는 관심사를 작성하세요.\n\n"
    "#### 🛠️ 기술 스택\n"
    "- [기술 또는 도구 1]\n"
    "- [기술 또는 도구 2]\n"
    "- [기술 또는 도구 3]\n"
)

st.markdown("---")

st.header("📬 연락 정보")
st.markdown(
    "- 이메일: [your.email@example.com]\n"
    "- 깃허브: [github.com/yourname]\n"
    "- 링크드인: [linkedin.com/in/yourname]\n"
)

st.info("이 페이지는 템플릿입니다. 내용을 자유롭게 수정해 나만의 소개 페이지로 만들어보세요.")
