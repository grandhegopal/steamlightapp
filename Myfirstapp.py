import streamlit as st
import pandas as pd

st.write("My first app Hello *world!*")
df =  pd.read_excel("GOPAL3073SLG_New.xlsx")
st.line_chart(df.head())
