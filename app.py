from PIL import Image
import requests
from streamlit_lottie import st_lottie
import streamlit as st


st.set_page_config(page_title="My Webpage", page_icon=":mount_fuji:",  layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if(r.status_code != 200):
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# --------  Header --------
with st.container():
    st.subheader("Hey there :wave:")
    st.title("Simply, A person who wants to make a difference")
    st.write("I am here to share my knowledge about all the stuffs I had gone through such as books, games, anime, manga, etc.")


# -------- LOAD ASSETS --------
# lottie_coding = "https://lottie.host/d34ebac9-5d33-4430-8de9-da765dd4e228/EYVH0SdemY.json"
# lottie_coding = "https://lottie.host/126666ae-dfd6-4aa5-bb1c-89521d1d4615/sT9rPIBtj0.json"
lottie_coding = "https://lottie.host/94f323a1-3630-47fe-af39-6a30253b98a0/hpuNpXT5UY.json"
lottie_discord = "https://lottie.host/cfbe235e-1118-43e3-9f1e-bddc5bb921dd/jwNq6sQlpY.json"
lottie_insta = "https://lottie.host/9a8dff9f-e399-47a5-b13d-667f4d2c3b44/L7q6zN1N6m.json"
img_book = Image.open("images/CPP.png")
img_book2 = Image.open("images/DAuP.png")


# -------- What I Do --------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Whats the idea")
        st.write("##")
        st.write(
            """
            **Welcome to my website**, where I share my thoughts and experiences on 
            <span style='font-family: Comic Sans MS;'>books</span>, 
            <span style='font-family: Comic Sans MS;'>manga</span>, 
            <span style='font-family: Comic Sans MS;'>anime</span>, and other 
            <span style='font-family: Comic Sans MS;'>entertaining content</span>. On this 
            <span style='font-family: Georgia;'>homepage</span>, you'll find detailed descriptions of the books I've read, along with my personal perspective. If it's a 
            <span style='font-family: Verdana;'>programming</span> or learning-related book, I'll provide insights and tips on what to focus on. For more in-depth information on programming concepts, you can navigate to a separate [webpage](https://google.in) dedicated to that. 
            
            <span style='font-family: Courier New;'>Join me as I explore various genres and share my enthusiasm for captivating stories and valuable knowledge.</span>
            
            
            """,
            unsafe_allow_html=True
        )
        left_img, right_img = st.columns(2)
        with left_img:
            st_lottie(lottie_discord, height=100, key="Discord")
            st.markdown(
                "<p style='text-align: center;'><a href='https://discord.gg/g5pfP5X4F'>Join the Server</a></p>",
                unsafe_allow_html=True
            )
        with right_img:
            st_lottie(lottie_insta, height=98, key="Instagram")
            st.markdown(
                "<p style='text-align: center;'><a href='https://instagram.com/please_send_request21?igshid=MzNlNGNkZWQ4Mg=='>Connect on Insta</a></p>",
                unsafe_allow_html=True
            )
        
    with right_column:
        st_lottie(lottie_coding)
        

# ------ PROJECTS ------
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        # insert image
        st.image(img_book)
        # pass
    with text_column:
        st.subheader("CORE PYTHON PROGRAMMING")
        st.write(
            """
            "Core Python Programming" by Dr. R. Nageswara Rao is a comprehensive book that covers all essential aspects of Python. It starts with Python introduction and basics, covers functions, data structures, file handling, OOP, exception handling, multithreading, networking, database programming, and GUI programming. It equips readers with solid Python programming skills.
            """
        )
        st.markdown("[Check it out ](https://google.in)")

st.write("""‌  """)


with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_book2)
    with text_column:
        st.subheader("Data Analytics using Python")
        st.write(
            """
            "Data Analytics using Python" by Bharti Motwani is an insightful book that covers Python's role in data analytics. It explores data manipulation, visualization, machine learning, NLP, time series analysis, and big data analytics. With practical examples and exercises, it's a valuable resource for mastering data analytics using Python.
            """
        )
        st.write("[Take a detailed look for yourself!](https://google.in)")

#----- Contact -----
with st.container():
    st.write("---")
    st.header("Get in Touch With Me!")
    st.write("##")

    # Documnetation: https://formsubmit.co/  !!! Change Email Address !!!
    contact_form = """
    <form action="https://formsubmit.co/aashu21022002@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
