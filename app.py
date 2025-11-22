import streamlit as st
import math

st.set_page_config(page_title="Professional Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Professional Calculator")
st.write("A clean, powerful multi-mode calculator built using Streamlit.")

# Sidebar mode selector
mode = st.sidebar.selectbox(
    "Select Calculator Mode",
    ["Basic", "Scientific", "Programmer", "Percentage", "Area Calculator"]
)

st.header(f"{mode} Mode")


# ---------------- BASIC CALCULATOR ----------------
if mode == "Basic":
    num1 = st.number_input("Enter Number 1", value=0.0)
    num2 = st.number_input("Enter Number 2", value=0.0)
    operator = st.selectbox("Choose Operation", ["+", "-", "*", "/"])

    if st.button("Calculate"):
        try:
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2

            st.success(f"Result: {result}")
        except Exception as e:
            st.error(f"Error: {e}")


# ---------------- SCIENTIFIC CALCULATOR ----------------
elif mode == "Scientific":
    st.subheader("Enter a mathematical expression")

    expression = st.text_input(
        "Example: sin(30), sqrt(16), log(10), 5*7 + 3",
        placeholder="Type your expression..."
    )

    # Allowed functions for safe evaluation
    safe_dict = {
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tan": lambda x: math.tan(math.radians(x)),
        "sqrt": math.sqrt,
        "log": math.log10,
        "ln": math.log,
        "pi": math.pi,
        "e": math.e,
    }

    if st.button("Evaluate"):
        try:
            result = eval(expression, {"__builtins__": None}, safe_dict)
            st.success(f"Result: {result}")
        except Exception as e:
            st.error(f"Invalid expression: {e}")


# ---------------- PROGRAMMER CALCULATOR ----------------
elif mode == "Programmer":
    st.subheader("Number Conversion (Programmer Mode)")

    n = st.number_input("Enter an Integer", value=0, step=1)

    if st.button("Convert"):
        st.info(f"Binary: {bin(n)}")
        st.info(f"Octal: {oct(n)}")
        st.info(f"Hexadecimal: {hex(n)}")


# ---------------- PERCENTAGE CALCULATOR ----------------
elif mode == "Percentage":
    st.subheader("Find X% of Y")
    percent = st.number_input("Percentage (X)", value=0.0)
    value = st.number_input("Value (Y)", value=0.0)

    if st.button("Compute"):
        st.success(f"{percent}% of {value} = {(percent/100) * value}")

    st.markdown("---")
    st.subheader("Increase / Decrease Percentage")

    base_value = st.number_input("Base Value", value=0.0, key="base_val")
    pct = st.number_input("Percentage", value=0.0, key="pct_val")
    action = st.radio("Action", ["Increase", "Decrease"])

    if st.button("Apply"):
        if action == "Increase":
            result = base_value + (base_value * pct / 100)
        else:
            result = base_value - (base_value * pct / 100)
        st.success(f"Result: {result}")


# ---------------- AREA CALCULATOR ----------------
elif mode == "Area Calculator":
    st.subheader("Choose Shape")
    shape = st.selectbox("Shape", ["Square", "Rectangle", "Circle", "Triangle"])

    if shape == "Square":
        side = st.number_input("Side Length", value=0.0)
        if st.button("Calculate Area"):
            st.success(f"Area: {side ** 2}")

    elif shape == "Rectangle":
        width = st.number_input("Width", value=0.0)
        height = st.number_input("Height", value=0.0)
        if st.button("Calculate Area"):
            st.success(f"Area: {width * height}")

    elif shape == "Circle":
        radius = st.number_input("Radius", value=0.0)
        if st.button("Calculate Area"):
            st.success(f"Area: {math.pi * radius * radius}")

    elif shape == "Triangle":
        base = st.number_input("Base", value=0.0)
        height = st.number_input("Height", value=0.0)
        if st.button("Calculate Area"):
            st.success(f"Area: {0.5 * base * height}")
