import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('Attrition data.csv')

st.set_page_config(page_title='Employee Analytics Dashboard', layout='wide')
st.title(" 👤📈 EMPLOYEE CAREER PROGRESSION")

# Display analyses in rows
row1_1, row1_2 = st.columns(2)
row2_1, row2_2 = st.columns(2)
row3_1, row3_2 = st.columns(2)
row4_1, row4_2 = st.columns(2)

# Analysis 1
with row1_1:
    st.subheader("Correlation Analysis")
    correlation_matrix = df.corr()
    st.write(correlation_matrix.style.background_gradient(cmap='coolwarm'))

with row1_2:
    st.subheader("Attrition Analysis")
    attrition_counts = df["Attrition"].value_counts()
    st.bar_chart(attrition_counts)

# Analysis 2
with row2_1:
    st.subheader("Job Satisfaction and Performance Analysis")
    fig_satisfaction_performance = px.scatter(df, x="JobSatisfaction", y="PerformanceRating", color="Attrition",
                                              labels={"JobSatisfaction": "Job Satisfaction", "PerformanceRating": "Performance Rating"},
                                              title="Job Satisfaction vs. Performance Rating")
    st.plotly_chart(fig_satisfaction_performance)

with row2_2:
    st.subheader("Demographic Analysis")
    fig_demographic = px.histogram(df, x="Gender", color="Attrition", title="Gender Distribution by Attrition")
    st.plotly_chart(fig_demographic)

# Analysis 3
with row3_1:
    st.subheader("Career Development Analysis")
    fig_career_dev = px.scatter(df, x="YearsAtCompany", y="YearsSinceLastPromotion", color="Attrition",
                                labels={"YearsAtCompany": "Years at Company", "YearsSinceLastPromotion": "Years Since Last Promotion"})
    st.plotly_chart(fig_career_dev)

with row3_2:
    st.subheader("Salary and Job Level Analysis")
    fig_salary_job_level = px.box(df, x="JobLevel", y="MonthlyIncome", color="Attrition",
                                  labels={"JobLevel": "Job Level", "MonthlyIncome": "Monthly Income"})
    st.plotly_chart(fig_salary_job_level)

# Analysis 4
with row4_1:
    st.subheader("Training and Development")
    fig_training_dev = px.bar(df, x="TrainingTimesLastYear", color="Attrition",
                              labels={"TrainingTimesLastYear": "Training Times Last Year"})
    st.plotly_chart(fig_training_dev)

with row4_2:
    st.subheader("Work-Life Balance")
    fig_work_life_balance = px.bar(df, x="WorkLifeBalance", color="Attrition",
                                   labels={"WorkLifeBalance": "Work-Life Balance"})
    st.plotly_chart(fig_work_life_balance)



