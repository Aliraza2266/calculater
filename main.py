import streamlit as st
from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

# Streamlit title
st.title("Simple Calculator")

# Function to perform calculation
def perform_calculation(x, y, operator):
    if operator == '+':
        return add(x, y)
    elif operator == '-':
        return subtract(x, y)
    elif operator == '*':
        return multiply(x, y)
    elif operator == '/':
        return divide(x, y)
    else:
        return "Invalid operator!"

# Input elements in Streamlit
x = st.number_input("Enter the first number:", value=0.0)
y = st.number_input("Enter the second number:", value=0.0)
operator = st.selectbox("Choose an operator:", ["+", "-", "*", "/"])

# Calculate button
if st.button("Calculate"):
    result = perform_calculation(x, y, operator)
    st.write(f"Result: {result}")

# Quit button
if st.button("Quit"):
    st.stop()
