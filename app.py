import streamlit as st
import pandas as pd

st.set_page_config(page_title="SAM LEGEND", page_icon="🎮", layout="wide")

st.markdown("<h1 style='color:#00ff88;text-align:center'>🎮 MERCIFUL×SAM ANALYTICS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>Level 70 | 3771 Matches | 5 Yrs Exp | Elite Collector 2 | 3x X-Suit</p>", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
c1.metric("Matches", "21", "Season")
c2.metric("Wins", "3", "14%")
c3.metric("F/D Ratio", "3.33")
c4.metric("Avg Damage", "682.4")

st.divider()

col1, col2 = st.columns(2)
with col1:
    st.subheader("🏆 Best Match")
    st.success("Rank #3 - 12 Finishes - 2133 Damage - SSS Rating")
    st.write("Rank #1 Chicken Dinner - Consistent Top 10")
with col2:
    st.subheader("🤖 AI Coach Insight")
    st.info("Survival 71.4% Top 10 (15/21). Your survival is elite! Final circle me thoda aggressive khelna hai. Potential to push F/D to 5+.")

st.subheader("📊 Season Graph")
df = pd.DataFrame({"Match": range(1,22), "Finishes": [2,1,4,0,3,12,1,2,5,0,3,1,2,4,2,1,0,3,2,6,1]})
st.line_chart(df, x="Match", y="Finishes")

st.markdown("---")
st.caption("Built by SAM LEGEND | BGMI Analytics SaaS v1.0")
