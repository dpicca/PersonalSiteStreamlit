import streamlit as st
from streamlit_option_menu import option_menu
from tools import add_bg_color, read_txt_file

st.set_page_config('My Personal Website', ':house:', layout='wide', initial_sidebar_state='auto')

#defining a function to read a txt file and return the content

add_bg_color() #add the background image

def home():
    st.title("Welcome to my personal website!")
    # put a vertical space
    st.markdown("")
    st.markdown("")
    st.markdown("")
    # put the image and the text side by side.

    col1, col2 = st.columns(2)
    col1.image('./assets/d.picca_-1.jpg', width=300)

    col2.markdown(read_txt_file('./texts/about_me.md'),unsafe_allow_html=True)

def curriculum():
    st.title("Curriculum")
    # put a vertical space
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown(read_txt_file('./texts/cv.md'), unsafe_allow_html=True)

def publications():
    st.title("Publications")
    # put a vertical space
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown(read_txt_file('./texts/publications.md'), unsafe_allow_html=True)

def projects():
    st.title("Projects")
    # put a vertical space
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown(read_txt_file('./texts/projects.md'), unsafe_allow_html=True)

def activities():
    st.title("Activities")
    # put a vertical space
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown(read_txt_file('./texts/activities.md'),unsafe_allow_html=True)

def teaching():
    st.title("Teaching")
    # put a vertical space
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown(read_txt_file('./texts/teaching.md'))


def main():
    with st.sidebar:
        choose = option_menu("Menu", ["Home", "Curriculum", "Publications","Projects", "Activities", "Teaching"],
                             icons=['house', 'envelope', 'book', 'hammer','activity', 'person video3'],
                             menu_icon="app-indicator", default_index=0,
                             styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
        )


    if choose == "Home":
        home()
    elif choose == "Curriculum":
        curriculum()
    elif choose == "Publications":
        publications()
    elif choose == "Projects":
        projects()
    elif choose == "Activities":
        activities()
    elif choose == "Teaching":
        teaching()



if __name__ == "__main__":
    main()