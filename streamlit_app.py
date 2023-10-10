import streamlit as st
import pandas as pd

# Create an empty DataFrame to store the data
data = pd.DataFrame(columns=["Campaign Name", "Start Date", "End Date", "Budget", "Target Audience"])

# Streamlit app header
st.title("Marketing Data Collection App")

# Create a form for data input
st.subheader("Enter Campaign Details:")
campaign_name = st.text_input("Campaign Name")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")
budget = st.number_input("Budget ($)")
target_audience = st.text_input("Target Audience")

# Add data to the DataFrame when the user clicks the "Submit" button
if st.button("Submit"):
    data = data.append({"Campaign Name": campaign_name, "Start Date": start_date, "End Date": end_date,
                        "Budget": budget, "Target Audience": target_audience}, ignore_index=True)

# Display the collected data
st.subheader("Collected Data:")
st.write(data)

# Optionally, you can add data visualization and analysis here.
# For example, you can create charts using libraries like Matplotlib or Plotly.
