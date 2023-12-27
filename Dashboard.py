import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Load your CSV file
data = pd.read_csv("24-30_May_21.csv")

# Set the title and a brief description of your dashboard
st.title("Disease Survelliance System")
st.write("Welcome to the Disease Patients Dashboard. This dashboard shows the total number of patients with different diseases.")

# Display the data
st.subheader("Data Overview")
st.write(data)
disease_counts = data['Diseases']
disease_counts.columns = [ 'Total']

# Create and display a bar chart
st.subheader("Total Patients by Disease")
fig = px.bar(data,x='Total', y='Diseases', title='Total Patients by Disease')
st.plotly_chart(fig)
fig = px.line(data, x='Diseases', y='Total', title='Daily Trends in Patients')
st.plotly_chart(fig)
data.plot()
plt.show()