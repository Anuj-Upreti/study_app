# 📦 Importing Streamlit library
import streamlit as st

# 🛠️ App-wide settings: sets the page title and layout
st.set_page_config(page_title="Class 10 Study App", layout="wide")

# 🧱 Page title and messages
st.title("📚 Class 10 Study Buddy by Moksh Joshi")

st.write("Welcome! Let's study smart. Pick a subject from the sidebar to begin.")

# 🚧 Sidebar setup – will contain subject navigation
st.sidebar.title("📂 Subjects")

# 📋 List of subjects to choose from (you can add or remove as needed)
subjects = ["Science", "Social Science", "Mathematics", "English", "Hindi"]

# 🧭 Create a dropdown in the sidebar to select a subject
selected_subject = st.sidebar.selectbox("Choose a Subject", subjects)

# 💡 Placeholder for subject-specific content – we'll build this out later
st.subheader(f"📝 You selected: {selected_subject}")
st.info("More content coming soon for this subject!")

# 📌 You can later load question-answer sets based on `selected_subject`
