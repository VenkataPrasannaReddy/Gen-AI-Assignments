import streamlit as st

st.title("Simple Sales Dashboard")
month=st.selectbox(label="months",options=["January","February","March","April"])
sales={"January":1200,"February":1500,"March":900,"April":2000}
st.metric(label=f"{month} sales",value=sales[month])
st.bar_chart({"month":sales.keys(),"sales":sales.values()},x="month",y="sales")
