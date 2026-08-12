import streamlit as st

st.title("Super Simple Title")
st.header("This is a header")
st.subheader("Subheader")
st.markdown("This is _Markdown_.")
st.caption("small text")

print('run')
pressed = st.button("Press me")
print(pressed)
