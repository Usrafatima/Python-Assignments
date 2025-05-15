import streamlit as st
import re
import random

st.set_page_config(page_title="Password Strength", page_icon="🔐")

st.title("🔐 Password Strength Checker")
st.markdown("### Welcome to the ultimate password strength checker! ")

password = st.text_input("Enter your password", type="password")

feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain both upper and lower case letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number (0-9).")

    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character (!@#$%^&*).")

    # Progress Bar
    st.progress(score / 4)

    # Display feedback
    if score == 4:
        st.success("Your password is strong!  ")
    elif score == 3:
        st.warning("Your password is medium strength. Try making it stronger.")
    else:
        st.error("Your password is weak. Please improve it.")

    if feedback:
        st.markdown("###  Improvement Suggestions:")
        for tip in feedback:
            st.write(f"- {tip}")

    # Generate a strong password
    def generate_password():
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
        return "".join(random.sample(chars, 12))

    if score < 4:
        st.markdown("###  Try a Stronger Password:")
        st.code(generate_password(), language="text")

else:
    st.info("Please enter your password to get started.")
st.caption("###  By Yusra Fatima")


