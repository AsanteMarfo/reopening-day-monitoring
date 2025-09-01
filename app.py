
import streamlit as st
import streamlit.components.v1 as components

st.title("My Power BI Dashboard")
powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=ad7250f2-9da9-4090-a07a-fbc873aca868&autoAuth=true&ctid=95f31300-13cc-44d5-93da-e2a04daacd7d"

components.html(f"<iframe title="Reopening Day" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=ad7250f2-9da9-4090-a07a-fbc873aca868&autoAuth=true&ctid=95f31300-13cc-44d5-93da-e2a04daacd7d" frameborder="0" allowFullScreen="true"></iframe>