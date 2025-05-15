import json
import streamlit as st

# File to store book data
STORAGE_FILE = "books_data.json"

# Function to load books from JSON
def load_books():
    try:
        with open(STORAGE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save books to JSON
def save_books(books):
    with open(STORAGE_FILE, "w") as file:
        json.dump(books, file, indent=4)

# Initialize book list
if "books" not in st.session_state:
    st.session_state.books = load_books()

# Page Config
st.set_page_config(page_title="Book Collection", layout="wide")

# Custom Header Navigation
st.markdown(
    """
    <style>
        .header {
            background-color: #2E86C1;
            padding: 10px;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .header h1 {
            color: white;
            font-size: 24px;
        }
        .menu {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 10px;
        }
        .menu button {
            background-color: white;
            color: #2E86C1;
            border: 2px solid #2E86C1;
            border-radius: 8px;
            padding: 8px 16px;
            font-size: 16px;
            cursor: pointer;
            transition: 0.3s;
        }
        .menu button:hover {
            background-color: #2E86C1;
            color: white;
        }
    </style>
    <div class='header'>
        <h1>📚 Book Collection Manager</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Navigation Buttons
col1, col2, col3, col4 = st.columns(4)
if col1.button("📖 View Books"):
    st.session_state.page = "View Books"
if col2.button("➕ Add Book"):
    st.session_state.page = "Add Book"
if col3.button("🔍 Search Books"):
    st.session_state.page = "Search Books"
if col4.button("🗑️ Delete Book"):
    st.session_state.page = "Delete Book"

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "View Books"

# Page Rendering
if st.session_state.page == "View Books":
    st.subheader("📖 Your Book Collection")
    if not st.session_state.books:
        st.warning("Your book collection is empty!")
    else:
        for book in st.session_state.books:
            st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']}")
            st.write(f"📖 Read: {'✅' if book['read'] else '❌'}")
            st.write("---")

elif st.session_state.page == "Add Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.text_input("Publication Year")
    genre = st.text_input("Genre")
    read = st.checkbox("Have you read this book?")

    if st.button("Add Book"):
        if title and author and year and genre:
            st.session_state.books.append({"title": title, "author": author, "year": year, "genre": genre, "read": read})
            save_books(st.session_state.books)
            st.success("Book added successfully!")
            st.session_state.page = "View Books"
            st.rerun()
        else:
            st.error("Please fill in all fields.")

elif st.session_state.page == "Search Books":
    st.subheader("🔍 Search for a Book")
    search_query = st.text_input("Enter title or author name")

    if search_query:
        results = [book for book in st.session_state.books if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower()]
        if results:
            for book in results:
                st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']}")
                st.write(f"📖 Read: {'✅' if book['read'] else '❌'}")
                st.write("---")
        else:
            st.warning("No matching books found.")

elif st.session_state.page == "Delete Book":
    st.subheader("🗑️ Delete a Book")
    book_titles = [book["title"] for book in st.session_state.books]
    if book_titles:
        book_to_delete = st.selectbox("Select a book to delete:", book_titles)
        if st.button("Delete Book"):
            st.session_state.books = [book for book in st.session_state.books if book["title"] != book_to_delete]
            save_books(st.session_state.books)
            st.success(f"Deleted '{book_to_delete}' successfully!")
            st.session_state.page = "View Books"
            st.rerun()
    else:
        st.warning("No books available to delete.")
