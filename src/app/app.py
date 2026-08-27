import sys
import os
import streamlit as st

# Get the src folder path
src_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

# Add src to Python path
sys.path.insert(0, src_path)

from generation.generate_response import generate_response


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="RAG Sentiment Analysis",
    page_icon="💬",
    layout="centered"
)


# -----------------------------
# Application Title
# -----------------------------
st.title("💬 RAG Sentiment Analysis")
st.write(
    "Enter a product-related question and get relevant "
    "customer reviews with sentiment analysis."
)


# -----------------------------
# User Input
# -----------------------------
query = st.text_input(
    "Enter your query:",
    placeholder="Example: What do customers think about the product?"
)


# -----------------------------
# Number of Reviews
# -----------------------------
top_k = st.slider(
    "Number of reviews to retrieve:",
    min_value=1,
    max_value=5,
    value=3
)


# -----------------------------
# Generate Response
# -----------------------------
if st.button("🔍 Analyze"):

    if not query.strip():
        st.warning("Please enter a query.")

    else:
        with st.spinner("Searching reviews..."):

            response = generate_response(
                query,
                top_k
            )

        st.subheader("📊 Analysis")

        if isinstance(response, str):
            st.write(response)

        else:
            st.write(response)