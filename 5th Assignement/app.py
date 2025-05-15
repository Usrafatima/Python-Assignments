import streamlit as st
import json
import os
import time
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


DATA_FILE = "data.json"
LOGIN_PASSWORD = "admin123"  
MAX_ATTEMPTS = 3
LOCKOUT_TIME = 60  


if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "locked_out_until" not in st.session_state:
    st.session_state.locked_out_until = 0
if "authenticated" not in st.session_state:
    st.session_state.authenticated = True


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def generate_key(passkey, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt.encode(),
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(passkey.encode()))

def encrypt_data(text, passkey):
    salt = base64.urlsafe_b64encode(os.urandom(16)).decode()
    key = generate_key(passkey, salt)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(text.encode()).decode()
    return encrypted, salt

def decrypt_data(encrypted, passkey, salt):
    try:
        key = generate_key(passkey, salt)
        fernet = Fernet(key)
        return fernet.decrypt(encrypted.encode()).decode()
    except Exception:
        return None


def login_page():
    st.title("🔐 Login Required")
    password = st.text_input("Enter admin password to reauthorize:", type="password")
    if st.button("Login"):
        if password == LOGIN_PASSWORD:
            st.session_state.attempts = 0
            st.session_state.locked_out_until = 0
            st.session_state.authenticated = True
            st.success("Login successful.")
            st.rerun()
        else:
            st.error("Incorrect password.")


def insert_page(data):
    st.title("🔒 Store Your Data")
    username = st.text_input("Enter your username:")
    text = st.text_area("Enter text to store securely:")
    passkey = st.text_input("Enter a passkey:", type="password")

    if st.button("Encrypt and Save"):
        if username and text and passkey:
            encrypted_text, salt = encrypt_data(text, passkey)
            data[username] = {
                "encrypted_text": encrypted_text,
                "salt": salt
            }
            save_data(data)
            st.success("Data saved securely!")
        else:
            st.warning("All fields are required.")


def retrieve_page(data):
    st.title("🔓 Retrieve Your Data")

    if time.time() < st.session_state.locked_out_until:
        st.error(f"Too many failed attempts. Try again after {int(st.session_state.locked_out_until - time.time())} seconds.")
        return

    username = st.text_input("Enter your username:")
    passkey = st.text_input("Enter your passkey:", type="password")

    if st.button("Decrypt Data"):
        if username in data:
            decrypted = decrypt_data(data[username]["encrypted_text"], passkey, data[username]["salt"])
            if decrypted:
                st.success("Decrypted text:")
                st.code(decrypted)
                st.session_state.attempts = 0
            else:
                st.session_state.attempts += 1
                st.error(f"Incorrect passkey! Attempt {st.session_state.attempts}/{MAX_ATTEMPTS}")
                if st.session_state.attempts >= MAX_ATTEMPTS:
                    st.session_state.locked_out_until = time.time() + LOCKOUT_TIME
                    st.session_state.authenticated = False
                    st.rerun()
        else:
            st.warning("User not found.")


def home_page():
    st.title("🔐 Secure Data Storage App")
    option = st.selectbox("Select an option", ["Store Data", "Retrieve Data"])
    data = load_data()
    if option == "Store Data":
        insert_page(data)
    elif option == "Retrieve Data":
        retrieve_page(data)


def main():
    if not st.session_state.authenticated:
        login_page()
    else:
        home_page()

if __name__ == "__main__":
    main()
