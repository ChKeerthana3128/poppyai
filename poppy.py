import streamlit as st
import pandas as pd

# 🎨 Streamlit Page Config
st.set_page_config(page_title="India State Population Lookup", page_icon="🌏", layout="centered")

# 📂 Load Dataset (CSV file should be in the same directory)
df = pd.read_csv("india_population.csv")  # Ensure your file is named correctly

# 🎯 App Title
st.title("📊 India State Population Lookup 🌍")

# 🏙️ Select a State
state = st.selectbox("🔍 Select a State:", df["State"].unique())

# 📊 Fetch Population Data
selected_state = df[df["State"] == state].iloc[0]
total_population = selected_state["total_population"]
male_population = selected_state["population_male"]
female_population = selected_state["population_female"]

# 📢 Display Results
st.markdown(f"""
    ### 🌏 **State: {state}**
    - 🏠 **Total Population:** {total_population:,}
    - 👨 **Male Population:** {male_population:,} ({(male_population/total_population)*100:.2f}%)
    - 👩 **Female Population:** {female_population:,} ({(female_population/total_population)*100:.2f}%)
""")

# 🔍 **Predictive Insights**
st.subheader("🔮 Predictive Insights & Analysis")

# 📌 **Gender Ratio Analysis**
gender_ratio = male_population / female_population
st.markdown(f"📊 **Gender Ratio (Males per Female):** `{gender_ratio:.2f}`")
if gender_ratio > 1.05:
    st.warning("⚠️ **More males than females** – Possible migration trends or gender imbalance.")
elif gender_ratio < 0.95:
    st.warning("⚠️ **More females than males** – Interesting demographic trend!")
else:
    st.success("✅ **Balanced Gender Ratio** – Healthy demographic!")

# 📌 **Comparison with National Average**
avg_population = df["total_population"].mean()
if total_population > avg_population:
    st.info(f"📈 **{state} has a higher population than the national average!**")
else:
    st.info(f"📉 **{state} has a lower population than the national average!**")

# 📌 **Growth Potential**
growth_factor = (male_population + female_population) / total_population
if growth_factor > 0.95:
    st.success("🚀 **High Population Growth Potential!**")
elif growth_factor > 0.85:
    st.info("📊 **Moderate Growth Potential**")
else:
    st.warning("📉 **Low Growth Potential** – Aging population or migration effects.")

# 🎨 **Footer**
st.markdown("---")
st.markdown("💡 *Data-driven insights for better policy-making and planning!* 📊")

