import streamlit as st

st.title("Product Form")
with st.sidebar.form("product_form"):
    product_name=st.text_input(label="Product Name",placeholder="Please enter your text here...")
    category=st.selectbox(label="Category",options=["Fashion","Electronics","Beauty","Home Appliances","Kitchen Essential"])
    price=st.number_input(label="Price",min_value=0.0,step=1000.0)
    if st.form_submit_button("Add Product"):
        st.success(f"{product_name} product added into {category} category")
