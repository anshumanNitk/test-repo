import streamlit as st
import math

def calculate_area(radius: float) -> float:
    """Return area of a circle given its radius."""
    return math.pi * radius ** 2

def main():
    st.title("Circle Area Calculator")

    # Get user input
    radius = st.number_input(
        "Enter the circle's radius:",
        min_value=0.0,
        value=1.0,
        step=0.1,
        format="%.2f",
    )

    if st.button("Calculate Area"):
        area = calculate_area(radius)
        st.success(f"The area of a circle with radius {radius:.2f} is **{area:.2f}**")

if __name__ == "__main__":
    main()
