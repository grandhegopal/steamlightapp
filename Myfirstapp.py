import streamlit as st
import pandas as pd

st.write("My first app Hello *world!*")
df = pd.read_csv("https://docs.google.com/spreadsheets/d/1CEr_xj8NYEhyw43hjOhPuzh0b7lF009e7OgWNL6P6MU/edit?usp=drive_link")
st.line_chart(df)
