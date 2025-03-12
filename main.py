import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/IMG_034018_0.png")

with col2:
    st.title("Glaudiston Santos de Oliveira Neto")
    content = """
        Hi, I'm Glaudiston! I'm a skilled JavaScript developer who has recently expanded my expertise in Python.
        My GitHub projects, such as To-do_Web-app and PythonTodoList, showcase my proficiency in building practical
        applications. I graduated in 2019 and have gained valuable experience as a freelancer. Now, I'm eager to
        leverage my knowledge and skills in a dynamic, large-scale company where I can make a significant impact.
    """
    st.info(content)

content2 = """
Bellow you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[2:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")