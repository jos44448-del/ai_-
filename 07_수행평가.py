import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="국가별 MBTI 비율 시각화", layout="wide")

# -------------------------
# 샘플 MBTI 데이터 (원하면 실제 데이터로 교체 가능)
# -------------------------
data = {
    "Country": ["Korea", "Korea", "Korea", "Korea",
                "USA", "USA", "USA", "USA",
                "Japan", "Japan", "Japan", "Japan"],
    "MBTI": ["INTJ", "ENFP", "ISTJ", "ESFP"] * 3,
    "Percent": [13, 22, 17, 10, 15, 18, 20, 12, 14, 16, 23, 9]
}

df = pd.DataFrame(data)

st.title("🌍 국가별 MBTI 비율 시각화 (Plotly)")

# -------------------------
# 국가 선택
# -------------------------
country_list = df["Country"].unique()
selected_country = st.selectbox("국가를 선택하세요:", country_list)

filtered = df[df["Country"] == selected_country].sort_values("Percent", ascending=False)

# -------------------------
# 색상 지정: 1등 빨간색, 나머지 점점 흐려지는 빨강 계열
# -------------------------
max_value = filtered["Percent"].max()

colors = ["red" if p == max_value else f"rgba(255,100,100,{0.2 + (p/max_value)*0.6})"
          for p in filtered["Percent"]]

# -------------------------
# Plotly 그래프 생성
# -------------------------
fig = px.bar(
    filtered,
    x="MBTI",
    y="Percent",
    text="Percent",
)

fig.update_traces(marker_color=colors, textposition="outside")
fig.update_layout(
    title=f"{selected_country} MBTI 비율",
    yaxis_title="비율 (%)",
    xaxis_title="MBTI",
    template="plotly_white",
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("#### 📌 설명")
st.write("""
- 국가를 선택하면 해당 국가의 MBTI 비율이 막대 그래프로 표시됩니다.
- 1등 MBTI 유형은 **빨간색**, 나머지는 **레드 계열의 부드러운 그라데이션**으로 표시됩니다.
- Plotly 기반이라 **줌 / 휠 확대 / 호버 정보** 등 인터랙션이 가능합니다.
""")
