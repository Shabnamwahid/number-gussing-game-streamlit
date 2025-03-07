import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Guess the number", page_icon="🗳", layout="centered")

# Initialize session state for storing the random number
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 10)

if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

# Custom styling
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
        }
        .stApp {
            background: linear-gradient(135deg, #8EC5FC, #E0C3FC);
            padding: 20px;
            border-radius: 15px;
        }
        .stTextInput, .stNumberInput {
            background: #ffffff !important;
            border-radius: 10px;
        }
        .stButton>button {
        
             background: linear-gradient(135deg, #D8BFD8, #4B0082);
            color: black;
            font-weight: bold;
            padding: 10px;
            border-radius: 10px;
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #f8b195, #f67280);
           

            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)
# Game Header
st.markdown("<h1 style='text-align: center; color:#4B0082'> 🔮❓Guess the Number Game🎲</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color:#2C003E ;'>I have chosen a number between 1 and 10. Can you guess it?</h4>", unsafe_allow_html=True)

# User input
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)
# Check button
if st.button("Check Guess"):
    st.session_state.attempts += 1
    if user_guess < st.session_state.random_number:
        st.warning("❌ Too low! Try again. 🔽")
    elif user_guess > st.session_state.random_number:
        st.warning("❌ Too high! Try again. 🔼")
    else:
        st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts! 🎯")

# Reset button to restart the game
if st.button("🔄 Restart Game"):
    st.session_state.random_number = random.randint(1, 10)
    st.session_state.attempts = 0
    st.rerun()  # ✅ Updated from st.experimental_rerun()