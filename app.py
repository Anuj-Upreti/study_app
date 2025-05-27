# 📦 Importing Streamlit and Lottie libraries
import streamlit as st
from streamlit_lottie import st_lottie
import requests

# 🛠️ App-wide settings
st.set_page_config(page_title="Class 10 Study App", layout="wide")

# 📘 Function to load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# 🧱 Page title and messages
st.title("📚 Class 10 Study Buddy by Moksh Joshi")
st.write("Welcome! Let's study smart. Pick a subject from the sidebar to begin.")

# 🚧 Sidebar for navigation
st.sidebar.title("📂 Subjects")
subjects = ["Science", "Social Science", "Mathematics", "English", "Hindi"]
selected_subject = st.sidebar.selectbox("Choose a Subject", subjects)

# ✨ Lottie animation URLs mapped to each subject
subject_animations = {
    "Science": "https://assets7.lottiefiles.com/packages/lf20_j1adxtyb.json",
    "Mathematics": "https://assets1.lottiefiles.com/packages/lf20_vfcnwlo4.json",
    "English": "https://assets1.lottiefiles.com/packages/lf20_twijbubv.json",
    "Social Science": "https://assets1.lottiefiles.com/packages/lf20_t24tpvcu.json",
    "Hindi": "https://assets1.lottiefiles.com/packages/lf20_lk80fpsm.json"
}

# 🎥 Display subject-specific animation and placeholder content
st.subheader(f"📝 You selected: {selected_subject}")

# Display animation if available
animation_url = subject_animations.get(selected_subject)
lottie_json = load_lottieurl(animation_url)
if lottie_json:
    st_lottie(lottie_json, height=250, key=selected_subject)

# 📌 Placeholder for content
st.info("More content coming soon for this subject!")
