import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/PrincessAngieFeet.jpeg")

with col2:
    st.title("Princess Angie Feet")
    content = """
    Hi I'm Glaudiston! I am a JavaScript, and recently a Python programmer. I graduated in 2019, have worked only as
    freelancer, but I'm ready to start working at a huge company where I can show up my knowledge and skills. 
    """
    st.info(content)

content2 = """
Bellow you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content2)

col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df.iterrows():
        st.header(row["title"])

with col4:
    for index, row in df.iterrows():
        st.header(row["title"])