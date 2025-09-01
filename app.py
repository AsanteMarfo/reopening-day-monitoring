
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Re-Opening Day Monitoring",
    layout="centered", # Can be "wide" or "centered"
    initial_sidebar_state="expanded"
)

powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=ad7250f2-9da9-4090-a07a-fbc873aca868&autoAuth=true&ctid=95f31300-13cc-44d5-93da-e2a04daacd7d&chromeless=1&navContentPaneEnabled=false"

st.header("Monitoring Dashboard")
st.write("""
        Welcome to the **Re-Opening Monitoring Dashbord** application!
        This Dashboard helps you monitor live data submission from field officers and School Improvement Officers.
    """)
# Replace with your actual embed URL
powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=ad7250f2-9da9-4090-a07a-fbc873aca868&autoAuth=true&ctid=95f31300-13cc-44d5-93da-e2a04daacd7d&chromeless=1&navContentPaneEnabled=false"

# Embed the dashboard
components.iframe(src=powerbi_url, width=1000, height=700, scrolling=True)

#st.image("https://app.powerbi.com/reportEmbed?reportId=ad7250f2-9da9-4090-a07a-fbc873aca868&autoAuth=true&ctid=95f31300-13cc-44d5-93da-e2a04daacd7d", caption="Re-Opening Day Monitoring", use_container_width=True)
