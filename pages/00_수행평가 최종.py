import streamlit as st
import pandas as pd
import plotly.graph_objects as go


st.set_page_config(page_title="MBTI 비율 시각화", layout="wide")
st.title("🌍 국가별 MBTI 비율 시각화")


data = {
"Korea": {
"ISTJ": 12, "ISFJ": 14, "INFJ": 3, "INTJ": 4,
"ISTP": 8, "ISFP": 9, "INFP": 7, "INTP": 6,
"ESTP": 5, "ESFP": 6, "ENFP": 10, "ENTP": 4,
"ESTJ": 4, "ESFJ": 5, "ENFJ": 3, "ENTJ": 4
},
"USA": {
"ISTJ": 11, "ISFJ": 12, "INFJ": 2, "INTJ": 5,
"ISTP": 7, "ISFP": 8, "INFP": 9, "INTP": 6,
"ESTP": 6, "ESFP": 7, "ENFP": 11, "ENTP": 5,
"ESTJ": 5, "ESFJ": 6, "ENFJ": 3, "ENTJ": 4
}
}


countries = list(data.keys())
selected_country = st.selectbox("국가를 선택하세요", countries)


df = pd.DataFrame(list(data[selected_country].items()), columns=["MBTI", "Ratio"])
df_sorted = df.sort_values(by="Ratio", ascending=False)


base_color = [255, 100, 100]
colors = []
for i in range(len(df_sorted)):
if i == 0:
colors.append("rgb(255,0,0)")
else:
factor = 0.7 + 0.3 * (i / len(df_sorted))
r = int(base_color[0] * factor)
g = int(base_color[1] * factor)
b = int(base_color[2] * factor)
colors.append(f"rgb({r},{g},{b})")


fig = go.Figure(
data=[go.Bar(x=df_sorted["MBTI"], y=df_sorted["Ratio"], marker_color=colors)]
)
fig.update_layout(
title=f"{selected_country} MBTI 비율",
xaxis_title="MBTI 유형",
yaxis_title="비율 (%)",
template="simple_white",
height=600
)


st.plotly_chart(fig, use_container_width=True)
