import streamlit as st

# Title of the Streamlit app
st.title('Simple Streamlit App')

# Text input field
name = st.text_input('Enter your name:')

# Number input field
age = st.number_input('Enter your age:', min_value=1, max_value=100)

# Button to display the name and age
if st.button('Submit'):
    st.write(f'Hello {name}, you are {age} years old!')

# Slider for rating
rating = st.slider('Rate this app', 1, 5)
st.write(f'You rated this app: {rating}/5')

# Sidebar
st.sidebar.title('Sidebar')
option = st.sidebar.selectbox('Select an option:', ('Option 1', 'Option 2', 'Option 3'))

st.sidebar.write(f'You selected: {option}')
