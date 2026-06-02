import streamlit as st
import pandas as pd
from sqlalchemy import create_engine 

st.set_page_config(
    page_title="News Analytics Dashboard",
    layout="wide"
)

DATABASE_URL = "postgresql://postgres:saniyabijoy@database-1.cvkg622c6us1.ap-southeast-2.rds.amazonaws.com:5432/news_db"

engine = create_engine(DATABASE_URL)

df = pd.read_sql("SELECT * FROM news_data ORDER BY created_at DESC", engine)


st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main-title {
    font-size: 42px;
    font-weight: bold;
    color: white;
    text-align: center;
    margin-bottom: 30px;
}
.sidebar-text {
    font-size: 15px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)
