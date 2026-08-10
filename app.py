import streamlit as st

st.title("My First Streamlit App")
st.write("Hello! My Streamlit app is successfully deployed!")

name = st.text_input("Enter your name:")
if name:
  st.success(f"Hello, {name}!")
