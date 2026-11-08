import streamlit as st

st.title("Price Calculator")
price=st.number_input("Enter the product price")
discount=st.slider("Discount",0,100)
discounted_price=0
if st.button("Check Discounted Price"):
    discounted_price=price*(1-discount/100)
    st.success(discounted_price)
    st.table([["Before","After"],[price,round(discounted_price,2)]])