import streamlit as st

st.title("Product Form")
product=st.sidebar.text_input(label="Enter the product name",placeholder="Please enter your text here...")
category=st.sidebar.selectbox(label="Category",options=["Fashion","Electronics","Beauty","Home Appliances","Kitchen Essential"])
if st.sidebar.button("Add Product"):
    st.sidebar.success(f"{product} product added into {category} category")
