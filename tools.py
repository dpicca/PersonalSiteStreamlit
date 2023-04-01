import streamlit as st

def read_txt_file(file_name):
    with open(file_name) as f:
        return f.read()

#defining a function to add a background image
def add_bg_color():
    st.markdown(
         f"""
         <style>
         .stApp {{
background-image: linear-gradient(to right top, #c0e2cb, #a8cfc4, #97bcbb, #8aa8ae, #81949e, #83929f, #85909f, #888e9e, #989db2, #aaadc5, #bcbcd9, #d0cced);         </style>
         """,
         unsafe_allow_html=True
     )

def custom_markdown(font_family = 'sans-serif' , color = 'white', font_size = 10, text = ''):
    new_text = f'<p style="font-family:{font_family}; color:{color}; font-size: {font_size}px;">{text}</p>'
    return st.markdown(new_text, unsafe_allow_html=True)
